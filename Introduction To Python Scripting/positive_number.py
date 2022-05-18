user_no = input("Enter a number: ")

# Validation
try:
    # Runs if input is valid
    user_no = float(user_no)
    print("Hooray, you entered a number")

    if user_no >= 0:
        print("True")
    
    else:
        print("False")

except:
    # Runs if input is invalid
    print("User input is not a number. Please enter a number")