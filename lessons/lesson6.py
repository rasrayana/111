#Функции
def plus(num1, num2):
    print(num1+num2)

def minus(num1, num2):
    print(num1-num2)

def multiply(num1, num2):
    print(num1 * num2)

def division(num1, num2):
    print(num1 / num2)

def user(num1, num2, choise):
    if choise == "1":
        plus(num1, num2)
    elif choise == "2":
        minus(num1, num2)
    elif choise == "3":
        multiply(num1, num2)
    elif choise == "4":
        division(num1, num2)
numm1 = int(input("Введите первое число: "))
numm2 = int(input("Введите второе число: "))
choise = input("Введите ваш выбор > 1 - сложение,  > 2 - вычитание, > 3 - умножение, > 4 - деление: ")
user(numm1, numm2, choise)


def dog():
    print("Bark-bark")

def cat():
    print("Meow-meow")

def cow():
    print("Mooo-mooo")

def elephant():
    print("Trumpet-trumpet")

def bird():
    print("Chirp-chirp")

def frog():
    print("Croak-croak")

def lion():
    print("Roarrr")

def user(choise):
    if choise == "dog":
        print("Bark-bark")
    elif choise == "cat":
        print("Meow-meow")
    elif choise == "cow":
        print("Mooo-mooo")
    elif choise == "elephant":
        print("Trumpet-trumpet")
    elif choise == "bird":
        print("Chirp-chirp")
    elif choise == "frog":
        print("Croak-croak")
    elif choise == "lion":
        print("Roarrrr")
choise = (input("Введите животное: "))
user(choise)


#set/ frozenset
hsa = {1,2,3,4,5,6,7,7}
hsa.add(8)
print(hsa)

bruh = {666, 777, 888, 999, 111}
print(bruh)

blin = frozenset([1, 2, 2, 3, 4, 5, 6, 7, 7, 8])
print(blin)

def animals():
    printt = {"cat", "dog", "cow"}
    print(printt)
    printt.add("bird")
    print(printt)
    printt.remove("cow")
    print(printt)

animals()