# Store the number to guess
our_fav_number = 10

# ourFavNumber OurFavNumber our_fav_number

# take user input
user_guess = input("Enter your guess: ")

# print(type(user_guess))

user_guess = int(user_guess)

# print(type(user_guess))

# < == > >= <= 

if user_guess == our_fav_number:
    print("Success, you guessed the number! Our favourite is: " + str(our_fav_number))

if user_guess < our_fav_number:
    print("Your guess is too low. Try a little higher")

if user_guess > our_fav_number:
    print("Your guess is too high. Try a little lower")


# try and except