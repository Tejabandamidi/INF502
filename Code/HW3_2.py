class Element:
    #defining the constructor and self to represent the attributes and methods with symbol, name, atomic number, row and column
    def __init__(self,symbol,name,atomic_number,row,column):
        self.symbol = symbol
        self.name = name
        self.atomic_number = atomic_number
        self.row = row
        self.column = column
#defining the list with symbol corresponding to the element with associated atomic number, row number and the column number respectively.
symbol_list = [Element('H','Hydrogen',1,1,1),Element('HE','Helium',2,1,18),Element('LI','Lithium',3,2,1),Element('BE','Beryllium',4,2,2),
                    Element('B','Boron',5,2,13),Element('C','Carbon',6,2,14),Element('N','Nitrogen',7,2,15),Element('O','Oxygen',8,2,16),
                    Element('F','Flourine',9,2,17),Element('NE','Neon',10,2,18),Element('NA','Sodium',11,3,1),Element('MA','Magnesium',12,3,2),
                    Element('AL','Aluminium',13,3,13),Element('SI','Silicon',14,3,14),Element('P','Phosphorus',15,3,15),Element('S','Sulfur',16,3,16),
                    Element('CL','Chlorine',17,3,17),Element('AR','Argon',18,3,18),Element('K','Potassium',19,4,1),Element('CA','Calcium',20,4,2),
                    Element('SC','Scandium',21,4,3),Element('TI','Titanium',22,4,4),Element('V','Vanadium',23,4,5),Element('CR','Chromium',24,4,6),
                    Element('MN','Manganese',25,4,7),Element('FE','Iron',26,4,8),Element('CO','Cobalt',27,4,9),Element('NI','Nickel',28,10,10),
                    Element('CU','Copper',29,4,11),Element('ZN','Zinc',30,4,12),Element('GA','Gallium',31,4,13),Element('GE','Germanium',32,4,14),
                    Element('AS','Arsenic',33,4,15),Element('SE','Selenium',34,4,16),Element('BR','Bromine',35,4,17),Element('KR','Krypton',36,4,18),
                    Element('RB','Rubidium',37,5,1),Element('SR','Strontium',38,5,2),Element('Y','Yttrium',39,5,3),Element('ZR','Zirconium',40,5,4),
                    Element('NB','Niobium',41,5,5),Element('MO','Molybdenum',42,5,6),Element('TC','Technetium',43,5,7),Element('RU','Ruthenium',44,5,8),
                    Element('RH','Rhodium',45,5,9),Element('PD','Palladium',46,5,10),Element('AG','Silver',47,5,11),Element('CD','Cadmium',48,5,12),
                    Element('IN','Indium',49,5,13),Element('SN','Tin',50,5,14),Element('SB','Antimony',51,5,15),Element('TE','Tellurium',52,5,16),
                    Element('I','Iodine',53,5,17),Element('XE','Xenon',54,5,18),Element('CS','Caesium',55,6,1),Element('BA','Barium',56,6,2),
                    Element('LA','Lanthanium',57,6,3),Element('CE','Cerium',58,6,3),Element('PR','Praseodymium',59,6,3),Element('ND','Neodymium',60,6,3),
                    Element('PM','Promethium',62,6,3),Element('SM','Samarium',62,6,3),Element('EU','Europium',63,6,3),Element('GD','Gadolinium',64,6,3),
                    Element('TB','Terbium',65,6,3),Element('DY','Dysprosium',66,6,3),Element('HO','Holmium',67,6,3),Element('ER','Erbium',68,6,3),
                    Element('TM','Thulium',69,6,3),Element('YB','Ytterbium',70,6,3),Element('LU','Lutetium',71,6,3),Element('HF','Hafnium',72,6,4),
                    Element('TA','Tantalum',73,6,5),Element('W','Tungsten',74,6,6),Element('RE','Rhenium',75,6,7),Element('OS','Osmium',76,6,8),
                    Element('IR','Iridium',77,6,9),Element('PT','Platinum',78,6,10),Element('AU','Gold',79,6,11),Element('HG','Mercury',80,6,12),
                    Element('TL','Thallium',81,6,13),Element('PB','Lead',82,6,14),Element('BI','Bismuth',83,6,15),Element('PO','Polonium',84,6,16),
                    Element('AT','Astatine',85,6,17),Element('RN','Radon',86,6,18),Element('FR','Francium',87,7,1),Element('RA','Cadmium',88,7,2),
                    Element('AC','Actinium',89,7,3),Element('TH','Thorium',90,7,3),Element('PA','Protactinium',91,7,3),Element('U','Uranium',92,7,3),
                    Element('NP','Neptunium',93,7,3),Element('PU','Plutonium',94,7,3),Element('AM','Americium',95,7,3),Element('CM','Curium',96,7,3),
                    Element('BK','Berkelium',97,7,3),Element('CF','Californium',98,7,3),Element('ES','Einsteinium',99,7,3),Element('FM','Fermium',100,7,3),
                    Element('MD','Mendelevium',101,7,3),Element('NO','Nobelium',102,7,3),Element('LR','Lawrencium',103,7,3),Element('RF','Rutherfordium',104,7,4),
                    Element('DB','Dubnium',105,7,5),Element('SG','Seaborgium',106,7,6),Element('BH','Bohrium',107,7,7),Element('HS','Hassium',108,7,8),
                    Element('MT','Meitnerium',109,7,9),Element('DS','Darmstadtium',110,7,10),Element('RG','Roentgenium',111,7,11),Element('CN','Copernicium',112,7,12),
                    Element('NH','Nihonium',113,7,13),Element('FL','Flerovium',114,7,14),Element('MC','Moscovium',115,7,15),Element('LV','Livermorium',116,7,16),
                    Element('TS','Tennessine',117,7,17),Element('OG','Oganesson',118,7,18)]
