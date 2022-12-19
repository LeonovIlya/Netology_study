age = input("Введите возраст: ")
height = input("Введите рост: ")
children = input("Есть ли дети? (да/нет): ")
study = input("Учитесь? (да/нет): ")
if age.isdigit() and height.isdigit():
    if 18 <= int(age) <= 27 and children == "нет" and study == "нет":
        if int(height) < 170:
            print('В танкисты')
        elif int(height) < 185:
            print('На флот')
        elif int(height) < 200:
            print('В десантники')
        else:
            print('В другие войска')
    else:
        print('Поздравляем! Вы не подлежите призыву')
else:
    print("Некорректные данные")
