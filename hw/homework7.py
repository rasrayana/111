#1
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
dictionary_1.update(dictionary_2)
print(dictionary_1)

#2
numbers = {'num_1' : 1, 'num_2' : 2, 'num_3' : 3, 'num_100' : 100}
for key in numbers:
     numbers[key] *= 5
print(numbers)
#3
student = {'name' : 'Askhat', 'age' : 17}
print(student['age'] * 2)
#4
student = {'name' : 'Askhat', 'age' : 17, 'color' : 'White'}
student['age'] = 16
print(student['age'])
print(student)
#5
student = {'name' : 'Askhat', 'age' : 17}
del student['age']
print(student)
#6
student = {'name' : 'Askhat'}
student.setdefault ('adress' , 'West Anar')
print(student)

#
password = {}
password1= input("password 1:")
password2= input("password2:")
password.setdefault(password1)
if len(password1)<8:
    print("Your password is too short, please try again")
elif "123" in password1:
    print("Your password is too easy, please try again")
elif password1 != password2:
    print("The password is incorrect")
else:
    print("Your password has been successfully created")
