filename = "a.txt"

print("we're going to erase {filename}.")
print("if you don't want that, hit cTRl-C*(*^C*).")
print("if you do want that, hit RETRUN.")

input("?")

print("Opening the file..")
target = open(filename, 'w')

print("Truncating the file, Goodbye!")

target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("Now I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally, we close it.")
target.close()


