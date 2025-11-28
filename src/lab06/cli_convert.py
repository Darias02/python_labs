import argparse
import sys
from pathlib import Path

# импортируем функции из lab05 напрямую
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


# создаём парсер аргументов
def build_parser():
    parser = argparse.ArgumentParser(description="конвертеры форматов")
    sub = parser.add_subparsers(dest="cmd")

    # json -> csv
    p1 = sub.add_parser("json2csv", help="конвертировать json->csv")
    p1.add_argument("--in", dest="input", required=True, help="входной файл (json)")
    p1.add_argument("--out", dest="output", required=True, help="выходной файл (csv)")

    # csv -> json
    p2 = sub.add_parser("csv2json", help="конвертировать csv->json")
    p2.add_argument("--in", dest="input", required=True, help="входной файл (csv)")
    p2.add_argument("--out", dest="output", required=True, help="выходной файл (json)")

    # csv -> xlsx
    p3 = sub.add_parser("csv2xlsx", help="конвертировать csv->xlsx")
    p3.add_argument("--in", dest="input", required=True, help="входной файл (csv)")
    p3.add_argument("--out", dest="output", required=True, help="выходной файл (xlsx)")

    return parser


def main(argv=None):
    argv = argv or sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.cmd == "json2csv":
            json_to_csv(args.input, args.output)
            print(f"{args.input} -> {args.output}")
        elif args.cmd == "csv2json":
            csv_to_json(args.input, args.output)
            print(f"{args.input} -> {args.output}")
        elif args.cmd == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
            print(f"{args.input} -> {args.output}")
        else:
            parser.print_help()
    except FileNotFoundError as e:
        parser.error(str(e))
    except Exception as e:
        parser.error(f"ошибка: {e}")


if __name__ == "__main__":
    main()
