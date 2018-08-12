def calTotal():
    ''' calculates and gives the grand total
        for the items entered after user has specified
        the quantity for each item
    '''
    
    user_input = input("Please enter the name of the item you would like to purchase, or enter quit to quit")

    total = 0 
    while user_input != 'quit':
        quantity = input("Please specify the quantity for the indiviaul items you would like to purchase")
        for x in menu:
            if x['item'] == item:
            total = total + (x['price']*(quantity))

    print ("The calculated total for the number of items you have specified is $", total)
                    
                       
    
