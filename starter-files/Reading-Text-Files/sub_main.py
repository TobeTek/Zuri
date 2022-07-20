def read_file(filename):
    open_file = open("./story.txt", "r")
    read_file = open_file.read()
    print(read_file)


# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}from fileinput import filename


def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as f:
        # Removed print line, and make use of return
        return f.read()


def count_words(read_file_content):
    text = read_file_content("Reading-Text-Files\story.txt")
    # assignment] Add your code here
    counter = dict()

    # Find a way to remove punctuation from `text`

    list_of_lines = text.split("\n")

    for line in list_of_lines:

        line = line.strip()
        line = line.lower()
        words = line.split(" ")
        for word in words:
            # Check if the word is already in dictionary
            if word in counter:
                # Increment count of word by 1
                counter[word] = counter[word] + 1
            else:
                # Add the word to dictionary with count 1
                counter[word] = 1
            return counter  # "as": 10, "would": 20}


print(count_words(read_file_content))
