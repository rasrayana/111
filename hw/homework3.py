#1
login = input("Придумайте пароль: ")
password = input("Ваш пароль: ")
if login == password:
    print("Welcome!")
else:
    print("Password is incorrect. Please, try again")

#2
degree = int(input("Какова температура на улице?: "))
if degree <= -30:
    print("Там так холодно, лучше дома сиди!")
elif degree >= -30 and degree <= 0:
    print("Холодновато. Оденься потеплее!")
elif degree >= 0 and degree <= 15:
    print("Прохладно. Куртку накинь!")
elif degree >= 15 and degree <= 30:
    print("Тепло. Иди погуляй в парке!")
elif degree >= 30 and degree <= 50:
    print("Ого, как жарко!")
elif degree >50:
    print("Там такая жара, лучше сиди дома!")
else:
    print("Ошибка")

#3
time = int(input("Введите текущее время[0 : 23]: "))
if 0 <= time <= 6:
    print("Ночь")
elif 7 <= time <= 12:
    print("Утро")
elif 13 <= time <= 18:
    print("День")
elif 18 <= time <= 23:
    print("Вечер")
else:
    print("Ошибка")

#4
grade = int(input("Введите свою оценку: "))
if grade >= 90:
    print("Отлично")
elif 80 <= grade <= 90:
    print("Хорошо")
elif 70 <= grade <= 80:
    print("Удовлетворительно")
elif 60 <= grade <= 70:
    print("Неудовлетворительно")
elif grade< 60:
    print("Студент должен пересдать экзамен")