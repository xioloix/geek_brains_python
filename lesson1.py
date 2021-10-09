"""
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у
пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""
my_nickname = "xioloix"
my_age = 34
my_lovely_number = 3.1415

my_list = [12, 14, "twelve", "fourteen"]
my_tuple = (12, 14, "twelve", "fourteen")
my_dict = {"first_el": 12, "second_el": 14, "third_el": "twelve", "fourth_el": "fourteen"}

print(my_nickname, my_age, my_lovely_number, my_list, my_tuple, my_dict)

user_age = int(input("Введите свой возраст"))
print(f"Через 10 лет вам будет {user_age + 10}")

user_name = input("Введите вашу погремуху")
print(f"Через 5 лет тебе {user_name} будет {user_age + 5}")

"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и
секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
seconds = int(input("Введите количество секунд"))
hours = seconds // 3600
minutes = (seconds - hours * 3600) // 60
seconds = seconds - (hours * 3600) - (minutes * 60)
print(f"{hours:02}:{minutes:02}:{seconds:02}")

"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
user_number = input("Введите число от 1 до 10")
sum_number = int(user_number) + int(user_number * 2) + int(user_number * 3)
print(sum_number)

"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в
числе. Для решения используйте цикл while и арифметические операции.
"""
user_number = input("Введите число")
length_number = len(user_number)
biggest_number = 0
steps_counter = 0
while steps_counter < length_number:
    if biggest_number < int(user_number[steps_counter]):
        biggest_number = int(user_number[steps_counter])
    steps_counter += 1
print(biggest_number)

"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток
— издержки больше выручки). Выведите соответствующее сообщение. Если фирма
отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли
к выручке). Далее запросите численность сотрудников фирмы и определите прибыль
фирмы в расчете на одного сотрудника.
"""
proceeds = int(input("Введите выручку"))
costs = int(input("Введите издержки"))

profit = False
if proceeds > costs:
    profit = True
    print("Фирма отработала в прибыль")
elif proceeds == costs:
    print("Фирма отработала в ноль")
else:
    print("Фирма отработала в убыток")

if profit:
    profitability = profit / proceeds
    count_workers = int(input("Введите кол-во сотрудников"))
    print(f"Прибыль на одного сотрудника {(proceeds - costs) / count_workers}")

"""
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил
a километров. Каждый день спортсмен увеличивал результат на 10 % относительно
предыдущего. Требуется определить номер дня, на который общий результат спортсмена
составить не менее b километров. Программа должна принимать значения параметров a и b
и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.

Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""
a = int(input("Введите число a"))
b = int(input("Введите число b"))

day_counter = 1

checker = True
while checker:
    a = a + (a * 0.1)
    day_counter += 1
    if a >= b:
        checker = False

print(day_counter)
