# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.
redo = True
while redo:
  word = str(input( " What is your word? " ))
  print("Type 'quit' if you want to exit")
  if word == "quit":
    break
  else:
    redo = True
    print(len(word))