import math

def user_price():
    _apple = int(input("\033[0;35;40m \n How many apples you want to buy:  "))
    _orange = int(input("\033[0;36;40m \n How many oranges you want to buy:  "))
    _grandtotal = obtain_totalPrice(appleF = _apple, orangeF = _orange)
    print(f"\033[1;32;40m \n The total amount is \033[5;33;40m {_grandtotal:,.2f} ")

#Added Python Color Class

def obtain_totalPrice(appleF, orangeF):
    total = (20 * appleF) + (25 * orangeF)
    return total

user_price()