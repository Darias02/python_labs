import csv
from pathlib import Path  # для работы с путями файлов
from typing import Iterable, Sequence


def read_text(
    path: str | Path, encoding: str = "utf-8"
) -> str:  # чтение содержимого файла
    path = Path(path)
    if path.suffix.lower() != ".txt":
        raise ValueError(f"файл {path} должен иметь расширение .txt")
    return path.read_text(encoding=encoding)


def write_csv(
    rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    path = Path(path)
    if path.suffix.lower() != ".csv":
        raise ValueError(f"файл {path} должен иметь расширение .csv")
    rows = list(rows)
    if rows:
        first_len = len(rows[0])
        for i, roww in enumerate(rows):  # возвращает индекс, элемент
            if len(roww) != first_len:
                raise ValueError(
                    f"Строка {i} имеет длину {len(roww)}, ожидалось {first_len}"
                )

    with path.open("w", newline="", encoding="utf-8") as f:  # открытие файла для записи
        w = csv.writer(f)
        if header is not None:  # eсли передан заголовок
            w.writerow(header)
        for r in rows:
            w.writerow(r)  # построчно записывает в csv


if __name__ == "__main__":
    print("тест")
    try:
        txt = read_text("data/lab04/input.txt")  # должен вернуть строку
        print(f"Прочитано {len(txt)} символов")
        print(f"Первые 50 символов: {txt[:50]}")
    except FileNotFoundError:
        print("Файл не нвйден")
    except Exception as e:
        print("ошибка при чтении {e}")

    try:
        write_csv([("word", "count"), ("test", 3)], "data/check.csv")  # создаст CSV
    except Exception as e:
        print("ошибка при создании CSV")
