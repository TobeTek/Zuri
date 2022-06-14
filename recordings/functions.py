def print_name(name, nationality, age=18):
    # Add code or steps
    print(f"My name is {name}")
    print(f"My age is {age}")
    print(f"My country/nationality is {nationality}")


def sum(*args):
    # Return the sum to our program 
    print(args)
    sum = 0
    for no in args:
        sum += no
    
    return sum

b = sum(5, 6, 10 ,14)
print(b)

b = sum(2,3)
print(b)



