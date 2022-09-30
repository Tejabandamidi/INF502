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