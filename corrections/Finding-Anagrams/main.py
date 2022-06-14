# Check if a word is an anagrams 


def find_anagrams(word, anagram):
    # [assignment] Add your code here
    
    # Change words to lowercase
    word = word.lower()
    anagram = anagram.lower()

    # Remove whitespace
    word = word.replace(" ", "")
    anagram = anagram.replace(" ", "")

    # sorted(word) == sorted(anagram) # True or False
    return sorted(word) == sorted(anagram)



print("Calling find_anagrams with 'silent' and 'listen' ", find_anagrams("silent", "listen"))
print("Calling find_anagrams with 'elvis' and 'lives' ", find_anagrams("elvis", "lives"))
print("Calling find_anagrams with 'dormitory' and 'dirty room' ", find_anagrams("dormitory", "dirty room"))

print("Calling find_anagrams with 'yellow' and 'hello' ", find_anagrams("yellow", "hello"))

