while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        print('цикл закончен')
        break
    if len(s) < 3:
        print('Слишком мало')
        continue
    print('''Введённая строка достаточной длины. Для завершения цикла введите "выход"''')
# Разные другие действия здесь...