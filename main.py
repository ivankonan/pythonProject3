# создаем списки времен года
winter=[1,2,12]
spring=[3,4,5]
summer=[6,7,8]
autumn=[9,10,11]
# создаем массив списков
season={'Зима': winter,
        'Весна': spring,
        'Лето': summer,
        'Осень': autumn}
month=int(input('Введите номер месяца ')) # вводим номер месяца
for key in season.keys(): # цикл по массиву времен года
    if month in season [key]: # проверка наличия номера месяце в списке сезона
        print(key) # вывод результата