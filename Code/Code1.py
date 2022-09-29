#Importing the math module to use squareroot function
import math
#defining the function by passing two arguments as sides of a triangle
def pythagoreanTheorem(length_a, length_b):
    return math.sqrt(length_a**2+length_b**2)
length_a=int(input())
length_b=int(input())
print(pythagoreanTheorem(length_a,length_b))