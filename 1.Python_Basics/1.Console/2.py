side_quadrate = input("Введите длину стороны квадрата: ")
measure_quadrate = input("Введите единицу измерения(сокращенно): ")
perimeter_quadrate = float(side_quadrate) * 4
square_quadrate = float(side_quadrate) ** 2
print("Периметр квадрата: ", perimeter_quadrate, measure_quadrate)
print("Площадь квадрата: ", square_quadrate, measure_quadrate + u"\u00B2")

length_rectangle = float(input("Введите длину прямоугольника: "))
width_rectangle = float(input("Введите ширину прямоугольника: "))
measure_rectangle = input("Введите единицу измерения(сокращенно):  ")
print("Периметр квадрата: ", length_rectangle * 2 + width_rectangle * 2, measure_rectangle)
print("Площадь квадрата: ", length_rectangle * width_rectangle, measure_rectangle + u"\u00B2")