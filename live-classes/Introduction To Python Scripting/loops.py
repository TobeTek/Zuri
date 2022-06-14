# While Loops

is_nighttime = True 

hour_of_the_day = 0

# When it is 10, we should wake up
while is_nighttime:
    print("The Hour of the day is ", hour_of_the_day)

    if hour_of_the_day == 10:
        print("Waking up!")
        break
    
    # Keep sleeping
    hour_of_the_day = hour_of_the_day + 1
    
    

# Wake up and start your day
print("We've woken up!")