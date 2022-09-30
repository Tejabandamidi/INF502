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