countLet, countExp = int(input('Введите количство лет: ')), int(input('Введите количство экспонатов: '))
if countLet <= 0 or countExp <= 0:
    print('Введены неверные данные. Колличество лет и экспонатов должно быть больше 0')
elif countLet and countExp > 0:
    countExp_for_one_day = 8 * 60 / 5
    print('За данное количество лет будет просмотрено ' + str(int(countLet*365 * countExp_for_one_day)) + ' экспонатов')
    print('Данное количество экспонатов будет просмотрено за' + ' ' + str(int(countExp/countExp_for_one_day//365)) + ' Год(Года/Лет) и ' + str(int(countExp/countExp_for_one_day % 365)) + ' день(дней) или за ' + str(int(countExp/countExp_for_one_day)) + ' дней')