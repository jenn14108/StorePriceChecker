"""
C-store App

This Python program lets C-store customers check the price of an item,
calculate the total price of a shopping cart, check items eligible for a meal
and check the discount with a given date.

"""

discount = [
    {'date':'0101', 'name': 'New Years Day','discount': 0.75},
    {'date':'0116','name': 'Martin Luther King, Jr. Day', 'discount': 0.80},
    {'date':'0220','name': 'Geroge Washington Birthday','discount': 0.85},
    {'date':'0529','name': 'Memorial Day','discount': 0.85},
    {'date':'0704','name': 'Independence Day','discount':0.60},
    {'date':'0904','name': 'Labor Day','discount': 0.85},
    {'date':'1009','name': 'Columbus Day','discount': 0.90},
    {'date':'1110','name': 'Veterans Day','discount': 0.85},
    {'date':'1123','name': 'Thanksgiving Day','discount': 0.65},
    {'date':'1225','name': 'Christmas Day','discount': 0.60}]

all_items = [
    {'item':'family size doritos', 'price': 2.89},
    {'item':'TGIF potato skin', 'price': 2.29},
    {'item':'bugels', 'price': 1.89},
    {'item':'small lays chips', 'price': 0.99},
    {'item':'cheez it', 'price': 3.29},
    {'item':'chex mix', 'price': 1.59},
    {'item':'pringles', 'price': 2.89},
    {'item':'chefs cut jerky', 'price': 6.39},
    {'item':'krave jerky', 'price': 6.39},
    {'item':'lorisa kitchen jerky', 'price': 7.39},
    {'item':'milano cookies', 'price': 3.69},
    {'item':'pepperidge farm pirouette', 'price': 6.49},
    {'item':'pepperidge farm cookies (box)', 'price': 6.99},
    {'item':'goldfish crackers (bag) ', 'price': 2.49},
    {'item':'goldfish crackers (box)', 'price': 9.99},
    {'item':'combox pretzels', 'price': 2.99},
    {'item':'hipz pretzel', 'price': 2.99},
    {'item':'trumoo milk (14 fl oz)', 'price': 1.69},
    {'item':'simply orange juice', 'price': 2.99},
    {'item':'odwalla', 'price': 3.49},
    {'item':'yup', 'price': 2.09},
    {'item':'dasani water (10.1 fl oz)', 'price': 0.99},
    {'item':'dasani water (20 fl oz)', 'price': 1.79},
    {'item':'smart water', 'price': 1.99},
    {'item':'powerade (20oz)', 'price': 1.99},
    {'item':'vitamon water (20oz)', 'price': 1.99},
    {'item':'minute maid', 'price': 1.89},
    {'item':'honest tea', 'price': 2.09},
    {'item':'can pop', 'price': 0.99},
    {'item':'fountain drink (small)', 'price': 1.39},
    {'item':'fountain drink (medium)', 'price': 1.69},
    {'item':'fountain drink (large)', 'price': 1.99},
    {'item':'coke (20oz)', 'price': 1.89},
    {'item':'sprite (20oz)', 'price': 1.89},
    {'item':'coke (1L)', 'price': 2.19},
    {'item':'sprite (1L)', 'price': 2.19},
    {'item':'fanta (20oz)', 'price': 1.89},
    {'item':'canada dry ginger ale (20oz)', 'price': 1.89},
    {'item':'fresca', 'price': 1.89},
    {'item':'mello yello', 'price': 1.89},
    {'item':'monster energy', 'price': 3.09},
    {'item':'apple', 'price': 1.19},
    {'item':'mandarin', 'price': 0.49},
    {'item':'asian pear', 'price': 2.69},
    {'item':'chicken & cheese wrap', 'price': 5.99},
    {'item':'grilled vegetables wrap', 'price': 5.99},
    {'item':'chicken caesar salad', 'price': 5.99},
    {'item':'caesar salad', 'price': 5.99},
    {'item':'quinoa & vegetable salad', 'price': 5.99},
    {'item':'classic caesar salad', 'price': 5.99},
    {'item':'garden salad', 'price': 5.99},
    {'item':'greek salad', 'price': 5.99},
    {'item':'chicken salad sandwich', 'price': 5.99},
    {'item':'tuna fish salad sandwich triangle', 'price': 5.99},
    {'item':'smoked turkey + swiss sandwich', 'price': 5.99},
    {'item':'peanut butter +grape jelly sandwich (white/wheat)', 'price': 2.99},
    {'item':'vegan buffalo wing wrap', 'price': 5.99},
    {'item':'cuban sandwich', 'price': 5.99},
    {'item':'italian combo', 'price': 5.99},
    {'item':'tuna sandwich on gluten free roll', 'price': 5.99},
    {'item':'turkey and swiss sandwich on gluten free roll', 'price': 5.99},
    {'item':'chicken salad sandwich', 'price': 5.99},
    {'item':'chicken with fresh mozzarella + tomato', 'price': 5.99},
    {'item':'tomato,basil,pesto +mozzarella', 'price': 5.99},
    {'item':'tuna salad sandwich', 'price': 5.99},
    {'item':'turkey +cheddar sandwich', 'price': 5.99},
    {'item':'pastrami + swiss sandwich', 'price': 5.99},
    {'item':'corned beef + swiss sandwich', 'price': 5.99},
    {'item':'tuna fish wrap', 'price': 5.99},
    {'item':'roasted beef kaiser sandwich', 'price': 5.99},
    {'item':'tuna salad bites', 'price': 4.99},
    {'item':'buffalo chicken bites', 'price': 4.99},
    {'item':'chicken caesar bites', 'price': 4.99},
    {'item':'tomato +mozzarella bites', 'price': 4.99}]

