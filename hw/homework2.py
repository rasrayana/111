#1
word = input("Введите слово: ")
print(word [::-1])


#2
word = input("Введите любое слово: ")
print(word [0])
print(word [-1])
print(word [0:-1])


#3 
name = """Advertising companies say advertising is necessary and important. It informs people about
new products. Advertising hoardings in the street make our environment colourful. And
adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next
programme in the mini-drama. Advertising can educate, too. Adverts tell us about new,
healthy products. And adverts in magazines give us ideas for how to look prettier, be
fashionable and be successful. Without advertising, life is boring and colourless.
But some consumers argue that advertising is a bad thing. They say that advertising is bad
for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers
know we love our children and want to give them everything. So they use children’s ‘pester
power’ to sell their products. Finally, consumers say, if there is advertising there must be
rules. Some adverts advertise unhealthy things like cigarettes and make people waste their
money"""
print(name.count('t'))
print(name.count('s'))


#4
str_1 = "Aidana"
str_2 = "Adilet"
print(str_1[::1] + str_2[::1])  

