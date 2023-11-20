def add(a, b):
    return a + b

def substraction(a, b):
    return a - b

def mult(a, b):
    return a * b

def division(a, b):
    try:
        return (a / b)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
def square_root(a):
    return a**0.5
