# Приветствие
def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")
greet()

# 1. Создание поля
field = [['-'] * 3 for _ in range(3)] #поле

def show_field(f): # функция для вывода поля
    print('  0 1 2')
    for i in range(len(f)):
        print(str(i), *(f[i]))
#show_field(field)

# 2. Проверка координат
def users_input(f):
    while True:
        cords = input("Ваш ход: ").split()
        if len(cords) != 2:                                  #Проверка координат на количество
            print(" Введите 2 координаты! ")
            continue

        x, y = cords
        if not (x.isdigit() and y.isdigit()):                 #Проверка координат на принадлежность к числам
            print('Введите числа')
            continue

        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:                   #Проверка диапозона координат
            print(" Координаты вне диапазона! ")
            continue

        if f[x][y] != "-":                                     #Проверка занятой клетки
            print(" Клетка занята! ")
            continue

        return x, y
#users_input(field)

# 3. Проверка выигрыша
def win(f,user):
    f_list = []
    for l in f:
        f_list += l
    positions = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    indices = set([i for i, x in enumerate(f_list) if x == user])   #Сохранение позиций, если пользователь ввел одну из перечисленных позиций
                                                                    # i, x - индекс и значение списка
    for p in positions:
        if len(indices.intersection(set(p))) == 3:
            return True
    return False
#win(field, users_input)

# 4. Ввод координат
count = 0

while True:
    show_field(field)
    count += 1
    if count % 2 == 1:                #Первым ходит крестик
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    if count % 2 == 1:
        user = "X"
    else:
        user = "0"

    if count < 9:
        x, y = users_input(field)
        field[x][y] = user

    if count == 9:                        #Условие для ничьи
        print(" Ничья!")
        break

    if win(field, user):                  # Условие для выигрыша
        print(f"Выйграл {user}")
        break