entrees= [
    {'item':'chicken & cheese wrap', 'price': 5.99},
    {'item':'grilled vegetables wrap', 'price': 5.99},
    {'item':'chicken caesar salad', 'price': 5.99},
    {'item':'caesar salad', 'price': 5.99},
    {'item':'quinoa & vegetable salad', 'price': 5.99},
    {'item':'classic caesar salad', 'price': 5.99},
    {'item':'garden salad', 'price': 5.99},
    {'item':'greek salad', 'price': 5.99},
    {'item':'chicken salad sandwich', 'price': 5.99},
    {'item':'tuna fish salad sandwich triangle', 'price': 5.99},
    {'item':'smoked turkey + swiss sandwich', 'price': 5.99},
    {'item':'smoked turkey + swiss sandwich', 'price': 5.99},
    {'item':'peanut butter + grape jelly sandwich (white/wheat)', 'price': 2.99},
    {'item':'vegan buffalo wing wrap', 'price': 5.99},
    {'item':'cuban sandwich', 'price': 5.99},
    {'item':'italian combo', 'price': 5.99},
    {'item':'tuna sandwich on gluten free roll', 'price': 5.99},
    {'item':'turkey and swiss sandwich on gluten free roll', 'price': 5.99},
    {'item':'chicken salad sandwich', 'price': 5.99},
    {'item':'chicken with fresh mozzarella + tomato', 'price': 5.99},
    {'item':'tomato,basil,pesto +mozzarella', 'price': 5.99},
    {'item':'tuna salad sandwich', 'price': 5.99},
    {'item':'turkey +cheddar sandwich', 'price': 5.99},
    {'item':'pastrami + swiss sandwich', 'price': 5.99},
    {'item':'corned beef + swiss sandwich', 'price': 5.99},
    {'item':'tuna fish wrap', 'price': 5.99},
    {'item':'roasted beef kaiser sandwich', 'price': 5.99},
    {'item':'tuna salad bites', 'price': 4.99},
    {'item':'buffalo chicken bites', 'price': 4.99},
    {'item':'chicken caesar bites', 'price': 4.99},
    {'item':'tomato +mozzarella bites', 'price': 4.99}]

