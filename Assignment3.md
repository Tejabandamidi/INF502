LINKS TO CODE:

[Code_1](https://github.com/Tejabandamidi/INF502/blob/main/Code/HW3_1.py)

[Code_2](https://github.com/Tejabandamidi/INF502/blob/main/Code/HW3_2.py)

```
1.
Problem 1: Wallets

Write a Python program that request a user to provide numbers representing the value in cash for different wallets. Your program should store these values in a list. The user should be able to add as many values as they want. One example of a filled `wallets` list (in this example, with 5 wallets) would be:

```
print(wallets)

Output: [1023, 984, 192, 1842, 12]
```

After the user adds the values for the wallets, your application should provide the following information:
* The fattest wallet has `$value` in it.
* The skinniest wallet has `$value` in it.
* All together, these wallets have `$value` in them.
* All together, the total value of these wallets is worth `$value` dimes.

Please try to think about different functions to complete your work.
```
SOLUTION:
```

EXPLANATION:
We declare an empty list wallet, define a function wallets in which the length of the list is taken as wallet_count from the user. It is assigned to the variable count which acts as the length of wallet. Then we use for loop for assigning the elements into the list by taking the user input as "Cash" variable.Then the list is displayed. Later, the maximum value, minimum value, sum and the dime value i.e, dime is 10 times sum are calculated. Then, the fattest wallet value, skinniest wallet value, total whole value and total value in dimes is displayed.
```

CODE:
Code is given below, please click on the link
[Code_1](https://github.com/Tejabandamidi/INF502/blob/main/Code/HW3_1.py)


```
OUTPUTS:

please provide numbers representing the value in cash for different wallets: 4
 150
 2005
 168
 12
[150, 2005, 168, 12]
The fattest wallet has $ 2005 in it.
The skinniest wallet has $ 12 in it
All together, these wallets have $ 2335 in them.
All together, the total value of these wallets is worth 23350  dimes

Process finished with exit code 0
```


```
Problem 2: Periodic Table 

The Periodic Table of the Elements was developed to organize information about the elements that make up the Universe.
Write a terminal application that lets you enter information about each element in the periodic table.
Make sure you include the following information:
* symbol, name, atomic number, row, and column

You must save the elements in a dictionary where the `symbol` is the key and the other attributes are nested inside `symbol`. The nested keys are `name`, `number`, `row`, `column`.

To populate your dictionary with data, provide a menu of options to the users:

1. Search the element by symbol (see all the details).
2. Search by a property (`name`, `number`, `row`, `column`) and see the values for that property for all the elements in the table.
3. Enter a new element manually (type the information for each property)
4. Change the properties of an element (by symbol)
5. Export periodic table as a JSON file
6. Load periodic table from JSON file
7. Exit the program

Make sure you do the appropriate communication with the user to get the necessary information to complete each step.
```
```
EXPLANATION:
We take the input as the list and then convert it into the dictionary. We use constructs and then we use self to initialize the attributes and methods associated. We define different functions for different operations and we call the functions for adding new elements, seeing the already existing elements information by specifying the user defined inputs.


```

CODE:
Code is given below, please click on the link
[Code_2](https://github.com/Tejabandamidi/INF502/blob/main/Code/HW3_2.py)

```
OUTPUT:

For Option 1



Please Choose any option
1. Display the information about the element, by entering that element's symbol.
2. Choose a property, and see that property for each element.
3. Enter the new element.
4. Change the attributes, by entering the element's symbol.
5. Exit the program.
Your input: 1
Please enter the symbol of the element you want to see the information about (not case sensitive): He
HE stands for the element Helium.
Atomic number 2.
Row 1 
Column 18.


For option 2
Output is 

Please Choose any option
1. Display the information about the element, by entering that element's symbol.
2. Choose a property, and see that property for each element.
3. Enter the new element.
4. Change the attributes, by entering the element's symbol.
5. Exit the program.
Your input: 2
0. Name
1. Atomic Number
2. Row
3. Column
Choose the number from following: 0
H Stands for Hydrogen
HE Stands for Helium
LI Stands for Lithium
BE Stands for Beryllium
B Stands for Boron
C Stands for Carbon
N Stands for Nitrogen
O Stands for Oxygen
F Stands for Flourine
NE Stands for Neon
NA Stands for Sodium
MA Stands for Magnesium

```


