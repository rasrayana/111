#Условия if, else, elif
# num1 = 20
# num2 = 100
# if num1 > num2:
#     print("Переменная num1 больше num2")
# else:
#     print("Переменная num2 больше num1")

# number_1 = int(input("Первое число: "))
# number_2 = int(input("Второе число: "))
# if number_1 > number_2:
#     print("Первое число больше")
# elif number_1 < number_2:
#     print("Второе число больше")
# else:
#     print("Они равны")

# num1 = int(input("Введите первое число: "))
# operator = input("+, -, *, /: ")
# num2 = int(input("Введите второе число: "))
# if operator == "+":
#     print("Ответ:", num1 + num2)
# elif operator == "-":
#     print("Ответ:", num1 - num2)
# elif operator == "*":
#     print("Ответ:", num1 * num2)
# elif operator == "/":
#     print("Ответ:", num1 / num2)
# else:
#     print("Такого оператора не существует")

# number = int(input("Введите число: "))
# if number % 2 == 0:
#     print(number, "четный")
# else:
#     print(number, "нечетный")

#Логические операторы
# login = input("Login: ")
# password = input("Password: ")
# if login == "geeks" and password == "geeksstudents":
#     print("Welcome")
# else:
#     print("Error")

name = input("Имя: ")
age = int(input("Возраст: "))
if age < 18:
    print(name, "вы несовершеннолетний")
elif age >= 18 and age <= 28:
    print(name, "годен к службе!")
else:
    print(name, "вы уже не годны для службы")

# num1 = 10
# num2 = 20
# num3 = 30
# if num1 > num2 and num1 > num3:
#     print("Первое число больше")
# elif num2 > num1 and num2 > num3:
#     print("Второе число больше")
# elif num3 > num1 and num3 > num2:
#     print("Третье число больше")
# else:
#     print("Числа равны")

# name = "aziza"
# if name == name[::-1]:
#     print(True)
# else:
#     print(False)

#Операторы сравнения
# print(20 == 20)
# print(12 == 13)

# print(5 != 4)
# print(200 != 200)

# print(5 > 2)
# print(5 > 50)

# print(30 < 100)
# print(5 < 1)

# print(10 >= 10)
# print(10 >= 100)

# print(5 <= 5)
# print(10 <= 3)