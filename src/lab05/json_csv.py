# JSON↔CSV
#работа с файлами, валидация ошибок
#A
import json
import csv
from pathlib import Path
def json_to_csv(json_path: str, csv_path: str) -> None:
    json_file = Path(json_path)
    csv_file = Path(csv_path)
    if not json_file.exists(): # проверка существует ли исходный JSON файл
        raise FileNotFoundError(f'JSON файл не найден: {json_path}')
    data = None # хранение данных из JSON
    
    try:
        with json_file.open('r', encoding='utf-8') as f: # чтение JSON файла
            data = json.load(f) # загружаем JSON данные
            
    except json.JSONDecodeError as e:
        raise ValueError(f'Неверный формат JSON в файле {json_path}: {str(e)}')
    except UnicodeDecodeError as e:
        raise ValueError(f'Проблема с кодировкой файла {json_path}: {str(e)}')
    
    # валидация структуры данных
    if not isinstance(data, list): # проверка, что данные являются списком
        raise ValueError(f'JSON должен содержать список объектов, получен {type(data).__name__}')
    if len(data) == 0:
        raise ValueError('Пустой JSON файл')
    
    for item in data: # проверка, что все элементы списка являются словарями
        if not isinstance(item, dict):
            raise ValueError(f'элемент/элементы не являются словарями')
    all_keys = set()
    for item in data:
        all_keys.update(item.keys()) # добавляем все ключи текущего словаря в множество
    
    if not all_keys: # если все словари пустые
        raise ValueError('JSON не содержит никаких полей (все словари пустые)')
    fieldnames = sorted(all_keys) 
    csv_file.parent.mkdir(parents=True, exist_ok=True) # создание директории для CSV файла, если она не существует
    
    try:
        with csv_file.open('w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames) # Создание DictWriter с определенными колонками
            writer.writeheader()# запись заголовока
            
            for item in data:
                row = {}
                for key in fieldnames:
                    row[key] = item.get(key, '')
                writer.writerow(row)
                
    except PermissionError as e:
        raise ValueError(f'Нет прав для записи в файл {csv_path}: {str(e)}')
    except Exception as e:
        raise ValueError(f'Ошибка при записи CSV файла: {str(e)}')

def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_file = Path(csv_path)
    json_file = Path(json_path)
    
    try:
        with csv_file.open('r', encoding='utf-8', newline='') as f: 
            sample = f.read(1024) # определение диалекта
            dialect = csv.Sniffer().sniff(sample)
            f.seek(0) # возвращаемся к началу после sniff
            data = list(csv.DictReader(f, dialect=dialect))

        if not csv.Sniffer().has_header(sample):
                raise ValueError('CSV файл не содержит заголовка')
            
    except FileNotFoundError:
        raise FileNotFoundError('файл не найден')
    except Exception as e:
        raise ValueError(f'Ошибка при записи CSV файла: {str(e)}')
    if len(data) == 0:
        raise ValueError('Пустой JSON файл')
    
    try:
        with json_file.open('w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
                
    except PermissionError as e:
        raise ValueError(f'Нет прав для записи в файл {csv_path}: {str(e)}')
    except Exception as e:
        raise ValueError(f'Ошибка при записи CSV файла: {str(e)}')

if __name__ == '__main__':
    try:
        json_to_csv(
            'data/samples/people.json', 
            'data/out/people_from_json.csv'
        )
        print('тест json -> csv')
        csv_to_json(
            'data/samples/people.csv',
            'data/out/people_from_csv.json'
        )
        print('тест csv -> json')
    except Exception as e:
        print(f'Ошибка: {e}')