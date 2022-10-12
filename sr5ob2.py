n = int(input('введите число элементов последовательности '))
sp = [0] * n
print('введите', n, 'элементов')
for i in range(n):
    sp[i] = int(input())
for i in range(len(sp)):
    if sp[i] % 2 == 0:
        sp[i] += 5
    else:
        sp[i] = 0
print(sp)