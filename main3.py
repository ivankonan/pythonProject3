import random
n = int(input('Введите количество элементов')) # задаем размер списка
A=[] # создаем пустой список

for i in range(n):
    A.append(random.randint(0,99))

print("Минимальный значение списка " + str(min(A)))

print("Элементы списка")
print(A)

