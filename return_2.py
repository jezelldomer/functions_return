import math

def user_price():
    _apple = int(input("How many apples you want to buy: "))
    _orange = int(input("How many oranges you want to buy: "))
    _grandtotal = obtain_totalPrice(appleF = _apple, orangeF = _orange)
    print(f"The total amount is {_grandtotal:,.2f}")

def obtain_totalPrice(appleF, orangeF):
    total = (20 * appleF) + (25 * orangeF)
    return total

user_price()