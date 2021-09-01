# Get user name.
userName = str(input("Welcome to the Online Super Market!\n\nPlease Enter your name: "))

while True:
    # Getting the user to choose the department.
    print("\nHi!",userName,"\nWhat are you looking for?\n")
    department =  input("Press   'G' for Groceries,\n\t'B' for Bisuits and Chocolates\n\t'PF' for Pet Food\n\t'PC' for Personal Care\n\t'Done' to checkout\n\t")
    # **********************************************************************************************************************************************************
    # Dictionaries:

    # Dictionary of every available fruit.
    fruits = [{'0. Apple':{'Rate':120, 'Quantity/kg':1}}, {'1. Banana':{'Rate':40, 'Quantity/dozen':1}}, {'2. Watermelon':{'Rate':60, 'Quantity/kg':1}}, {'3. Chikoo':{'Rate':30, 'Quantity/kg':1}}, {'4. DragonFruit':{'Rate':150, 'Quantity/kg':1}}, {'5. Kiwi':{'Rate':100, 'Quantity/kg':1}}, {'6. Melon':{'Rate':120, 'Quantity/kg':1}}, {'7. Lichi':{'Rate':130, 'Quantity/kg':1}}, {'8. Mango':{'Rate':70, 'Quantity/kg':1}}, {'9. Grapes':{'Rate':80, 'Quantity/kg':1}}, {'10. Cherry':{'Rate':50, 'Quantity/kg':1}}, {'11. Strawberry':{'Rate':150, 'Quantity/kg':1}}]

    # Dictionary of every available vegetable
    vegetables = [{'0. Onion':{'Rate':40, 'Quantity/kg':1}}, {'1. Tomato':{'Rate':20, 'Quantity/kg':1}}, {'2. Potato':{'Rate':30, 'Quantity/kg':1}}, {'3. Ladyfinger':{'Rate':50, 'Quantity/kg':1}}, {'4. Cauliflower':{'Rate':100, 'Quantity/kg':1}}, {'5. Cucumber':{'Rate':40, 'Quantity/kg':1}}, {'6. Carrot':{'Rate':35, 'Quantity/kg':1}}, {'7. Green_Peas':{'Rate':100, 'Quantity/kg':1}}, {'8. French_Beans':{'Rate':70, 'Quantity/kg':1}}, {'9. Drumstick':{'Rate':60, 'Quantity/kg':1}}, {'10. Lemon':{'Rate':5, 'Quantity/unit':1}}, {'11. Cabbage':{'Rate':100, 'Quantity/kg':1}}]
    
    # Dictionary of every available Biscuits and Chocolates
    biscuits_chocolates = [{'0. Biscuit_Name_1':{'Rate':45, 'Quantity/unit':1}}, {'1. Biscuit_Name_2':{'Rate':75, 'Quantity/unit':1}}, {'2. Biscuit_Name_3':{'Rate':20, 'Quantity/unit':1}}, {'3. Chocolate_Name_1':{'Rate':30, 'Quantity/unit':1}}, {'4. Chocolate_Name_2':{'Rate':220, 'Quantity/unit':1}}, {'5. Chocolate_Name_3':{'Rate':150, 'Quantity/unit':1}}]
    
    # Dictionary of every available Pet food
    pet_food = [{'0. Petfood_Name_1':{'Rate':180, 'Quantity/unit':1}}, {'1. Petfood_Name_2':{'Rate':175, 'Quantity/unit':1}}, {'2. Petfood_Name_3':{'Rate':340, 'Quantity/unit':1}}, {'3. Petfood_Name_4':{'Rate':400, 'Quantity/unit':1}}, {'4. Petfood_Name_5':{'Rate':520, 'Quantity/unit':1}}, {'5. Petfood_Name_6':{'Rate':1050, 'Quantity/unit':1}}]
    
    # Dictionary of every available Personal Care
    personal_care = [{'0. Shampoo':{'Rate':20, 'Quantity/unit':1}}, {'1. Toothbrush':{'Rate':45, 'Quantity/unit':1}}, {'2. Toothpaste':{'Rate':90, 'Quantity/unit':1}}, {'3. Beard_Oil':{'Rate':45, 'Quantity/unit':1}}, {'4. Soap':{'Rate':50, 'Quantity/unit':1}}, {'5. Hair_Oil':{'Rate':120, 'Quantity/unit':1}}, {'6. Facewash':{'Rate':250, 'Quantity/unit':1}}]
    # **********************************************************************************************************************************************************

    def cleanUpFunc(itemsDictionary, category):

        #Printing the Dictionary out.
        for eachitem in itemsDictionary:
            print(eachitem, '\n')

        totalCategoryAmount = 0     
        while True:
            print("\nEnter 'done' to checkout.\n\nEnter the", category, "corresponding number: ")
            itemNumber = input()

            if itemNumber == 'done': break # To exit the while loop if typed 'done'.
            else: 
                try:
                    # converting the input into 'integer'.
                    itemNumber = int(itemNumber)

                    # If the input is greater than the length of the Dictionary, then a message is diaplayed and 'continue' statement is used.
                    if itemNumber > (len(itemsDictionary)-1):
                        print("Invalid Input. PLease try again!")
                        continue
                    else:
                        quantity = int(input("Enter the quantity: "))
                        print()

                        # Triple Split Pattern.
                        firstSplit = str(itemsDictionary[itemNumber]).split() # Value from the dictionary is extracted, converted to string, and splitted.
                        secondSplit = firstSplit[1].split("'")                # Split with argument given for extracting name.
                        thirdSplit = firstSplit[3].split(",")                 # Split with argument given for extracting rate.
                        itemNameExtract = secondSplit[0]                      # Item Name extraction.
                        rateExtract = thirdSplit[0]                           # Rate extraction. 
                        price = int(rateExtract)*quantity                     # Calculating price
                except:
                    print("Invalid Input. Please try again!!")
                    continue

            print(category, "Name: ", itemNameExtract, "\nRate: ", rateExtract, "\nQuantity: ", quantity, "\nAmount to be paid: ", price)
            totalCategoryAmount = totalCategoryAmount+price # Calculating the total amount.
        print("\nTotal", category, "Amount to be paid: ", totalCategoryAmount, "\n\nHave a Good Day!", userName)

    # ******************************************************************************************************************************

    def groceries():
        # Getting the user to choose the category.
        gSelection = int(input("What would you like to buy?\nPress   '1' for Fruits\n\t'2' for Vegetables\n"))

        # Fruits Category
        if gSelection == 1:
            categoryName = "Fruit's"
            cleanUpFunc(fruits, categoryName)
        elif gSelection == 2:
            categoryName = "Vegetable's"
            cleanUpFunc(vegetables, categoryName)

    def biscuitsAndChocolates():
        categoryName = "Product"
        cleanUpFunc(biscuits_chocolates, categoryName)

    def petFood():
        categoryName = "Pet Food's"
        cleanUpFunc(pet_food, categoryName)

    def personalCare():
        categoryName = "Product"
        cleanUpFunc(personal_care, categoryName)

    # ******************************************************************************************************************************
    
    if department == 'Done': break
    elif department == 'G': 
        print("So, you're here today for Groceries.\n")
        groceries()
    elif department == 'B': 
        print("So, you're here today for Biscuits and Chocolates.")
        biscuitsAndChocolates()
    elif department == 'PF': 
        print("So, you're here today for Pet Food.")
        petFood()
    elif department == 'PC': 
        print("So, you're here today for Personal Care or Toiletries.")
        personalCare()
    else:
        print("Invalid Input. PLease try again!")
        continue