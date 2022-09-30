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