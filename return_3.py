import math 

def info():
    _money = float(input("\033[0;35;40m \n Enter your money: "))
    _apple = float(input("\033[0;36;40m \n What is the cost of an apple?: "))
    total =  int(_money / _apple)
    result = (total * _apple)
    grand_total = (_money - result)
    return total, grand_total

def display(totalG, grand_totalG):   
    print (f"\033[1;32;40m \n You can buy \033[1;34;40m{totalG} \033[1;33;40mapples and your change is \033[1;37;40m{grand_totalG:,.2f} ")

#Added Python Color Class

total, grand_total = info()

display (total, grand_total)
