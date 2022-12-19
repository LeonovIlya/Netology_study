month = input("Введите месяц: ")
day = int(input("Введите число: "))

if (21 <= day <= 31 and month == "март") or (1 <= day <= 19 and month == "апрель"):
    print("Овен")

elif (20 <= day <= 30 and month == "апрель") or (1 <= day <= 20 and month == "май"):
    print("Телец")

elif (21 <= day <= 31 and month == "май") or (1 <= day <= 21 and month == "июнь"):
    print("Близнецы")

elif (22 <= day <= 30 and month == "июнь") or (1 <= day <= 22 and month == "июль"):
    print("Рак")

elif (23 <= day <= 31 and month == "июль") or (1 <= day <= 22 and month == "август"):
    print("Лев")

elif (23 <= day <= 31 and month == "август") or (1 <= day <= 22 and month == "сентябрь"):
    print("Дева")

elif (23 <= day <= 30 and month == "сентябрь") or (1 <= day <= 23 and month == "октябрь"):
    print("Весы")

elif (24 <= day <= 31 and month == "октябрь") or (1 <= day <= 22 and month == "ноябрь"):
    print("Скорпион")

elif (23 <= day <= 30 and month == "ноябрь") or (1 <= day <= 21 and month == "декабрь"):
    print("Стрелец")

elif (22 <= day <= 31 and month == "декабрь") or (1 <= day <= 20 and month == "январь"):
    print("Козерог")

elif (21 <= day <= 31 and month == "январь") or (1 <= day <= 18 and month == "февраль"):
    print("Водолей")

elif (19 <= day <= 29 and month == "февраль") or (1 <= day <= 20 and month == "март"):
    print("Рыбы")
else:
    print("Некорректные данные!")
