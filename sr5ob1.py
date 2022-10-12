from random import randint
n = int(input('введите число элементов последовательности '))
if n == 0:
    print('Ошибка. Число элементов последовательности должно быть больше 0')
else:
    sp = [0] * n
    print('введите', n, 'элементов или нажмите Enter для случайной генерации элемента')
    for i in range(n):
        sp[i] = input()
        if sp[i] == '':
            sp[i] = float(randint(1, 100))
        else:
            sp[i] = float(sp[i])
    print(sp)
    maxElem = 0
    nommax = 0
    for i in range(n):
        if sp[i] > maxElem:
            maxElem = sp[i]
            nommax = i
    for i in range(nommax + 1, n):
        sp[i] = 0
    print(sp)
