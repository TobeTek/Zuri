# if

if 10 < 20:
    print("10 is less than 20")

if 5 == 20:
    print("5 is equal to 20")

# elif --> else if
if "a" == "b":
    print("a is the same as b")

elif "a" != "b":
    print("a is not equal to b")

elif 100 < 200:
    print("100 is less than 200")

# else
our_flag = 500 == 1000 # our_flag = False

if our_flag:
    print("500 is equal to 1000")

elif False:
    print("80 is greater than 90")

elif True:
    print("Running true block")

else:
    print("Running the else block")

