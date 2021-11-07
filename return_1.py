
def name_age_address():
    _name = input("Enter your name: ")
    _age = int(input("Enter your age: "))
    _address = input("Enter your address: ")
    return _name, _age, _address

def display(nameG, ageG, addG): 
    print(f"Hi, my name is {nameG}, I am {ageG} years old and I live in {addG}. ")

name, age, address = name_age_address()

display (name, age, address)