m = int(input('Минуты:'))
print(f'{m//60}:{(2 - len(str(m%60)))*'0' + str(m%60)}')
