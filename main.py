old = int(input('Ваш возраст: '))

print('Рекомендовано:', end=' ')

if 3 <= old < 6:
    print('"Заяц в лабиринте"')

if 6 <= old < 12:
    print('"Марсианин"')

if 12 <= old < 16:
    print('"Загадочный остров"')

if 16 <= old:
    print('"Поток сознания"')