def meal():
    '''
    asks the individual if he or she would like to use a meal instead of
    money or points for the items that they have identified
    ''' 
    
    meal_menu: ['MAIN_ITEMS', 'FRUIT_AND_CHIPS', 'DRINK']

    MAIN_ITEMS: [
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

    FRUITS_AND_CHIPS: [
        {'item':'small lays chips', 'price': 0.99},
        {'item':'apple', 'price': 1.19},
        {'item':'mandarin', 'price': 0.49},
        {'item':'asian pear', 'price': 2.69}]

    DRINKS: [
        {'item':'trumoo milk (14 fl oz)', 'price': 1.69},
        {'item':'dasani water (10.1 fl oz)', 'price': 0.99},
        {'item':'fountain drink (small)', 'price': 1.39}]
