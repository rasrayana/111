#1
for i in range(5):
    print(0)

#2
numbers = []
for nums in range(1, 101,): 
    numbers.append(nums)
print(numbers)

#3
for even in range(0, 497, 2): 
    print(even)

#4
a = list(range(1, 1001))
print(a)
min = min(a)
print(min)
max = max(a)
print(max)
sum = sum(a)
print(sum)

#5
zero = []   
for i in range(100): 
    zero.append(0)
print(zero)

#6
while True:
    age = int(input("Введите свой возраст: "))
    if age >= 18:
        print("Доступ разрешен ")
        break
    else:
        print("Извините, пользование данным ресурсом только с 18 лет ")
