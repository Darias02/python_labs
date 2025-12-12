import csv
from pathlib import Path
from models import Student


class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.write_text("", encoding="utf-8")

    def _read_all(self):
        if not self.path.exists():
            return []

        with open(self.path, "r", encoding="utf-8") as f:
            read = csv.DictReader(f)
            if read.fieldnames != ["fio", "birthdate", "group", "gpa"]:
                return []

            return list(read)

    def _write_all(self, records):
        with open(self.path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
            writer.writeheader()
            if records:
                writer.writerows(records)

    def _ensure_storage_exists(self):
        if not self.path.exists() or self.path.stat().st_size == 0:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(
                    f, fieldnames=["fio", "birthdate", "group", "gpa"]
                )
                writer.writeheader()

    def list(self):
        if not self.path.exists():
            return []

        students = []
        with self.path.open(encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row["gpa"] = float(row["gpa"])
                    students.append(Student.from_dict(row))
                except (ValueError, KeyError) as e:
                    print(f"ошибка: {e}")
                    continue

        return students

    def add(self, student: Student):
        file_exists = self.path.exists() and self.path.stat().st_size > 0

        with self.path.open("a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])

            if not file_exists:
                writer.writeheader()

            writer.writerow(student.to_dict())

    def find(self, substr: str):
        return [r for r in self.list() if substr.lower() in r.fio.lower()]

    def remove(self, fio: str):
        records = self._read_all()
        filtered_records = [r for r in records if r["fio"] != fio]

        if len(filtered_records) == len(records):
            raise ValueError(f"студент {fio} не найден")

        self._write_all(filtered_records)

    def update(self, fio: str, **fields):
        records = self._read_all()
        updated = False

        for record in records:
            if record["fio"] == fio:
                allowed_fields = {"fio", "birthdate", "group", "gpa"}
                for field, value in fields.items():
                    if field in allowed_fields:
                        if field == "gpa":
                            try:
                                record[field] = str(float(value))
                            except ValueError:
                                raise ValueError(f"некорректное значение GPA: {value}")
                        else:
                            record[field] = value
                updated = True
                break

        if not updated:
            raise ValueError(f"студент {fio} не найден")

        self._write_all(records)


def main():
    csv_file = "data/lab09/students.csv"
    import os

    if os.path.exists(csv_file):
        os.remove(csv_file)

    group = Group(csv_file)

    # добавляем студентов
    students = [
        Student("Иванов Иван", "2003-10-10", "БИВТ-21-1", 4.3),
        Student("Петров Петр", "2002-05-15", "БИВТ-21-1", 4.7),
        Student("Сидорова Анна", "2003-02-20", "БИВТ-21-2", 4.9),
    ]

    print("добавляем студентов:")
    for student in students:
        group.add(student)
        print(f"  добавлен: {student.fio}")

    # показываем всех
    print("\nвсе студенты:")
    all_students = group.list()
    for s in all_students:
        print(f"  {s.fio}, {s.group}, GPA: {s.gpa}")

    # поиск
    print('\nпоиск "Иван":')
    found = group.find("Иван")
    for s in found:
        print(f"  найден: {s.fio}")

    # обновление
    print("\nобновляем Иванова:")
    try:
        group.update("Иванов Иван", gpa=4.8)
        print("  успешно обновлен")
    except ValueError as e:
        print(f"  ошибка: {e}")

    # удаление
    print("\nудаляем Петрова:")
    try:
        group.remove("Петров Петр")
        print("  успешно удален")
    except ValueError as e:
        print(f"  ошибка: {e}")

    # финальный список
    print("\nфинальный список:")
    final_students = group.list()
    for s in final_students:
        print(f"  {s.fio}, {s.group}, GPA: {s.gpa}")

    print(f"\nвсего студентов: {len(final_students)}")


if __name__ == "__main__":
    main()
