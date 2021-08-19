winter=[1,2,12]
spring=[3,4,5]
summer=[6,7,8]
autumn=[9,10,11]
season={'Зима': winter,
        'Весна': spring,
        'Лето': summer,
        'Осень': autumn}
month=int(input('Введите номер месяца '))
for key in season.keys():
    if month in season [key]:
        print(key)