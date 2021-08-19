n=int(input('Введите количество лет ')) # колличество лет
price=[] # создание пустого списка цен
for i in range(n) : # цикл ввода стоимости оборудования
    price.append(int(input('Введите сумму ' + str(i+1) + ' года '))) # ввод элементов по годам

percent = int(input('Введите процент износа ')) # процент износа оборудования
sum_price = sum(price)
print(sum_price-sum_price*(percent/100))

