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
    





