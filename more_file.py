from sys import argv 
from os.path import exists

from_file = "test.txt"
to_file = "new_test.txt"

print(f"Copying from {from_file} to {to_file}")

in_file =open(from_file)
indata = in_file.read()

print("The input file is {len*(indata*)*} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETRUN to continue, CTRL-C to abort.")
input()

out_files = open(to_file, 'w')
out_files.write(indata)

