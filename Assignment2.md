[code_1](https://github.com/Tejabandamidi/INF502/blob/main/Code/HW2_1.py)

[code_2](https://github.com/Tejabandamidi/INF502/blob/main/Code/HW2_2.py)

[code_3](https://github.com/Tejabandamidi/INF502/blob/main/Code/HW2_3.py)

[code_4](https://github.com/Tejabandamidi/INF502/blob/main/Code/HW2_4.py)


```
1. Write a function with the following signature: pythagoreanTheorem(length_a, length_b).

The function returns the length of the hypotenuse assuming that length_a and length_b are the lengths of the two legs of a right triangle (the legs that form the triangle's right angle). Hint: the math module might have useful functions to use.
```
CODE1
```
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

```
OUTPUT1
```
```

```
2. Write a function with the following signature: list_mangler(list_in).

The function assumes that list_in is a list of integers, and returns a new list containing transformed elements of list_in. If the element is even, it's doubled. If the element is odd, it's tripled.
```
CODE2
```
#Defining the function
def list_mangler(list_in):
    #creating an empty list
    list_mangler=[]
    #loop for traversing all the elements from the list
    for i in list_in:
        #checking the condition if the element is an even number or not
        if i % 2 == 0:
            #multiplying the element with two if the condition is true
            i *= 2
            #appending the element to the list
            list_mangler.append(i)
        else:
            #multiplying the element with three if the condition is not true
            i *= 3
            # appending the element to the list
            list_mangler.append(i)
    #returning the function
    return list_mangler
#creating an empty list for taking user input
list_in=[]
#declaring the length of the list for user input
n=int(input("enter the length:"))
#Loop for taking the input and assigning the elements
for i in range(n):
    #taking the elements into the list from the user
    b=int(input("enter elements:"))
    #appending the elements from user to the list
    list_in.append(b)
#displaying the list with doubled and tripled elements based on the condition
print(list_mangler(list_in))
```
OUTPUT2
```
```

```
3. Write a function with the following signature: grade_calc(grades_in, to_drop).

The function accepts a list grades_in containing integer grades, drops the to_drop lowest grades (so, for to_drop equal to 2, the function should drop the 2 lowest grades), calculates the average of the grades left, and returns the letter grade this average corresponds to according to the letter grade scale for this course.

```
CODE3
```
#defining the function to calculate the grades
def grade_calc(grades_in, to_drop):
    #deleting the least grades defined by the user
    del grades_in[0:to_drop]
    #displaying the remaining top grades
    print(grades_in)
    #calculating the average of the remaining grades
    average=(sum(grades_in)/len(grades_in))
    #displaying the average
    print(average)
    #checking the conditions for letter grade and returning the corresponding letter grade
    if average >= 90 and average <= 100: #if the condition is true
        return 'A' #Letter grade "A" is returned for the average
    elif average >= 80 and average < 90: #else-if the condition is true
        return 'B' #Letter grade "B" is returned for the average
    elif average >= 70 and average < 80: #else-if the condition is true
        return 'C' #Letter grade "C" is returned for the average
    elif average >= 60 and average < 70: #if none of the above conditions are true
        return 'D' #Letter grade "D" is returned for the average
    else:
        return 'F' #Letter grade "F" is returned for the average

#Defining an empty list for grades
grades_in=[]
#Specifying the length of the list
n=int(input('Number of grades :'))
#taking grades as the user-input
a=0
#loop for taking all the elements from the user
for i in range(n):
    #taking the element as input from the user
    a=int(input())
    #appending the grades to the list
    grades_in.append(a)
    #iterating for every cycle by 1
    i+=1
#sorting all the elements
grades_in.sort()
#displaying the list of grades
print(grades_in)
#specifying the number of lowest grades to be dropped
to_drop = int(input('Grades to drop : '))
#Displaying the grades and corresponding letter grade
print(grade_calc(grades_in, to_drop))
```
OUTPUT3
```
```

```
4. Write a function with the following signature: odd_even_filter(numbers).

The function accepts an input list of integers and returns a list with two sublists. The first sublist contains all even numbers in the input list and the second sublist contains all odd numbers.
```
CODE4
```
#defining the function to seperate the even and odd elements from a list
def odd_even_filter(n):
    #defining two empty lists as sub-lists for even and odd integers based on the condition
    even_list = [] #list for even integers
    odd_list = [] #list for odd integers
    #checking the condition for every element in the list to split them into even and odd and assigning them to different sub-lists
    for i in n:
        if(i % 2 == 0):#checking the condition if the integer is an even number
            # appending the value to the list of even integers when the condition is true
            even_list.append(i)
        else:#when the condition is not true
            #appending the value to the list of odd integers when the if condition is not true
            odd_list.append(i)
    #displaying the sub-lists of the given list after seperating
    print("sub-lists of given list: ")
    #Even list and Odd lists respectively
    print([even_list,odd_list])
#specifying an empty list to take the user input
n_list=[]
#specifying the length of the list
a=int(input("please specify the size:"))
#asking for the user input
print("enter the integers:")
#loop for taking all the elements from user as input
for j in range(a):
    #input elements into the list
    b=int(input(""))
    #appending the input elements to the list
    n_list.append(b)
    #sorting the elements in the list
    n_list.sort()
odd_even_filter(n_list)
```
OUTPUT4
```
```
