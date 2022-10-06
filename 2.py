katet1, katet2, gipotenuza = float(input('Введите длину первого катета: ')), float(input('Введите длину второго катета: ')), float(input('Введите длину гипотенузы: '))
if katet1**2 + katet2**2 == gipotenuza**2:
    print('Площадь =', katet1*katet2/2, 'Периметр =', katet1+katet2+gipotenuza)
else:
    print('Ошибка, данный треугольник не прямоугольный')
