#defining the wallet function
def wallets():
    #user input is given for taking the number of wallets to be given by the user
    wallet_count = int(input("please provide numbers representing the value in cash for different wallets: "))
    #count is the variable that stores the input number given by the user which specifies the number of wallets to be used
    count=wallet_count
    #wallet is the list to store the values given by the user as cash
    wallet=[]
    #for loop for taking the input integers as cash by iterating until the length of count
    for i in range(count):
        #cash is the input element stored into the list named wallet
        Cash=int(input(" "))
        #appending the cash input into the wallet list
        wallet.append(Cash)
    # printing the list wallet with the values given
    print(wallet)
    #high_amount is the variable used to store the highest value, max is used for finding the highest value in the list.
    high_amount=max(wallet)
    #low_amount is the variable used to store the least value, min is used to find the least value in the list.
    low_amount=min(wallet)
    #total is the sum of the whole values in the list, sum is used to calculate the summation of the values within the list.
    total=sum(wallet)
    #dime is the variable used here for storing the ten times the total amount obtained. Since 1 Dollar=10 dimes, we multiply the sum with 10.
    dime=total*10
    #returns the values
    return high_amount, low_amount, total, dime

#Printing the values as per needed
high_amount, low_amount, total, dime = wallets()
#displaying the amount present in the fattest wallet.
#Here the huge amount is present so the wallet is fattest, therefore, we assume this has max amount from the list
print("The fattest wallet has $",high_amount ,"in it.")
#displaying the amount present in the skinniest wallet.
#Here the least amount is present so the wallet is skinniest, therefore, we assume this has min amount from the list
print("The skinniest wallet has $",low_amount,"in it")
#displaying the whole amount present in the list named wallet
#we used sum to calculate the total of the list
print("All together, these wallets have $",total ,"in them.")
#displaying the whole sum amount in terms of dimes. we multiply the total value with 10 to obtain the whole value in dimes.
print("All together, the total value of these wallets is worth", dime," dimes")


