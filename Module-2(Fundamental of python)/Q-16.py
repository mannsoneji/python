# Write a Python program to count the occurrences of each word in a given sentence

sentance = input("Enter the sentance : ").lower()


words = sentance.split()
wordcount = {}

for word in words:
    wordcount[word] = wordcount.get(word, 0) + 1

print(wordcount)