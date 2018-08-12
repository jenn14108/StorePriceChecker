def price_checker(item):
    '''
    returns the price of items that an
    individual is interested in buying
    '''

    menu = [
    {'item':'burger', 'price': 7.25},
    {'item':'steak', 'price': 12.00},
    {'item':'curry','price': 18.50},
    {'item':'sushi','price': 15.00},
    {'item':'lobster','price': 29.45},
    {'item':'mac and cheese','price': 6.25},
    {'item':'roast chicken','price': 9.50},
    {'item':'salmon','price': 15.34},
    {'item':'caesar salad','price': 9.00},
    {'item':'soda','price': 2.25},
    {'item':'bottled water','price': 1.50}]

    for x in items:
        if x['item'] == item: 
            return x['price']

if __name__ == "__main__":
    print("This program will give you the price of the items you are interested in purchasing")
    print("In all lowercase letters, type in item names until you are done, then type 'done'")

   user_input = input("Enter an item ")
