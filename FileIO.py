my_file = open('test.txt', mode='w+') # while opening a file with 'w' mode, it truncates any existing text
# Modes available while opening a file :
#   w - write mode (overwrite any existing file or create a new one)
#   r - read mode (gives an error if a file doesn't exist)
#   a - append mode (used to write on an existing file, also gives error if a file doesn't exist)
#   r+ - read and write (gives an error if a file doesn't exist)
#   w+ - write and read (overwrite any existing file or create a new one)
my_file.write('Created a new File, will now close it after reading')
print(my_file.read())
my_file.close()
# Need to close the file to prevent any leak
# If we don't want to close a file, we can use another syntax:
with open('test.txt', mode='w+') as file:
    file.write('Created a new file, without the need to close it')
    print(file.read())
# To iterate through a file
for line in open('test.txt', mode = 'r'):
    print(line)
