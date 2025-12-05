from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                f"неверный формат даты рждения: '{self.birthdate}'. "
                "ожидается: YYYY-MM-DD"
            )
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA должен быть в диапазоне 0-5, получен: {self.gpa}")

    def age(self) -> int:
        birth = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        years = today.year - birth.year
        if (today.month, today.day) < (birth.month, birth.day):
            years -= 1
        return years

    def to_dict(self) -> dict:
        if not all([self.fio, self.birthdate, self.group, self.gpa is not None]):
            raise ValueError("некоторые поля отсутствуют")
        if not isinstance(self.fio, str):
            raise TypeError(
                f"ФИО должно быть строкой, получено: {type(self.fio).__name__}"
            )
        if not isinstance(self.birthdate, str):
            raise TypeError(
                f"Дата рождения должна быть строкой, получено: {type(self.birthdate).__name__}"
            )
        if not isinstance(self.group, str):
            raise TypeError(
                f"группа должна быть строкой, получено: {type(self.group).__name__}"
            )
        if not isinstance(self.gpa, (int, float)):
            raise TypeError(
                f"GPA должен быть числом, получено: {type(self.gpa).__name__}"
            )
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA должен быть в диапазоне 0–5, получен: {self.gpa}")
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                f"формат даты рождения должен быть YYYY-MM-DD, получено: {self.birthdate}"
            )
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(clss, d: dict):
        return clss(
            fio=d.get("fio"),
            birthdate=d.get("birthdate"),
            group=d.get("group"),
            gpa=d.get("gpa"),
        )

    def __str__(self):
        return f"{self.fio}, {self.group}, GPA: {self.gpa}"
