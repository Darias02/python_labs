import sys
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
