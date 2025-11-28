import argparse
import sys
from pathlib import Path


from src.lib.text import normalize, tokenize, count_freq, top_n


# команда cat
def cmd_cat(path: Path, number: bool):
    if not path.exists():
        raise FileNotFoundError(f"файл не найден: {path}")

    with path.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.rstrip("\n")
            if number:
                print(f"{i} {line}")
            else:
                print(line)


# команда stats
def cmd_stats(path: Path, top: int):
    if not path.exists():
        raise FileNotFoundError(f"файл не найден: {path}")

    text = path.read_text(encoding="utf-8")
    normalized = normalize(text)  # нормализуем текст
    tokens = tokenize(normalized)  # разбиваем на слова
    freq = count_freq(tokens)  # считаем частоты
    top_words = top_n(freq, top)  # берём топ-n слов

    # выводим результаты
    print(f"всего слов: {len(tokens)}")
    print(f"уникальных слов: {len(set(tokens))}")
    print(f"топ-{top}:")
    for word, count in top_words:
        print(f"{word}:{count}")


# создаём парсер аргументов
def build_parser():
    parser = argparse.ArgumentParser(description="cli для cat и stats")
    sub = parser.add_subparsers(dest="cmd")

    # подкоманда cat
    p_cat = sub.add_parser("cat", help="вывести файл построчно")
    p_cat.add_argument("--input", required=True)
    p_cat.add_argument("-n", action="store_true", help="нумеровать строки")

    # подкоманда stats
    p_st = sub.add_parser("stats", help="анализ частот слов")
    p_st.add_argument("--input", required=True)
    p_st.add_argument("--top", type=int, default=5)

    return parser


# main - точка входа
def main(argv=None):
    argv = argv or sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.cmd == "cat":
            cmd_cat(Path(args.input), args.n)
        elif args.cmd == "stats":
            cmd_stats(Path(args.input), args.top)
        else:
            parser.print_help()
    except FileNotFoundError as e:
        parser.error(str(e))


if __name__ == "__main__":
    main()
