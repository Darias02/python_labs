# python_labs
# Лабораторная работа 1
## Задание 1
![Код:](./images/lab01/01.png)
![Вывод:](./images/lab01/01r.png)

## Задание 2
![Код:](./images/lab01/02.png)
![Вывод:](./images/lab01/02r.png)

## Задание 3
![Код:](./images/lab01/03.png)
![Вывод:](./images/lab01/03r.png)

## Задание 4
![Код:](./images/lab01/04.png)
![Вывод:](./images/lab01/04r.png)

## Задание 5
![Код:](./images/lab01/05.png)
![Вывод:](./images/lab01/05r.png)

## Задание 6
![Код:](./images/lab01/06.png)
![Вывод:](./images/lab01/06r.png)

## Задание 7
![Код:](images/lab01/07.png)
![Вывод:](./images/lab01/07r.png)

# Лабораторная работа 2

## Задание 1 - arrays
### min_max
```python
test_m_m = [
    [3, -1, 5, 5, 0],
    [42],
    [-5, -2, -9],
    [],
    [1.5, 2, 2.0, -3.1]
]
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0: 
        return 'ValueError'
    return (min(nums), max(nums)) 
for i in test_m_m:
    print(min_max(i))
```
### unique_sorted
```python
test_u_s = [
    [3, 1, 2, 1, 3],
    [],
    [-1, -1, 0, 2, 2],
    [1.0, 1, 2.5, 2.5, 0]
]
def unique_sorted(nums2: list[float | int]) -> list[float | int]:
    if len(nums2) == 0: 
        return 'ValueError'
    return sorted(set(nums2))
for i in test_u_s:
    print(unique_sorted(i))
```

### flatten
```python
fl_test = [
    [[1, 2], [3, 4]],
    ([1, 2], (3, 4, 5)),
    [[1], [], [2, 3]],
    [[1, 2], "ab"]
]
def flatten(mat: list[list | tuple]) -> list:
    result = []
    for a in mat:
        if isinstance(a, (list, tuple)): result.extend(flatten(a))
        else:
            if type(a) == int or type(a) == float: result.append(a)
            else: return 'TypeError'
    return result
for i in fl_test:
    print(flatten(i))
```
![Вывод:](./images/lab02/1x.png)

## Задание 2 - matrix
### transpose
```python

test_t = [
    [[1, 2, 3]],
    [[1], [2], [3]],
    [[1, 2], [3, 4]],
    [],
    [[1, 2], [3]]
]


def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    len_mat = len(mat[0])
    for i in mat:
        if len(i) != len_mat:
            return 'ValueError'

    len_column = len(mat[0]) 
    result_t = [[] for _ in range(len_column)]
    
    for str in range(len(mat)): 
        for column in range(len_column):  
            result_t[column].append(mat[str][column])  
    
    return result_t

for i in test_t:
    print(transpose(i))
```
### row_sums
```python
test_rs = [
    [[1, 2, 3], [4, 5, 6]],
    [[-1, 1], [10, -10]],
    [[0, 0], [0, 0]],
    [[1, 2], [3]]
]


def row_sums(mat: list[list[float | int]]) -> list[float]:
    res = []
    len_column = len(mat[0])
    for i in mat:
        if len(i) != len_column:
            return 'ValueError'
    for row in mat:
        row_sum = sum(row)
        res.append(row_sum)
    return res
for i in test_rs:
    print(row_sums(i))
```



### col_sums
```python
test_cs = [
    [[1, 2, 3], [4, 5, 6]],
    [[-1, 1], [10, -10]],
    [[0, 0], [0, 0]],
    [[1, 2], [3]]
]

def col_sums(mat: list[list[float | int]]) -> list[float]:
    result_cs = []
    len_str = len(mat[0])
    result_cs = [0] * len_str
    for i in mat:
        if len(i) != len_str:
            return 'ValueError'
        
    for column in mat:
        k = 0
        for strok in column:
            result_cs[k%len_str] = result_cs[k%len_str] + strok
            k+=1
    return result_cs
for i in test_cs:
    print(col_sums(i))
```

![Вывод:](./images/lab01/02r.png)

## Задание 3 - tuples
```python
test_input = [
    ("Иванов Иван Иванович", "BIVT-25", 4.6),
    ("Петров Пётр", "IKBO-12", 5.0),
    ("Петров Пётр Петрович", "IKBO-12", 5.0),
    ("  сидорова  анна   сергеевна ", "ABB-01", 3.999), 
    (' FJJ ', 'RR'),
    ('WER', 'Det', 52), 
    ('qw', '', 53.9)
]
def format_record(rec: tuple[str, str, float]) -> str: 
    if not isinstance(rec[2], float):
        return TypeError
    try: 
        len(rec)!= 3 or type(rec[0]) != str or type(rec[1]) != str or type(rec[2]) != float or len(rec[0])==0 or len(rec[1])==0 
    
        name, gr, gpa = rec
    
        name = name.split()
        if len(name) == 3: name = f'{name[0].title()} {name[1][0].upper()}.{name[1][0].upper()}.'
        else: name = f'{name[0].title()} {name[1][0].upper()}.'
        return f'{name}, гр. {gr}, GPA {gpa}'
    except:
        return TypeError

for i in test_input:
    print(format_record(i))
```
![Вывод:](./images/lab02/3x.png)