fruits_and_chips= [
    {'item':'small lays chips', 'price': 0.99},
    {'item':'apple', 'price': 1.19},
    {'item':'mandarin', 'price': 0.49},
    {'item':'asian pear', 'price': 2.69}]

drinks=[
    {'item':'trumoo milk (14 fl oz)', 'price': 1.69},
    {'item':'dasani water (10.1 fl oz)', 'price': 0.99},
    {'item':'fountain drink (small)', 'price': 1.39}]

def final_project():
    """ a program designed for c-store customers """
    print_instructions()
    print("")
    print("Here is a list of all items: ")
    print_all_items()
    print("")
    print("Choices: 1 to check price, 2 to calculate total of a shopping cart, 3 to check if entered items are eligible for a meal and 4 to check if a given date is eligible for discount.")
    choice=int(input("Enter a number as your choice(Enter 5 to quit): "))
    while choice !=5:
        if choice==1:
            item=input("Enter the name of the item: ")
            print(price_checker(item))
        elif choice==2:
            calTotal()
        elif choice==3:
            meal()
        else:
            print(discountChecker())
        choice=int(input("Enter a number as your choice(Enter 5 to quit): "))
    print("Thank you for using the C-store App! Have a good one:)")

def print_instructions():
    """print_instructions() tells users the functions of this program"""
    instructions = """Welcome to the C-Store App! In this app, you can:
    1. Check the price of an item;
    2. Calculate the total price of a shopping cart;
    3. Check items eligible for a meal;
    4. Check if there's a discount with a given date.
    """
    print(instructions)

def print_all_items():
    for x in all_items:
        print(x['item'])

def price_checker(item):
    '''
    returns the price of items that an individual is interested in buying
    '''

    for x in all_items:
        if x['item']==item:
            return "The price of the item is $"+str(x['price'])
    return "The item doesn't exist."


def calTotal():
    ''' calculates and gives the grand total
        for the items entered after user has specified
        the quantity for each item
    '''

    item = input("Please enter the name of the item you would like to purchase, or enter 'quit' to quit: ")

    total = 0
    while item != 'quit':
        quantity = int(input("Please specify the quantity for the indiviaul items you would like to purchase: "))

        for x in all_items:
            if x['item']==item:
                total = total + (x['price']*(quantity))

        item = input("Please enter the name of the item you would like to purchase, or enter 'quit' to quit: ")

    print ("The calculated total for the number of items you have specified is $", total)

def meal():
    exist=False;
    print("Composition of a meal: a salad or a sandwich, a small chip or a fruit and a small water, a milk or a fountain drink.")
    entree=input("Enter the name of a salad or a sandwich: ")
    for x in entrees:
        if x['item']==entree:
            exist=True
    if exist==True:
        print("This item qualifies for an entree in a meal.")
    else:
        print("This item doesn't qualifiy for an entree in a meal.")

    exist=False;
    side=input("Enter the name of a fruit or a snack: ")
    for x in fruits_and_chips:
        if x['item']==side:
            exist=True
    if exist==True:
        print("This item qualifies for a side in a meal.")
    else:
        print("This item doesn't qualifiy for a side in a meal.")

    exist=False;
    drink=input("Enter the name of a water, a milk or a fountain drink: ")
    for x in drinks:
        if x['item']==drink:
            exist=True
    if exist==True:
        print("This item qualifies for a drink in a meal.")
    else:
        print("This item doesn't qualifiy for a drink in a meal.")

def discountChecker():
    date=input("Enter today's date in MM/DD format(eg, 0101 for Jan 1st): ")
    for x in discount:
        if x['date']==date:
            return "Today is "+str(x['name'])+" and the discount is "+str((1-x['discount'])*100)+ " percent off."
    return "Sorry, today is not a holiday. No discounts today."

if __name__=="__main__":
    final_project();
