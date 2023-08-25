def murat():
    print("Geeks")
murat()

#set, frozenset
#Типы данных - int, str, float, bool, list, tuple, set, frozenset
# nums1 = [1, 2, 3, 4, 5]
# nums2 = [3, 4, 5, 6, 7]
# nums3 = nums1 + nums2
# print(set(nums3))

# names = {'Nurbolot', 'Kurmanbek', 'Murat', 'Bayastan', 'Nurbolot'}
# print(names)

# numbers = {10, 20, 30, 30, 30, 30, 40, 50, 60, 70, 70}
# print(numbers)

# cars = {'BMW', 'Tesla', 'Mercedes'}
# print(cars)
# cars.add('Honda')
# print(cars)
# cars.add('BMW')
# print(cars)
# cars.remove('Tesla')
# print(cars)
# cars.pop()
# print(cars)

# st = {1, 1.0, True, "1"}
# print(st)

#Frozenset
# frzn = frozenset({1, 2, 3, 3, 3, 4, 5, 5, 6})
# print(frzn)
# frzn.remove(1)
# print(frzn)

#Dictionary - словари
student = {'name':'Askhat', 'age':20}
print(student)
print(student['name'])
print(student['age'])
student.setdefault('language', 'Python') #Метод setdefault, добавляет в
                                        #словарь ключ и значение
print(student)
student.pop('age') #Метод pop, удаляет ключ из словаря и за одно значение
print(student)
student['language'] = 'JavaScript' #Таким образом можно обновлять значения
                                #в словарях Python
print(student)

tesla_modex_x = {'brand':'Tesla', 'model':'Model X', 'year':2023, 'color':'white'}
print(tesla_modex_x)
print(tesla_modex_x.keys()) #Метод keys() возвращает специальную коллекцию ключей в словаре
print(tesla_modex_x.values()) #Метод values() возвращает специальную коллекцию значений в словаре
print(tesla_modex_x.items()) #Метод items() возвращает пары «ключ — значение» в формате кортежей

for key, value in tesla_modex_x.items():
    print(key, value)

contact = {'MCHS':'112'}
while True:
    command = input("1 - посмотреть, 2 - добавить, 3 - удалить, 4 - обновить: ")
    if command == "1":
        print(contact)
    elif command == "2":
        add_name = input("Имя: ")
        if add_name in contact.keys():
            print("Такой контакт уже существует")
        else:
            add_number = input("Номер: ")
            contact.setdefault(add_name, add_number)
            print("Контакт", add_name, "успешно добавлен")
    elif command == "3":
        delete_name = input("Кого удалить: ")
        contact.pop(delete_name)
        print(delete_name, "успешно удален")
    elif command == "4":
        update_name = input("Кого обновить: ")
        new_number = input("Новый номер: ")
        contact[update_name] = new_number
        print("Контакт", update_name, "успешно обновлен")
    else:
        print("Такой комманды нету")