# Feel free to add as much lines as you want between ## START CODE HERE and ## END CODE HERE.
# Please donot write code outside this boundry or you may fail the test.

# start by importing the necessary documents
import os
import random
import string 
dirname = os.path.dirname(__file__)

def rank(pwd: str) -> str:
    '''
    Ranker function that ranks the password based on the assigned criteria

    Input: pwd -> character or string

    The following are the requirements for POOR / MODERATE / STRONG password.

    Passwords can contain (not required) any of the following requirements:  
    i. Lower case letters (a – z).       iii) Numbers ( 0 – 9 ).  
    ii. Upper case letters (A – Z).      iv) Symbols ( ! + - = ? # % * @ & ^ $ _ )

    1. A POOR Password is defined as: 
    a. Contains less than 3 from the above 4 items ( i – iv ).  
    b. Less than 8 characters in length.

    2. A MODERATE Password is defined as:  
    a. Contains 3 from the above 4 items ( i – iv )  
    b. Between 8 to 10 characters in length.

    3. A STRONG Password is defined as:  
    a. Meets all 4 of the above items ( i – iv )  
    b. Greater than 10 characters in length.

    Returns: rank -> rank of password; POOR / MODERATE / STRONG
    '''
    ## Start code here
    def has_lowercase(pwd) -> bool:
        return True if any(char.islower() for char in pwd) else False
    

    def has_uppercase(pwd) -> bool:
        return True if any(char.isupper() for char in pwd) else False

    def has_chars(pwd) -> bool:
        symbols = '! + _ = ? # % * @ & _ ^ $'. split('')
        return True if any(char in symbols for char in pwd) else False

    def has_nums(pwd) -> bool:
        return True if any(char.isdigit() for char in pwd) else False


    if has_lowercase(pwd) and has_uppercase(pwd) and has_chars(pwd) and has_nums(pwd) and len(pwd) > 10:
        return 'STRONG'
    if (has_chars(pwd) + has_lowercase(pwd) + has_nums(pwd) + has_uppercase(pwd)) >= 3 and len(pwd) >= 8:
        return "MODERATE"
    else:
        return "POOR"
    return 'ERROR RATING PASSWORD'

def write_file(checked_file , line: tuple):
   
    try:
        checked_file.write(','.join(line))
        checked_file.write('\n')
    except IOError:
        print('IOError occured, restarting the program...')
        pass




