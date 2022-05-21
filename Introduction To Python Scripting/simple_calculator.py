# Simple CLI Calculator
print("Welcome to Simple CLI Calculator")

is_running = True 

while is_running:
    # Processing Calculations...
    print("Starting Calculator Process")
    user_operation = input("What operation would you like to perform?\nPick any of ['+','-','*', '/', '%'] : ")

    # Get user numbers
    try: # Try to get user numbers, if they're valid integers/floats, continue
        no1 = float(input("First number: "))
        no2 = float(input("Second number: "))
    
    except: # We get an error when running it
        print("Failed, invalid numbers...")
        continue 


    if user_operation == "+":
        # perform addition
        print(no1 + no2)

    elif user_operation == "-":
        # perform subtraction
        print(no1 - no2)

    elif user_operation == "*":
        # perform multiplication
        print(no1 * no2)

    elif user_operation == "/":
        # perform division
        print(no1 / no2)

    elif user_operation == "%":
        # perform division
        print(no1 % no2)

    else:
        # Invalid operation
        print("Invalid operation entered, try again...")
    
    choice = input("Would you like to run another calculation. [y,n] :")
    if choice == "y":
        pass 
    
    if choice == "n":
        is_running = False 
        # This is the same thing as a break.

print("Thanks for using the Calculator, bye bye...")

# Ctrl + C to exit any Python program...!