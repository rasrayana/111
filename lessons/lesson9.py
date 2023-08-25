# def div(num1: int, num2:int):
#     print(num1 + num2)
# div(69, 23)

# def add(nim1: int= 10, num2: int= 15):
#     print(nim1 + num2)
# add(20)
# def mult(num1: int= 5, num2: int = 5) -> int:
#     print(num1 * num2)
# mult()

def welcome(name: str = "Rayana") -> str:
    return "welcome " + name
print(welcome( "Jakshylyk"))
print(welcome())

def calculator(num1:int = 1, num2: int = 3,operator:str = "+")  ->int:
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Такого оператора нет"
print(calculator(30, 39, "-"))

calculator()