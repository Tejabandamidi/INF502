Links to code:

[code_1](https://github.com/Tejabandamidi/INF502/blob/main/Code/HW2_1.py)

[code_2](https://github.com/Tejabandamidi/INF502/blob/main/Code/HW2_2.py)

[code_3](https://github.com/Tejabandamidi/INF502/blob/main/Code/HW2_3.py)

[code_4](https://github.com/Tejabandamidi/INF502/blob/main/Code/HW2_4.py)

1.
```
1. Write a function with the following signature: pythagoreanTheorem(length_a, length_b).

The function returns the length of the hypotenuse assuming that length_a and length_b are the lengths of the two legs of a right triangle (the legs that form the triangle's right angle). Hint: the math module might have useful functions to use.
```
CODE
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

Explanation
```
To calculate the longest side (Hypotenuse) of a triangle, we use a mathematical expression with a square-root function. In out code, we imported math module and used math.sqrt to find the square-root of sum of the square of two integers which are given as input (sides of the triangle, length_a and length_b).
```
[code_1](https://github.com/Tejabandamidi/INF502/blob/main/Code/HW2_1.py)

OUTPUT1
```
EXAMPLE_1:
C:\Users\hi\PycharmProjects\INF502HW2\venv\Scripts\python.exe C:/Users/hi/PycharmProjects/INF502HW2/HW2_1.py
length_a: 4
length_b: 3
5.0

Process finished with exit code 0

EXAMPLE_2:
C:\Users\hi\PycharmProjects\INF502HW2\venv\Scripts\python.exe C:/Users/hi/PycharmProjects/INF502HW2/HW2_1.py
length_a: 5
length_b: 4
6.4031242374328485

Process finished with exit code 0

EXAMPLE_3:
C:\Users\hi\PycharmProjects\INF502HW2\venv\Scripts\python.exe C:/Users/hi/PycharmProjects/INF502HW2/HW2_1.py
length_a: 3
length_b: 3
4.242640687119285

Process finished with exit code 0

EXAMPLE_4:
C:\Users\hi\PycharmProjects\INF502HW2\venv\Scripts\python.exe C:/Users/hi/PycharmProjects/INF502HW2/HW2_1.py
length_a: 6
length_b: 8
10.0

Process finished with exit code 0

```
2.
```
2. Write a function with the following signature: list_mangler(list_in).

The function assumes that list_in is a list of integers, and returns a new list containing transformed elements of list_in. If the element is even, it's doubled. If the element is odd, it's tripled.
```
CODE
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
n=int(input("enter the length of input list:"))
#Loop for taking the input and assigning the elements
for i in range(n):
    #taking the elements into the list from the user
    b=int(input("enter elements:"))
    #appending the elements from user to the list
    list_in.append(b)
#displaying the list with doubled and tripled elements based on the condition
print(list_mangler(list_in))
```
Explanation
```
list_in is a list of integers.list_mangler is the final output list which contains integers that are doubled or tripled after checking the conditions. Here, all the elements are traversed from the input list. In this code, we checked if the integers are even or odd. When the condition is true for even integers, they are doubled and returned, else, the integers are tripled and values are returned. These elements are displayed as a list and we specified that list as list_mangler.
```
[code_2](https://github.com/Tejabandamidi/INF502/blob/main/Code/HW2_2.py)

OUTPUT2
```
EXAMPLE_1:
C:\Users\hi\PycharmProjects\INF502HW2\venv\Scripts\python.exe C:/Users/hi/PycharmProjects/INF502HW2/HW2_2.py
enter the length of input list:4
enter elements:2
enter elements:4
enter elements:3
enter elements:6
[4, 8, 9, 12]

Process finished with exit code 0

EXAMPLE_2:
C:\Users\hi\PycharmProjects\INF502HW2\venv\Scripts\python.exe C:/Users/hi/PycharmProjects/INF502HW2/HW2_2.py
enter the length of input list:5
enter elements:32
enter elements:19
enter elements:5
enter elements:2
enter elements:7
[64, 57, 15, 4, 21]

Process finished with exit code 0

EXAMPLE_3:
C:\Users\hi\PycharmProjects\INF502HW2\venv\Scripts\python.exe C:/Users/hi/PycharmProjects/INF502HW2/HW2_2.py
enter the length of input list:4
enter elements:2
enter elements:4
enter elements:6
enter elements:8
[4, 8, 12, 16]

Process finished with exit code 0

EXAMPLE_4:
C:\Users\hi\PycharmProjects\INF502HW2\venv\Scripts\python.exe C:/Users/hi/PycharmProjects/INF502HW2/HW2_2.py
enter the length of input list:5
enter elements:3
enter elements:11
enter elements:17
enter elements:15
enter elements:21
[9, 33, 51, 45, 63]

Process finished with exit code 0
```
3.
```
3. Write a function with the following signature: grade_calc(grades_in, to_drop).

The function accepts a list grades_in containing integer grades, drops the to_drop lowest grades (so, for to_drop equal to 2, the function should drop the 2 lowest grades), calculates the average of the grades left, and returns the letter grade this average corresponds to according to the letter grade scale for this course.

```
CODE
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
Explanation
```
In this code, a list of grades are taken as user input into the list grades_in. User can specify the length of the list and can give the equal number of elements. These elements are sorted using grades_in.sort() function and the least grades are dropped using to_drop which specifies the number of elements to be dropped. To delete these least grades, we used del function and specified the range from 0th element to the user desired number element specified through to_drop. After this, rest of the highest grades are used to calculate the average and corresponding letter grades are specified by checking the conditions in if, elif and else conditions. Corresponding Grades and Letter grades are displayed by the return function.
```
[code_3](https://github.com/Tejabandamidi/INF502/blob/main/Code/HW2_3.py)

OUTPUT3
```
EXAMPLE_1:
C:\Users\hi\PycharmProjects\INF502HW2\venv\Scripts\python.exe C:/Users/hi/PycharmProjects/INF502HW2/HW2_3.py
Number of grades :4
52
66
89
98
[52, 66, 89, 98]
Grades to drop : 2
[89, 98]
93.5
A

Process finished with exit code 0

EXAMPLE_2:
C:\Users\hi\PycharmProjects\INF502HW2\venv\Scripts\python.exe C:/Users/hi/PycharmProjects/INF502HW2/HW2_3.py
Number of grades :4
11
17
98
16
[11, 16, 17, 98]
Grades to drop : 2
[17, 98]
57.5
F

Process finished with exit code 0

EXAMPLE_3:
C:\Users\hi\PycharmProjects\INF502HW2\venv\Scripts\python.exe C:/Users/hi/PycharmProjects/INF502HW2/HW2_3.py
Number of grades :5
91
96
87
76
77
[76, 77, 87, 91, 96]
Grades to drop : 3
[91, 96]
93.5
A

Process finished with exit code 0

EXAMPLE_4:
C:\Users\hi\PycharmProjects\INF502HW2\venv\Scripts\python.exe C:/Users/hi/PycharmProjects/INF502HW2/HW2_3.py
Number of grades :4
85
86
79
71
[71, 79, 85, 86]
Grades to drop : 2
[85, 86]
85.5
B

Process finished with exit code 0

```
4.
```
4. Write a function with the following signature: odd_even_filter(numbers).

The function accepts an input list of integers and returns a list with two sublists. The first sublist contains all even numbers in the input list and the second sublist contains all odd numbers.
```
CODE
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
Explanation
```
A list n_list is created to store the user-specified input integers. This list is of size specified by the user and equivalent number of elements are given by the user into the list.These elements are sorted for easy traversing. After this, they are traversed to check the condition to verify if they are even or odd. All the integers which are even are appended to the even_list and the remaining integers are appended to the odd_list. These two lists are returned as nested list in one single list and returned to odd_even_filter function. 
```
[code_4](https://github.com/Tejabandamidi/INF502/blob/main/Code/HW2_4.py)

OUTPUT4
```
EXAMPLE_1:
C:\Users\hi\PycharmProjects\INF502HW2\venv\Scripts\python.exe C:/Users/hi/PycharmProjects/INF502HW2/HW2_4.py
please specify the size:4
enter the integers:
1
2
3
4
sub-lists of given list: 
[[2, 4], [1, 3]]

Process finished with exit code 0

EXAMPLE_2:
C:\Users\hi\PycharmProjects\INF502HW2\venv\Scripts\python.exe C:/Users/hi/PycharmProjects/INF502HW2/HW2_4.py
please specify the size:5
enter the integers:
2
4
6
8
10
sub-lists of given list: 
[[2, 4, 6, 8, 10], []]

Process finished with exit code 0

EXAMPLE_3:
C:\Users\hi\PycharmProjects\INF502HW2\venv\Scripts\python.exe C:/Users/hi/PycharmProjects/INF502HW2/HW2_4.py
please specify the size:5
enter the integers:
3
9
11
15
17
sub-lists of given list: 
[[], [3, 9, 11, 15, 17]]

Process finished with exit code 0

EXAMPLE_4:
C:\Users\hi\PycharmProjects\INF502HW2\venv\Scripts\python.exe C:/Users/hi/PycharmProjects/INF502HW2/HW2_4.py
please specify the size:5
enter the integers:
57
21
10
48
14
sub-lists of given list: 
[[10, 14, 48], [21, 57]]

Process finished with exit code 0

```
