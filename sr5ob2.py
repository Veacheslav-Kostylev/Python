from random import randint
n = int(input('введите число элементов 1 последовательности '))
if n == 0:
    print('Ошибка. Число элементов последовательности должно быть больше 0')
else:
    sp1 = [0] * n
    print('введите', n, 'элементов или нажмите Enter для случайной генерации элемента')
    for i in range(n):
        sp1[i] = input()
        if sp1[i] == '':
            sp1[i] = int(randint(1, 100))
        else:
            sp1[i] = int(sp1[i])
    print(sp1)
m = int(input('введите число элементов 2 последовательности '))
if m == 0:
    print('Ошибка. Число элементов последовательности должно быть больше 0')
else:
    sp2 = [0] * m
    print('введите', m, 'элементов или нажмите Enter для случайной генерации элемента')
    for i in range(m):
        sp2[i] = input()
        if sp2[i] == '':
            sp2[i] = int(randint(1, 100))
        else:
            sp2[i] = int(sp2[i])
    print(sp2)
print('Общие элементы для 1 и 2 последовательностей:')
for i in range(n):
    for j in range(m):
        if sp1[i] == sp2[j]:
            print(sp1[i])
            break

