# 1. Замена пропущенного элемента средним арифметическим
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
average = sum(num for num in numbers if num is not None) / len([num for num in numbers])

numbers[numbers.index(None)] = average

print("Измененный список:", numbers)
