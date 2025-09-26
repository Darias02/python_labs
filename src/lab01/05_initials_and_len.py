slov = 'ЙЦУКЕНГШЩЗХЪЁФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNM'
fio = input('ФИО:')
fio = fio.replace(' ', '')
inc = ''
for i in fio:
    if i in slov: inc += i
print(f'Инициалы: {inc}.\nДлина (символов): {len(fio)+2}')
