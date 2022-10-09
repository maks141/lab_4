from Lab_2 import lab_2

# Входные данные
while True:
    employees = int(input('Введите количество сотрудников: '))
    if employees > 0:
        break
    else:
        print('Ввод должен содержать числа, большие чем 0')

# Входные данные
kilometers = []
for i in range(1, employees + 1):
    while True:
        kilometer = int(input('Введите количество километров для {} сотрудника: '.format(i)))
        if kilometer > 0:
            break
        else:
            print('Ввод должен содержать числа, большие чем 0')
    kilometers.append(kilometer)

# Входные данные
taxi = []
for i in range(1, employees + 1):
    while True:
        price = int(input('Введите цену за километр у {} такси: '.format(i)))
        if price > 0:
            break
        else:
            print('Ввод должен содержать числа, большие чем 0')
    taxi.append(price)

# Cортировка списков
max_kilometers = sorted(kilometers, reverse=True)
min_taxi = sorted(taxi)

# Выбор такси для сотрудника
counter = 0
for i in kilometers:
    index_km = max_kilometers.index(i)
    num_taxi = taxi.index(min_taxi[index_km])
    counter += 1
    print('Сотрудник {} - такси №{}'.format(counter, num_taxi + 1))

# Конечная сумма
data_sum = []
for i in range(len(max_kilometers)):
    summ = max_kilometers[i] * min_taxi[i]
    data_sum.append(summ)
print('Сумма', sum(data_sum))
print(lab_2(sum(data_sum)))