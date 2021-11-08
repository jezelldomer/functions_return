import math 

def info():
    _money = float(input("Enter your money: "))
    _apple = float(input("What is the cost of an apple?: "))
    total =  int(_money / _apple)
    result = (total * _apple)
    grand_total = (_money - result)
    return total, grand_total
