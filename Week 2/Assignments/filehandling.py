'''
Write a Python function called read_file() that takes a single parameter
filename, and opens the specified file in read-only mode. 
The function should read the entire contents of the file and return the contents as a string.
'''

def read_file():
    file = open(r'C:\Users\Hp\Desktop\TWL_DRCFS_30DaysPythonBootcamp\Week 2\Assignments\my_file.txt' , 'r')
    contents = file.read()
    print(contents)

read_file()
    