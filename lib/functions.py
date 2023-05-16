# !/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

# greet_programmer()

def greet(name):
    print(f"Hello, {name}!")

# greet("Guido")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

# greet_with_default("Guido")

def add(num1, num2):
    return num1 + num2

# add(45, 55)

def halve(number):
    pass
    if isinstance(number, (int, float)):
        return number / 2
    else:
        return None
    
# halve(100)