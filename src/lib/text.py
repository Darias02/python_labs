import re  
from typing import Dict, List, Tuple

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not text:
        return []
    
    
    # 1. Приводим к нижнему регистру
    if casefold:
        text = text.casefold()
    
    # 2. Заменяем ё на е
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    
    # 3. Заменяем управляющие символы на пробелы
    text = text.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')
    
    # 4. Убираем лишние пробелы
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text




def tokenize(text: str) -> list[str]:
    if not text:
        return []
    
    # Регулярное выражение для поиска слов
    # \w+ - одна или более букв/цифр/подчёркивания
    # (?:-\w+)* - ноль или более повторов: дефис + буквы/цифры/подчёркивания
    pattern = r'\w+(?:-\w+)*'
    
    # re.findall возвращает все непересекающиеся совпадения шаблона
    tokens = re.findall(pattern, text)
    
    return tokens
    pass

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq_dict = {}
    
    for token in tokens:
        # get возвращает текущее значение или 0 если ключа нет
        freq_dict[token] = freq_dict.get(token, 0) + 1
    
    return freq_dict
    pass

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    # Преобразуем словарь в список кортежей
    items = list(freq.items())
    
    # Сортируем: сначала по частоте (убывание), потом по слову (возрастание)
    # -x[1] для убывания частоты, x[0] для возрастания слова
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    
    # Возвращаем первые n элементов
    return sorted_items[:n]
    pass





