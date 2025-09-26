N, och, home = int(input()), 0, 0
for i in range(N):
    a = input().split()
    if a[-1] == 'True': och+=1
    else: home+=1
print(f'очный формат обучения: {och}\nзаочный формат обучения:{home}')
