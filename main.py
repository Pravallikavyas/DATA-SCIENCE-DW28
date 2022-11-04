# A python program for the user to login,register and display password
import re
# Opening a new file to store user credentials
fp = open("usercredentials.txt", "a")
# A function to create a new user account by providing mail-id and password details
def userregistration():
    print("REGISTRATION")
    # Prompting the user to enter the mail-id
    user_name = input("Enter username/mailid:")
    # Regular expression to validate mail-id
    pattern = "^[a-z]+[\.]?[a-z 0-9]+[@][a-z]+[.][a-z]{2,3}$"
    # Validating the user mail-id
    while not (re.search(pattern, user_name)):
        print("Invalid username")
        user_name = input("Enter username/mailid:")
        pattern = "^[a-z]+[\.]?[a-z 0-9]+[@][a-z]+[.][a-z]{2,3}$"
        # If the maild-id is valid then it prints valid username or else it prompts again to register mail-id
        if re.search(pattern, user_name):
            break
    print("Valid username")
    # Prompting the user to set password
    pass_word = input("Enter your password:")
    # Regular expression to validate password
    passpattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$"
    # Validating user password
    while not (re.search(passpattern, pass_word)):
        # If the user sets wrong password then the instructions for the password will be displayed
        print("Password invalid !!.Your password should contain atleast one uppercase letter,one lowercase letter,one digit,one special character and the password length should be in between 5 to 16 characters.")
        # Prompting the user to enter the password
        pass_word = input("Enter your password:")
        # If the password is valid then it prints valid password or else it prompts again to set password
        if re.search(passpattern, pass_word):
            break
    # Writing the user credentials to the file
    fp.write("\n"+user_name+","+pass_word)
    print("Password is valid.")
    # Closing the file
    fp.close()
# A function for the user to login if the user credentials are correct
def userlogin():
    # Opening the file in read mode to read the values of user credentials
    fp = open("usercredentials.txt", "r")
    print("LOGIN")
    # Prompting the user to enter user credentials
    user_login = input("Enter your username/mailid:")
    password_login = input("Enter your password:")
    # Reading the values in file using file pointer
    for line in fp:
        line_strip = line.strip()
        line_split = line_strip.split(",")
        # Variables to store the values from the file
        user2 = line_split[0]
        pass2 = line_split[1]
        # Checks if the user given details are matched with the data in the file.If the details are matched then it displays login success
        if((user_login==user2) and (password_login==pass2)):
            print("login success")
            return
    print("No user exists.Register again")
    # If login is not success then the user must register
    userregistration()
    # Closing the file
    fp.close()
    # A function to display user original password
def forgotpassword( ):
    print("Enter the username to get your password")
    # Opening the file in read mode to read the values of user credentials
    fp = open("usercredentials.txt", "r")
    # Prompting the user to enter mail-id
    login_check = input("\nEnter your username/mailid:")
    # Reading the values in file using file pointer
    for line in fp:
        line_strip = line.strip()
        line_split = line_strip.split(",")
        # Variables to store the values from the file
        u2=line_split[0]
        p2=line_split[1]
        # If the user entered mail-id matches with the value in file then the password will be displayed
        if(login_check==u2):
            print("The password for "+u2+" is "+p2)
            return
    # If the mail id is not matched then there is no user registered.
    print("The user is not registered.Please register")
    userregistration()
    # Closing the file
    fp.close( )
# Asking the choice from the user to ask whether the user wants to register,login or wants to see the user password.
choice = int(input("Enter your choice: "))
match choice:
    case 1:
        userregistration( )
    case 2:
        userlogin( )
    case 3:
        forgotpassword( )