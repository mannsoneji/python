#  Write a python program to find the longest words.

def find_longest_word(text):
    words = text.split()

    max_length = max(len(word) for word in words)

    longest_word = [word for word in words if len(word) == max_length]

    return longest_word

text = "Hello world welcome to python programming language"

longest_words = find_longest_word(text)

print("The longest word is : ",longest_words)


