import math
def add(x, y):
"""Addition"""
return x + y
def subtract(x, y):
"""Subtraction"""
return x - y
def multiply(x, y):
"""Multiplication"""
return x * y
def divide(x, y):
"""Division"""
if y == 0:
raise ValueError("Cannot divide by zero!")
return x / y

if __name__ = "__main__":
  #sample inputs
  x=4
  y=8
  
  print(add(x,y))
  print(sub(x,y))
  print(multiply(x,y)
  print(divide(x,y))

