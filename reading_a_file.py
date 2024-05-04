from sys import argv

script, filename = argv #here we are passing two argument 1. script name 2. txt file name 

txt = open(filename)

print(f"Here's you file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input(">") # this is allow you open this file twice.

txt_again = open(file_again)

print(txt_again.read())
