# Ask user for input
user_sentence = input("Enter a sentence: ")

# Remove extra whitespace
user_sentence = user_sentence.strip(" ")

# Split the sentence into words
list_of_words = user_sentence.split(" ")

# Get the number of words
no_words = len(list_of_words)

# Print out the number of words
print(no_words)