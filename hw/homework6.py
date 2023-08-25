#1
# def userstext():
#     while True:
#         userstext = (input("Введите что хотите : "))
#         if userstext.find("?")>=0:
#             print("Конечно!")
#         elif userstext.find("!")>=0:
#             print("Успокойся")
#         elif userstext == "":
#             print("Как классно, когда ты молчишь. Продолжай в том же духе")
#         else:
#             print("ну и что")

# userstext()

#2
# def text():
#     text = "money, money, money, it’s always sunny, in the rich men’s world"
#     print(text.count("money"), "money")
#     print(text.count("it’s"), "it’s")
#     print(text.count("always"), "always")
#     print(text.count("sunny"), "sunny")
#     print(text.count("in"), "in" )
#     print(text.count("the"), "the")
#     print(text.count("rich"), "rich")
#     print(text.count("men’s"), "men’s")
#     print(text.count("world"), "world")

# text()

# #3
# def nums():
#     n = int(input("Введите число: "))
#     rev_n = int(str(n)[::-1])
#     print(n + rev_n)

# nums()

#Доп. задания
#1
# set_1 = {111, 333, 555, 777, 999}
# set_2 = {222, 444, 666, 888}
# print(set_1.union(set_2))

# #2
# fruits = {"pineapple", "apple", "orange", "peach", "pear", "dragon fruit"}
# if "apple" in fruits:
#     print("There is an apple in set fruits")
# else:
#     print("There is not an apple in set fruits")

# #3
# even_numbers = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
# divisible_by_three = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
# set = even_numbers.intersection(divisible_by_three)
# print(set)