def option1():
    '''
    Helper function that will be executed when user selects option 1 in the initial case.
    '''
    # Steps to follow:
    # 1. Ask user to rank password from either Users-Pwds.txt or a custom file (second part for bonus only you can skip this)
    # 2. Open the file containing username and password in each line and a file to store the ranked password information(Users-Pwds-Chked.txt).
    # 2.1 ## !IMPORTANT ## Store the list of username,passwords in a variable called usrpwds. 
    # 3. Use the rank() function to rank the password
    # 4. Write to the Users-Pwds-Chked.txt file (username,password,rank) in each line as string. Omit the brackets and only fill up the actual values. 
    # 5. Close necessary files and print to terminal.
    
    ## START CODE HERE
    print('-'*80)
    print('Please select one of 2 options')
    print('option 1. rank passwords from Users-Pwds(200).txt \t option 2. rank passwords from Users-Pwds(10).txt \noption 3. Enter your own path')

    option = input('Enter your option: ')
    option = check_int_type(option)


    if option == 1:
        checked = open(os.path.join(dirname,r'C:\Users\Hp\Desktop\TWL_DRCFS_30DaysPythonBootcamp\Week 2\Assignments\Users-Pwds(10).txt'),'w')
        usrpwds = open(os.path.join(dirname,r'C:\Users\Hp\Desktop\TWL_DRCFS_30DaysPythonBootcamp\Week 2\Assignments\Users-Pwds(200).txt'),'r').read().split()

        for userpwd in usrpwds:
            username, password = userpwd.split(',')
            strength = rank(password) # give rank to the current password

            line = (username,password,strength)
            write_file(checked, line) # use helper function to write the line in given file

        checked.close()
        print('#'*80)
        print('[INFO] '+'Number of passwords checked:',str(len(usrpwds)))
        print('[INFO] '+'The given rankings can be found in Users-Pwds-Chked.txt')
        print('#'*80)


    elif option == 2:
            checked = open(os.path.join(dirname,r'C:\Users\Hp\Desktop\TWL_DRCFS_30DaysPythonBootcamp\Week 2\Assignments\Users-Pwds(10).txt'),'w')
            usrpwds = open(os.path.join(dirname,r'C:\Users\Hp\Desktop\TWL_DRCFS_30DaysPythonBootcamp\Week 2\Assignments\Users-Pwds(200).txt'),'r').read().split()
            for userpwd in usrpwds:
                username, password = userpwd.split(',')
                strength = rank(password)

                line = (username,password,strength)
                write_file(checked, line)
        
            checked.close()
            print('#'*80)
            print('[INFO] '+'Number of passwords checked:',str(len(usrpwds)))
            print('[INFO] '+'The given rankings can be found in Users-Pwds-Chked.txt')
            print('#'*80)

    elif option == 3:
            path = input("Enter your absolute (not relative) filepath: ")
            if path[-3:].upper() == 'TXT':
                try:
                    usrpwds = open(path,'r').read().split()
                    checked = open(os.path.join(dirname,'Users-Pwds-Chked.txt'),'w')
                    for userpwd in usrpwds:
                        username, password = userpwd.split(',')
                        strength = rank(password)

                        line = (username,password,strength)
                        write_file(checked, line)
                    checked.close()
                    print('#'*80)
                    print('[INFO] '+'Number of passwords checked:',str(len(usrpwds)))
                    print('[INFO] '+'The given rankings can be found in Users-Pwds-Chked.txt')
                    print('#'*80)
                except FileNotFoundError:
                    print('\n'+'*'*80)
                    print("Sorry we couldnot find your file in the given path:")
                    print(path + 'IS INVALID, restarting the program...')
                    print('#'*80+ '\n')
            else:
                try:
                    path = path+'.txt'
                    usrpwds = open(path,'r').read().split()
                    checked = open(os.path.join(dirname,'Users-Pwds-Chked.txt'),'w')
                    for userpwd in usrpwds:
                        username, password = userpwd.split(',')
                        strength = rank(password)

                        line = (username,password,strength)
                        write_file(checked, line)
                    checked.close()
                    print('#'*80)
                    print('[INFO] '+'Number of passwords checked:',str(len(usrpwds)))
                    print('[INFO] '+'The given rankings can be found in Users-Pwds-Chked.txt')
                    print('#'*80)
                except FileNotFoundError:
                    print('\n'+'#'*80)
                    print("Sorry we couldnot find your file in the given path:")
                    print(path + 'IS INVALID, restarting the program...')
                    print('#'*80+ '\n')

    else:
            print('Please choose between 1 and 3')


       
    ## END CODE HERE

    

    
