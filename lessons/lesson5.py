#for and while
# for number in range(1001):
#     print(number)

# for i in range(67, 99, 2):    #в циклах с использованием функции range можно указывать начало конец и шаг
#     print(i) #выводим врем переменную num

# numbers = [] #создаем пустой список numbers
# for i in range(1, 100, 2): 
#     numbers.append(i)
# print(numbers)

# names = ["Nurbolot", "Bayastan", "Syimyk", "Beksultan", "Janysh"]
# for name in names:
#     print("Hello!", name)

# nums = [198, 289, 15, 56, 69, 90, 178, 8765]
# for num in nums:
#     if num % 2 == 0:
#         print(num, "число четное")
#     else:
#         print(num, "число нечетное")

#while
# num_1 = 10
# num_2 = 20
# while num_2 > num_1:
#     num_1 += 1
#     #num_1 = num_1 + 1
#     print(num_1)

n = 0
while True:
    n += 1
    print(n, "Hello geeks") #прикол
    if n == 10000:
        print("STOP")
        break #или continue(по настроению b
