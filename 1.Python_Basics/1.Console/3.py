salary = int(input("Введите заработную плату в месяц в рублях: "))
period = int(input("Введите период в месяцах: "))
percent_slavery = int(input("Введите, какой процент(%) уходит на ипотеку: "))
percent_life = int(input("Введите, какой процент(%) уходит на жизнь: "))
spend_slavery = (salary * period) * (percent_slavery / 100)
bank = ((salary * period) * (percent_life / 100)) - spend_slavery
print("На ипотеку было потрачено: ", spend_slavery, "рублей")
print("Было накоплено: ", bank, "рублей")