def option2():
    '''
    Function to be executed when the user selects option 2 (generate password) in the main loop.
    
    Steps to follow:
        Prompt the user for a username (No more the 20 characters in length).
        Create a Function that will have no (zero) arguments. (generate)
        The Function will randomly generate a STRONG password (Meeting the STRONG Requirments).
        Ask the user if they would like this saved (Y or N).
        If Y: Open the Input file (Users-Pwds.txt) and append the username,password to the EOF.
        If N: Ask if they would like to generate a different password for this user (Y or N).
        Then the program loops back to the menu again offering displaying and offering to select 1, 2 or 3.
    '''

    def gen_pass() -> str:
        '''
        Helper function to generate password.
        Returns: A string pwd with strong ranking in our ranking system.
        '''
        # Starter code, Ualphabets contains all upper case alphabets
        # Lalphabets condains all lowercase alphabets
        # chars contains all special characters and digits contains all numeric digits
        Ualphabets = string.ascii_uppercase
        Lalphabets = string.ascii_lowercase
        chars = string.punctuation
        digits = string.digits
        pwd = ''
        while True:
            pwd+=random.choice(Ualphabets)
            pwd+=random.choice(Lalphabets)
            pwd+=random.choice(chars)
            pwd+=random.choice(digits)
            if rank(pwd) == "STRONG":
                break
        return pwd
        # Hint: user random.choice to select a random Upperalphabet(Ualphabet), Lalphabet, chars, and digits. Join then all together in pwd and check ranking
        # While the required ranking is not met continue joining new Ualphabet, Lalphabet, chars and digits.
        
        ## START CODE HERE
    username = input("Enter your username: ")
    if len(username) > 20:
        print("username length is more than 20, please re enter it")
        option2()
    else:
        pass
    password = gen_pass()
    print('#'*80)
    print('[Username]: '+ username)
    print('[Password]: '+ password)
    print('#'*80)

    print('Do you want to save the password?')
    answer = input("please return Y to save and N to not save: ").upper()

    if answer == 'Y':
        print('Do you want to save the password in your custom file location?')
        ques = input("please return Y  or N: ").upper()
        if ques == "Y":
            path = input('Enter your absolute path here: ') 
            if path[-3:].upper() == 'TXT':
                try:
                    f = open(path,'a')
                    write_file(f, (username,password))
                    f.close()
                except Exception as e:
                    print('\n'+'*'*80)
                    print('Exception:' + str(e))
                    print("Invalid file path, please enter a valid file path")
                    print('*'*80+'\n')
            else:
                try:
                    path = path+'.txt'
                    f = open(path,'a')
                    write_file(f, (username,password))
                    f.close()
                except Exception as e:
                    print('\n'+'*'*80)
                    print('Exception:' + str(e))
                    print("Invalid file path, please enter a valid file path")
                    print('*'*80+'\n')

        else:
            # write to the file as suggested in the question prompt
            print('-'*10 + 'SAVING USERNAME AND PASSWORD in Users-Pwds.txt' + '-' * 10)
            f = open(os.path.join(dirname,'Users-Pwds.txt'),'a')
            write_file(f,(username,password))
            f.close()
            
    elif answer == 'N':
        print('-'*10 + 'Would you like to generate a new password?' + '-' * 10)
        answer = input("please return Y or N : ").upper()
        if answer == "Y":
            option2()
        else:
            print('-'*10 + 'Restarting the program...' + '-' * 10)

            pass 
    else: 
        print('Either choose Y or N, restarting the program...')

def check_int_type(inp):
    try:
        inp = int(inp)
        return inp
    except Exception as exception:
        print('\n'+'*'*80)
        print('Exception:' + str(exception))
        print("Invalid option, please only enter the number of option and omit other details. Restarting the program....")
        print('#'*80+'\n')    

def main():

    print('Welcome to my password ranking program')
    while True:
        print('-'*40)
        print('Please select one of 3 options')
        print('option1. Rank password from an existing file \t option2. Generate a strong password \noption3. exit the program')
        inp = input("Enter your option here:")
        
        # try converting the inp to integer form and then check condition if input was either option1, 2, 3 or something else. 
        # exit the loop by using the break command if the user selects 3 other wise use option1() and option 2() function 

        ## START CODE HERE
        if inp == 1:
            option1()
        elif inp == 2:
            option2()
        elif inp ==3:
            print('-'*45)
            print('Closing the program \nThis program was built by: Ashim Dahal')
            break
        else:
            print("Please choose a number between 1 and 3.")

        ## END CODE HERE


# DONOT TOUCH THESE LINES
if __name__=='__main__':
    main()