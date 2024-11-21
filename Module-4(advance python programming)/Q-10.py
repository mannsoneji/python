# Write a Python program to count the frequency of words in a file.

def count_frequency(file_name):
    word_count = {}

    with open(file_name, 'r') as file:
        for line in file:
            words = line.strip().lower().split()


            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    return word_count

file_name = 'example.txt'

word_frequency = count_frequency(file_name)

for word, count in  word_frequency.items():
    print(f"{word}: {count}")
