#1
m = ["Круг", 0.25, "Квадрат", "треугольник", 15, "круг", "овал", 10]
m.remove(0.25)
m.remove(15)
m.remove(10)
print(m)
#2
abc =  ["A", "B", "C", "D", "E", "F", "G"]
del abc[1:5]
print(abc)
#3
numbers = [1,4]
numbers.insert(1,2)
numbers.insert(2,3)
print(numbers)
#4
mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]
mass = [x for x in mass if x >= 0]
sorted_asc = sorted(mass)
sorted_desc = sorted(mass, reverse = True)
print(sorted_asc)
print(sorted_desc)
#5
n = int(input("Введите количество чисел: "))

negative_numbers = []
positive_numbers = []
zeros = []             

for i in range(n):
    num = float(input("Введите число: "))
    
    if num < 0:
        negative_numbers.append(num)
    elif num > 0:
        positive_numbers.append(num)
    else: 
        zeros.append(num)

if negative_numbers:
    sum_negative = sum(negative_numbers)
    print(f"Сумма отрицательных чисел: {sum_negative}")
else:
    print("Отрицательных чисел нет")

if positive_numbers:
    avg_positive = sum(positive_numbers) / len(positive_numbers)
    print(f"Среднее арифметическое положительных чисел: {avg_positive}")
else:
    print("Положительных чисел нет")

if zeros:
    stars_list = ['*' for _ in range(len(zeros))]
    
    print(f"Количество звёзд: {len(zeros)} {stars_list}")
else:
    print("Нулей нет")
    
print("\nРаспределение чисел:")
print(f"Отрицательные: {negative_numbers}")
print(f"Положительные: {positive_numbers}")
print(f"Нули: {zeros}")