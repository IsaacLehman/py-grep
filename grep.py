import glob
import os
import sys

green = '\033[32m'
white = '\033[39m'
clear_top = '\033[2J'
# Using '*' pattern
print(clear_top)
print(green)
print("Your current working directory: ", os.getcwd())
print("Items in current directory:")
print('  |  '.join(os.listdir()))
print()
print("--------------------------------------------")
starting_path = input("Enter the path to search on: ")
search_arg    = input("Enter your search argument: ")
print("--------------------------------------------")
print()
def print_dir(path, search):
    num_errors = 0
    num_files  = 0
    for f in glob.glob(path):
        if os.path.isdir(f): # IF A DIRECTORY
            nf, ne = print_dir(f+"/*", search)
            num_files  += nf
            num_errors += ne
            continue
        num_files += 1
        try:
            with open(f, 'r') as reader:
                lines = reader.readlines()
                line_num = 1
                for line in lines:
                    if search in line:
                        finds.append((str(line_num), green+" → "+white, f))
                    line_num+=1
        except Exception as e:
            num_errors += 1 # if we could not read the file
    return num_files, num_errors

finds = []
num_files, num_errors = print_dir(starting_path+'/*', search_arg)
print(green+"# Non-Readable Files: ", num_errors)
print("# Readable Files: ", num_files)
print()
print("Line #\t\tFile Path", white)
for f in finds:
    print('\t'.join(f))
print()
