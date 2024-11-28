# Create a program that will accept a word and output the word one letter at a time in reverse.
word = str(input( " What is your word? " ))
for i in range(len(word)-1, 0-1, -1):
    print (word[i])
