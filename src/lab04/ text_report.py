import sys
from pathlib import Path
from collections import Counter

sys.path.insert(
    0, str((Path(__file__).parent.parent))
)  # добавлят корень проекта в начало списка
from lib.text import normalize, tokenize, top_n
from lab04.io_txt_csv import read_text, write_csv


def frequencies_from_text(text: str) -> dict[str, int]:  # подсчитывает частоты слов
    tokens = tokenize(normalize(text))
    return Counter(tokens)


def sorted_word_counts(
    freq: dict[str, int],
) -> list[tuple[str, int]]:  # сортировка по убыванию частоты, по авфавиту
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def report(
    input_path: Path, output_path: Path, encoding: str = "utf-8"
) -> dict[str, int]:  # очтёт
    try:
        if input_path.suffix.lower() != ".txt":
            raise ValueError(
                f"входной файл должен быть .txt, получен: {input_path.suffix}"
            )

        if output_path.suffix.lower() != ".csv":
            raise ValueError(
                f"выходной файл должен быть .csv, получен: {output_path.suffix}"
            )
        text = read_text(input_path, encoding=encoding)
        if not text.strip():
            print("файл пустой")
            header = ("word", "count")
            write_csv([], output_path, header)  # Только заголовок
            return ""
        freq = frequencies_from_text(text)
        sorted_counts = sorted_word_counts(freq)
        header = ("word", "count")  # заголовок
        write_csv(sorted_counts, output_path, header)
        return freq
    except FileNotFoundError:
        print(f"FileNotFoundError")
        sys.exit(1)  # завершение программы с ошибкой

    except Exception as e:
        print(f"ошибка обработки {e}")
        sys.exit(1)


def main():
    input_file = Path("data/lab04/input.txt")
    output_file = Path("data/lab04/report.csv")  # путь для выхода
    print(f"...обработка файла: {input_file}")
    try:
        frequencies = report(input_file, output_file)
        sum_words = sum(frequencies.values())  # кол-во слов
        unique_words = len(frequencies)  # кол-во уникальных слов
        top_words = top_n(frequencies, 5)
        print(f"Всего слов: {sum_words}")
        print(f"Уникальных слов: {unique_words}")
        print("Топ-5:")

        for word, count in top_words:
            print(f"  {word}: {count}")
    except Exception as e:
        print(f"ошибка {e}")


if __name__ == "__main__":
    main()