#assigning the list to the dictionary and creating symbol_dict as dictionary
symbol_dict = {element.symbol: element for element in symbol_list}



#defining the function for the symbol
def option1(symbol):
    #displaying the information of an element.
    print("{} stands for the element {}.\nAtomic number {}.\nRow {} \nColumn {}.".format(symbol,symbol_dict[symbol].name,symbol_dict[symbol].atomic_number,symbol_dict[symbol].row,symbol_dict[symbol].column))
    print("\n")


#defining the function for properties


def option2(property):
    #specifing the conditions to choose to display the name, atomic number, row or column
    if property == 0:
        for symbol in symbol_dict:
            print("{} Stands for {}".format(symbol,symbol_dict[symbol].name))
    elif property == 1:
        for symbol in symbol_dict:
            print("Atomic Number for {} is {}".format(symbol, symbol_dict[symbol].atomic_number))
    elif property == 2:
        for symbol in symbol_dict:
            print("Row of element {} is {}".format(symbol, symbol_dict[symbol].row))
    elif property == 3:
        for symbol in symbol_dict:
            print("Column of element {} is {}".format(symbol, symbol_dict[symbol].column))
    print("\n")


#defining the function for taking the input from the user to add the new element with respective properties
def option3():
    global symbol_list
    global symbol_dict
    #taking user input to define the symbol for the new element
    symbol = str(input("Enter the symbol for new element: ")).upper()
    # taking user input to define the name for the new element
    name = str(input("Enter the name of "+symbol+": "))
    # taking user input to define the atomic number for the new element
    atomic_number = str(input("Enter the Atomic number of "+symbol+": "))
    # taking user input to define the row of the new element
    row = str(input("Specify the Row of "+symbol+": "))
    # taking user input to define the Column of the new element
    column = str(input("Specify the Column of "+symbol+": "))
    #Appending the properties
    symbol_list.append(Element(symbol, name, atomic_number, row, column))
    symbol_dict = {element.symbol: element for element in symbol_list}
    #Displaying the added element properties
    print(symbol+" Added as a new element")
    print("{} stands for the element {}.\nAtomic number is {}.\nRow {} \nColumn {}.".format(symbol,symbol_dict[symbol].name,symbol_dict[symbol].atomic_number,symbol_dict[symbol].row,symbol_dict[symbol].column))
    print("\n")


#Defining the function for modifying the attributes of the existing element

def option4():
    global symbol_dict
    symbol = "Invalid"
    while symbol == "Invalid":
        try:
            symbol = str(input("Specify the symbol of corresponding element to change: ")).upper()
            name = symbol_dict[symbol].name
        except KeyError:
            print("Symbol not found, Enter a valid symbol")
            symbol = "Error"
    name = str(input("Enter the new name for"+symbol+": "))
    atomic_number = str(input("Update the atomic number for" + symbol + ": "))
    row = str(input("Update the Row for" + symbol + ": "))
    column = str(input("Update the column for " + symbol + ": "))
    symbol_dict[symbol] = Element(symbol, name, atomic_number, row, column)
    print(symbol+ "changes made are successful")
    print("{} Stands for the element {} \nAtomic number is {}.\nRow {}\nCcolumn {}.".format(symbol,symbol_dict[symbol].name,symbol_dict[symbol].atomic_number,symbol_dict[symbol].row,symbol_dict[symbol].column))
    print("\n")




menu_choice = 0
while menu_choice != 5:
    print('Please Choose any option')
    print("1. Display the information about the element, by entering that element's symbol.")
    print("2. Choose a property, and see that property for each element.")
    print("3. Enter the new element.")
    print("4. Change the attributes, by entering the element's symbol.")
    print("5. Exit the program.")
    try:
        menu_choice = int(input("Your input: "))
    except ValueError:
        print("This is an invalid choice!")
    while menu_choice < 1 or menu_choice > 5:
        try:
            menu_choice = input("Please enter a valid choice: ")
            menu_choice = int(menu_choice)
        except (ValueError, TypeError):
            print("This is an invalid choice")
            menu_choice = 0
    if menu_choice == 1:
        symbol = "Invalid"
        while symbol == "Invalid choice":
            try:
                symbol = str(input("Specify the symbol of the element to see the information about (not case sensitive): "))
                symbol = symbol.upper()
                option1(symbol)
            except KeyError:
                print("Symbol not found, please enter a valid symbol")
                symbol = "Invalid choice"
    elif menu_choice == 2:
        property = -1
        while property > 3 or property < 0:
            try:
                print("0. Name")
                print("1. Atomic Number")
                print("2. Row")
                print("3. Column")
                property = int(input("Choose the number from following: "))
            except ValueError:
                print("Invalid choice,choose between 0 to 3: ")
                property = -1
        option2(property)
    elif menu_choice == 3:
        option3()
    elif menu_choice == 4:
        option4()
