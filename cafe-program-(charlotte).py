#cafe program

import time
cost = 0
orders = []

print("**************************************************")
print("Welcome to Cloudy Cafe!")
print()
time.sleep(1)

while True:
    print("""
    Please pick an option:
    a) Food Options
    b) Snack Options
    c) Desert Options
    d) Drink options
    V) View chosen choices and current cost
    F) FINISH """)
    print()

    time.sleep(1)
    opt = input("Your option is: ")
    time.sleep(1)
    print()

    if opt == 'a':
        print("=========================================")
        print("You have chosen: Food Options")
        print("=========================================")

        time.sleep(1)
        while True:
            print("""
            1) Fried rice with egg
            2) Spaghetti Bolognese
            3) Beef Steak
            4) Chicken Salad
            B) BACK""")
            print()

            print()
            time.sleep(1)
            fopt = input("Your Food Option is: ")

            time.sleep(1)
            if fopt == '1':
                print("+++++++++++++++++++++++++++++++++++++++++")
                print("You have chosen: Fried rice and egg")
                orders.append('Fried rice and egg')
                time.sleep(1)
                print("This will cost: £4.99")
                cost = cost + 4.99
                print("+++++++++++++++++++++++++++++++++++++++++")
                print()
                print("**************************************************")

                break 


            if fopt == '2':
                print("+++++++++++++++++++++++++++++++++++++++++")
                print("You have chosen: Spaghetti Bolognese")
                orders.append('Spaghetti Bolognese')
                time.sleep(1)
                print("This will cost: £5.45")
                cost = cost + 5.45
                print("+++++++++++++++++++++++++++++++++++++++++")
                print()
                print("**************************************************")
                break

            if fopt == '3':
                print("+++++++++++++++++++++++++++++++++++++++++")
                print("You have chosen: Beef Steak")
                orders.append('Beef Steak')
                time.sleep(1)
                print("This will cost: £5.00")
                cost = cost + 5.00
                print("+++++++++++++++++++++++++++++++++++++++++")
                print()
                print("**************************************************")
                break

            if fopt == '4':
                print("+++++++++++++++++++++++++++++++++++++++++")
                print("You have chosen: Chicken Salad")
                orders.append('Chicken Salad')
                time.sleep(1)
                print("This will cost: £4.90")
                cost = cost + 4.90
                print("+++++++++++++++++++++++++++++++++++++++++")
                print()
                print("**************************************************")
                break

            if fopt == 'B':
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("Back to the beggining!")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                time.sleep(1)
                break



    if opt == 'b':
        print("=========================================")
        print("You hav chosen: Snack Options")
        print("=========================================")
        
        
        time.sleep(1)
        while True:
            print("""
            1) Turkey Sandwiches
            2) French Fries
            3) Crossaint
            4) Fruit Salad
            B) BACK""")
            print()

            sopt = input("Your Snack Option is: ")
            time.sleep(1)
            print()

            time.sleep(1)
            if sopt == '1':
                print("+++++++++++++++++++++++++++++++++++++++++")
                print("You have chosen: Turkey Sandwiches")
                orders.append('Turkey Sandwiches')
                time.sleep(1)
                print("This will cost: £2.50")
                cost = cost + 2.50
                print("+++++++++++++++++++++++++++++++++++++++++")
                print()
                print("**************************************************")
                break
    
            if sopt == '2':
                print("+++++++++++++++++++++++++++++++++++++++++")
                print("You have chosen: French Fries")
                orders.append('French Fries')
                time.sleep(1)
                print("This will cost: £2.10")
                cost = cost + 2.10
                print("+++++++++++++++++++++++++++++++++++++++++")
                print()
                print("**************************************************")
                break

            if sopt == '3':
                print("+++++++++++++++++++++++++++++++++++++++++")
                print("You have chosen: Crossaint")
                orders.append('Crossaint')
                time.sleep(1)
                print("This will cost: £1.50")
                cost = cost + 1.50
                print("+++++++++++++++++++++++++++++++++++++++++")
                print()
                print("**************************************************")
                break
    
            if sopt == '4':
                print("+++++++++++++++++++++++++++++++++++++++++")
                print("You have chosen: French Fries")
                orders.append('French Fries')
                time.sleep(1)
                print("This will cost: £2.00")
                cost = cost + 2.00
                print("+++++++++++++++++++++++++++++++++++++++++")
                print()
                print("**************************************************")
                break
            

            if sopt == 'B':
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("Back to the beggining!")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                time.sleep(1)
                break


    if opt == 'c':
        print("=========================================")
        print("You hav chosen: Desert Options")
        print("=========================================")

        time.sleep(1)
        while True:
            print("""
            1) Ice Cream
            2) Caramel Cake
            3) Chocolate Brownie
            4) Strawberry Donut
            B) BACK""")
            print()

            dopt = input("Your Desert Option is: ")
            time.sleep(1)
            print()

            time.sleep(1)
            if dopt == '1':
                print("+++++++++++++++++++++++++++++++++++++++++")
                print("You have chosen: Ice Cream")
                orders.append('Ice Cream')
                time.sleep(1)
                print("This will cost: £1.90")
                cost = cost + 1.90
                print("+++++++++++++++++++++++++++++++++++++++++")
                print()
                print("**************************************************")
                break
        
            if dopt == '2':
                print("+++++++++++++++++++++++++++++++++++++++++")
                print("You have chosen: Caramel Cake")
                orders.append('Caramel Cake')
                time.sleep(1)
                print("This will cost: £2.00")
                cost = cost + 2.00
                print("+++++++++++++++++++++++++++++++++++++++++")
                print()
                print("**************************************************")
                break

            if dopt == '3':
                print("+++++++++++++++++++++++++++++++++++++++++")
                print("You have chosen: Chocolate Brownie")
                time.sleep(1)
                print("This will cost: £1.50")
                cost = cost + 1.50
                print("+++++++++++++++++++++++++++++++++++++++++")
                print()
                print("**************************************************")
                break
        
            if dopt == '4':
                print("+++++++++++++++++++++++++++++++++++++++++")
                print("You have chosen: Strawberry Donut")
                orders.append('Strawberry Donut')
                time.sleep(1)
                print("This will cost: £1.90")
                cost = cost + 1.90
                print("+++++++++++++++++++++++++++++++++++++++++")
                print()
                print("**************************************************")
                break
            
            if dopt == 'B':
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("Back to the beggining!")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                time.sleep(1)
                break



    if opt == 'd':
        print("=========================================")
        print("You hav chosen: Drink Options")
        print("=========================================")

        time.sleep(1)
        while True:
            print("""
            1) Milkshake
            2) Smoothie
            3) Hot Chocolate
            4) Ice Tea
            5) Soda
            B) BACK""")
            print()

            bopt = input("Your Drink Option is: ")
            time.sleep(1)
            print()


            #Putting bopt instead of dopt because then we'd have two and it would get mixed up with drink and desert
            #The b in bopt just stands for beverage instead

            print()
            time.sleep(1)
            if bopt == '1':
                print("+++++++++++++++++++++++++++++++++++++++++")
                print("You have chosen: Milkshake")
                orders.append('Milkhake')
                time.sleep(1)
                print("This will cost: £2.50")
                cost = cost + 2.50
                print("+++++++++++++++++++++++++++++++++++++++++")
                print()
                print("**************************************************")
                break
        
            if bopt == '2':
                print("+++++++++++++++++++++++++++++++++++++++++")
                print("You have chosen: Smoothie")
                orders.append('Smoothie')
                time.sleep(1)
                print("This will cost: £2.45")
                cost = cost + 2.45
                print("+++++++++++++++++++++++++++++++++++++++++")
                print()
                print("**************************************************")
                break

            if bopt == '3':
                print("+++++++++++++++++++++++++++++++++++++++++")
                print("You have chosen: Hot Chocolate")
                orders.append('Hot Chocolate')
                time.sleep(1)
                print("This will cost: £2.50")
                cost = cost + 2.50
                print("+++++++++++++++++++++++++++++++++++++++++")
                print()
                print("**************************************************")
                break
        
            if bopt == '4':
                print("+++++++++++++++++++++++++++++++++++++++++")
                print("You have chosen: Ice Tea")
                orders.append('Ice Tea')
                time.sleep(1)
                print("This will cost: £2.00")
                cost = cost + 2.00
                print("+++++++++++++++++++++++++++++++++++++++++")
                print()
                print("**************************************************")
                break
        
            if bopt == '5':
                print("+++++++++++++++++++++++++++++++++++++++++")
                print("You have chosen: Soda")
                orders.append('Soda')
                time.sleep(1)
                print("This will cost: £1.10")
                cost = cost + 1.10
                print("+++++++++++++++++++++++++++++++++++++++++")
                print()
                print("**************************************************")
                break
            
            if bopt == 'B':
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("Back to the beggining!")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                time.sleep(1)
                break


    if opt == 'V':
        print("You've chosen to view your current items and cost")
        time.sleep(1)
        print()
        print("Here are your items:")
        for item in orders:
            print(item)
        time.sleep(1)
        print()
        print("Your current cost is: £" ,cost, " ")




    if opt == 'F':
        print("You have Chosen to leave")

        while True:
            time.sleep(1)
            print("Items you have chosen:")
            for item in orders:
                print(item)
            time.sleep(1)
            print()
            print("Your total amount is: £" ,cost, " ")
            print()
            time.sleep(2)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Bye! We hope to see you soon :]")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            time.sleep(1)
            print()
            print("Find more information about us on our website:") #put link to html webpage here
            time.sleep(1)
            breakpoint()