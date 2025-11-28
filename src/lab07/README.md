# ЛР 7
# Тестирование: pytest + стиль (black)




## Реализация и тестирование функций из двух модулей:
src/lib/text.py – функции обработки текста:
normalize(text: str) -> str – приведение текста к нижнему регистру, замена символов ё на е, удаление лишних пробелов;
tokenize(text: str) -> list[str] – разбиение текста на токены (слова);
count_freq(tokens: list[str]) -> dict[str, int] – подсчет частоты встречаемости токенов;
top_n(freq: dict[str, int], n: int = 3) -> list[tuple[str, int]] – топ N слов по частоте с учётом алфавитной сортировки при равной частоте.
src/lab05/json_csv.py – функции конвертации файлов:
json_to_csv(src_path: str, dst_path: str) – конвертация JSON → CSV;
csv_to_json(src_path: str, dst_path: str) – конвертация CSV → JSON.


### терминал:
![Вывод:](./images/lab07/test_nb.png)

![Вывод:](./images/lab07/test_tb.png)

![Вывод:](./images/lab07/test_cf.png)

![Вывод:](./images/lab07/test_tn.png)

![Вывод:](./images/lab07/test_jtcr.png)

![Вывод:](./images/lab07/test_if.png)

![Вывод:](./images/lab07/test_nf.png)


## Приведение к единому стилю
```bash
black .
```

## Проверка на соответствие кода стилю black:
![Вывод:](./images/lab07/black.png) 
