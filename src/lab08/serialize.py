import json
from typing import List
from .models import Student


def save_students_to_json(path: str, students: List[Student]):
    data = [s.to_dict() for s in students]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def load_students_from_json(path: str) -> List[Student]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Student.from_dict(item) for item in data]


if __name__ == "__main__":
    students = load_students_from_json("data/lab08/students_input.json")
    save_students_to_json("data/lab08/students_output.json", students)
    print("студенты, загруженные из students_input.json:")
    for student in students:
        print(student)
