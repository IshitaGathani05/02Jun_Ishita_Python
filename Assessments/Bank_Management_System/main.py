import banker
import customer


#Menu for user's option
def options():
    while True:
        print()
        print("-----WELCOME TO PYTHON BANK MANAGEMENT SYSTEM-----")
        print("Select your role")
        print("1. Banker")
        print("2. Customer")
        print("3. Exit")
        choice=int(input("Choose your role (1-3): "))

        if choice==1:
            while True:
                banker.menu()
                break

        if choice==2:
            while True:
                customer.menu()
                break
        
        if choice==3:
            while True:
                print("Exiting...Thank You")
                exit()

#Run the app
options()