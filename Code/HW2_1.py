#Importing the math module to use squareroot function
import math
#defining the function by passing two arguments as sides of a triangle
def pythagoreanTheorem(length_a, length_b):
    #using the square-root function from math module by passing the arguments
    #returning the values
    return math.sqrt(length_a**2+length_b**2)
#assigning the values from user input
length_a=int(input())
length_b=int(input())
#displaying the output
print(pythagoreanTheorem(length_a,length_b))
