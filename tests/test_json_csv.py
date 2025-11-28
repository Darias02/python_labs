import pytest
import json
import csv
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


# позитивные сценарии
@pytest.mark.parametrize(
    "json_data, csv_fieldnames",
    [
        ([{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}], ["name", "age"]),
        ([{"item": "apple", "qty": 10}, {"item": "banana", "qty": 5}], ["item", "qty"]),
    ],
)
def test_json_to_csv_roundtrip(tmp_path: Path, json_data, csv_fieldnames):
    src_json = tmp_path / "src.json"
    dst_csv = tmp_path / "out.csv"
    roundtrip_json = tmp_path / "roundtrip.json"

    src_json.write_text(
        json.dumps(json_data, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # JSON -> CSV
    json_to_csv(str(src_json), str(dst_csv))
    assert dst_csv.exists()

    # CSV -> JSON
    csv_to_json(str(dst_csv), str(roundtrip_json))
    assert roundtrip_json.exists()

    # проверка, что количество записей и ключи совпадают
    with roundtrip_json.open(encoding="utf-8") as f:
        data_after = json.load(f)
    assert len(data_after) == len(json_data)
    for record in data_after:
        assert set(csv_fieldnames) <= set(record.keys())


# негативные сценарии
@pytest.mark.parametrize(
    "write_content, func",
    [
        ("", json_to_csv),  # пустой JSON
        ("{not: valid}", json_to_csv),  # некорректный JSON
        ("", csv_to_json),  # пустой CSV
        ("name,age\nAlice", csv_to_json),  # некорректный CSV
    ],
)
def test_invalid_files(tmp_path: Path, write_content, func):
    src = tmp_path / "input.file"
    dst = tmp_path / "output.file"
    src.write_text(write_content, encoding="utf-8")
    with pytest.raises(ValueError):
        func(str(src), str(dst))


@pytest.mark.parametrize("func", [json_to_csv, csv_to_json])
def test_nonexistent_file(tmp_path: Path, func):
    src = tmp_path / "does_not_exist.file"
    dst = tmp_path / "output.file"
    with pytest.raises(FileNotFoundError):
        func(str(src), str(dst))
