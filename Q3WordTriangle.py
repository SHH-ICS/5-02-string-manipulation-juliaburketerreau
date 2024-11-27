
word = str(input( " Enter your word: " ))
length = len(word)
for i in range(length):
    for j in range(i + 1):
      print(word[j], end=" ")
    print()
   



