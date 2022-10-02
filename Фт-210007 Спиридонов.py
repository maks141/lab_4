from Lab_2 import lab_2

employees = int(input('Введите количество сотрудников: '))

kilometers = []
for i in range(1, employees + 1):
    kilometer = int(input('Введите количество километров для {} сотрудника: '.format(i)))
    kilometers.append(kilometer)


taxi = []
for i in range(1, employees + 1):
    price = int(input('Введите цену за километр у {} такси: '.format(i)))
    taxi.append(price)

max_kilometers = sorted(kilometers, reverse=True)
min_taxi = sorted(taxi)
counter = 0
for i in kilometers:
    index_km = max_kilometers.index(i)
    num_taxi = taxi.index(min_taxi[index_km])
    counter += 1
    print('Сотрудник {} - такси №{}'.format(counter, num_taxi + 1))

data_sum = []
for i in range(len(max_kilometers)):
    summ = max_kilometers[i] * min_taxi[i]
    data_sum.append(summ)
print('Сумма', sum(data_sum))
print(lab_2(sum(data_sum)))