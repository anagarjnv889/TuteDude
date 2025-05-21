# Task 1: Calculate Factorial Using a Function 
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
n=int(input("Enter a number: "))
print("Factorial of",n,"is:",factorial(n))

# Task 2: Using the Math Module for Calculations
import math
a=int(input("Enter a number: "))
print("Square root :",math.sqrt(a))
print("Logarithm:",math.log(a))
print("Sine:",math.sin(a))