# Лабораторная работа 3
## text.py
* _файл для хранения функций_
```python
import re  

def normalize(text: str, *, casefold: bool = True, replacement: bool = True) -> str:
    if not text:
        return ''
    
    
    if casefold:
        text = text.casefold()
    
    if replacement:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    
    text = text.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')
    
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


def tokenize(text: str) -> list[str]:
    if not text:
        return []
    pattern = r'\w+(?:-\w+)*'
    tokens = re.findall(pattern, text)
    
    return tokens

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq_dict = {}
    
    for token in tokens:
        freq_dict[token] = freq_dict.get(token, 0) + 1
    return freq_dict  

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = list(freq.items())
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]
```
## text_stats.py
* _файл с реализацией функций_
```python
iimport sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
from text import normalize, tokenize, count_freq, top_n

sys.path.append(os.path.join(os.path.dirname(__file__)))
from test import normalize_test, tokenize_test, count_freq__top_n_test


for i in normalize_test:
    print(normalize(i))
for i in tokenize_test:
    print(tokenize(i))
for i in count_freq__top_n_test:
    print(count_freq(i))
    print(top_n(count_freq(i)))


def main():
    text = sys.stdin.readline().strip()  
    if not text:
        print("Всего слов: 0")
        print("Уникальных слов: 0")
        print("Топ-5:")
        return
    
    normalized = normalize(text)
    tokens = tokenize(normalized)
    
    total = len(tokens)
    unique = len(set(tokens))
    freq_dict = count_freq(tokens)
    top_words = top_n(freq_dict, 5)
    
    print(f"Всего слов: {total}")
    print(f"Уникальных слов: {unique}")
    print(f"Топ-{min(5, len(set(tokens)))}:")
    for word, count in top_words:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()

```
### test.py
* _файл с тестами_
```python
normalize_test = [
    "ПрИвЕт\nМИр\t",
    "ёжик, Ёлка",
    "Hello\r\nWorld",
    "  двойные   пробелы  "
]


tokenize_test = [
    "привет мир",
    "hello,world!!!",
    "по-настоящему круто",
    "2025 год",
    "emoji 😀 не слово"
] 


count_freq__top_n_test = [
    ["a","b","a","c","b","a"],
    ["bb","aa","bb","aa","cc"]
]

```


#### Вывод:
![Вывод:](./images/lab03/img.png)

# Лабораторная работа 4


## файл io_txt_cvs.py
```python
import csv
from pathlib import Path #для работы с путями файлов
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = 'utf-8') -> str: #чтение содержимого файла
    path = Path(path)
    return path.read_text(encoding=encoding)




def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    if rows:
        first_len = len(rows[0])
        for i, roww in enumerate(rows): #возвращает индекс, элемент
            if len(roww) != first_len:
                raise ValueError(f'Строка {i} имеет длину {len(roww)}, ожидалось {first_len}') 
            
    with p.open('w', newline='', encoding='utf-8') as f: #открытие файла для записи
        w = csv.writer(f)
        if header is not None: #eсли передан заголовок
            w.writerow(header)
        for r in rows:
            w.writerow(r)



if __name__ == '__main__':
    print('тест')
    try:
        txt = read_text('data/lab04/input.txt')  # должен вернуть строку
        print(f'Прочитано {len(txt)} символов')
        print(f'Первые 50 символов: {txt[:50]}')
    except FileNotFoundError:
        print('Файл не нвйден')
    except Exception as e:
        print('ошибка при чтении')
    
    try:
        write_csv([('word','count'),('test',3)], 'data/check.csv')  # создаст CSV
    except Exception as e:
        print('ошибка при создании CSV')
```


## файл text_report.py
```python
port sys
from pathlib import Path
from collections import Counter 
sys.path.insert(0, str((Path(__file__).parent.parent))) #добавлят корень проекта в начало списка
from lib.text import normalize, tokenize, top_n
from lab04.io_txt_csv import read_text, write_csv
def frequencies_from_text(text: str) -> dict[str, int]: #подсчитывает частоты слов
    tokens = tokenize(normalize(text))
    return Counter(tokens) 

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]: #сортировка по убыванию частоты, по авфавиту
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
def report(input_path: Path, output_path: Path, encoding: str = 'utf-8') -> dict[str, int]: #очтёт
    try:
        text = read_text(input_path, encoding=encoding)
        if not text.strip():
            print('файл пустой')
            header = ('word', 'count')
            write_csv([], output_path, header)  # Только заголовок
            return {}
        
        
        freq = frequencies_from_text(text)
        sorted_counts = sorted_word_counts(freq)
        header = ('word', 'count') #заголовок
        write_csv(sorted_counts, output_path, header)
        return freq
    except FileNotFoundError:
        print(f'FileNotFoundError')
        sys.exit(1) #завершение программы с ошибкой
        
    except Exception as e:
        print(f'ошибка обработки {e}')
        sys.exit(1)



def main():
    input_file = Path('data/lab04/input.txt')
    output_file = Path('data/lab04/report.csv') #путь для выхода
    print(f'...обработка файла: {input_file}')
    try:
        frequencies = report(input_file, output_file)
        sum_words = sum(frequencies.values()) #кол-во слов
        unique_words = len(frequencies) #кол-во уникальных слов
        top_words = top_n(frequencies, 5)
        
        print(f'Всего слов: {sum_words}')
        print(f'Уникальных слов: {unique_words}')
        print('Топ-5:')

        for word, count in top_words:
            print(f'  {word}: {count}')
    except Exception as e:
        print(f'ошибка {e}')



if __name__ == '__main__':
    main()
```


## запуск 'Привет, мир! Привет!!!':

![Вывод:](./images/lab04/1.png)


![Вывод:](./images/lab04/1x.png)


![Вывод:](./images/lab04/1xx.png)
## запуск с пустым файлом input.txt:

![Вывод:](./images/lab04/2.png)


![Вывод:](./images/lab04/2x.png)


![Вывод:](./images/lab04/2xx.png)

## запуск с отсутствием файла input.txt:

![Вывод:](./images/lab04/0.png)
