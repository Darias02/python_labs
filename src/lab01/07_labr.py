a, sl, alf, ch = input(), '', 'QWERTYUIOPASDFGHJKLZXCVBNM', '1234567890'
shag = []
for i in range(len(a)):
    if a[i] in alf: 
        sl+=a[i]
        shag.append(i)
        break
for i in range(len(a)):
    if a[i] in ch:
        sl+=a[i+1]
        shag.append(i+1)
        break
for i in range(len(a)):
    if shag[-1]-shag[-2] == i-shag[-1]:
        sl+=a[i]
        shag.append(i)
if sl[-1] == '.': print(sl)
else: print(sl)

