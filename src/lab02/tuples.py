test_input = [
    ("Иванов Иван Иванович", "BIVT-25", 4.6),
    ("Петров Пётр", "IKBO-12", 5.0),
    ("Петров Пётр Петрович", "IKBO-12", 5.0),
    ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
]
def format_record(rec: tuple[str, str, float]) -> str:
    name, gr, gpa = rec
    
    name = name.split()
    if len(name) == 3: name = f'{name[0].title()} {name[1][0].upper()}.{name[1][0].upper()}.'
    else: name = f'{name[0].title()} {name[1][0].upper()}.'
    return f'{name}, гр. {gr}, GPA {gpa}'
for i in test_input:
    print(format_record(i))
