import random
import string


users = list()
credentials = list()

"""
declared two empty lists to store data
"""

class Credentials:
    
    def __init__(self, account_name, username, password):
        self.account_name = account_name
        self.username = username
        self.password = password

        """
        Created the class credentials and initialized using the self keyword
        """
    def my_credentials():
        print("Choose one of the following options to continue")
        print("\n1. Create new credentials \n2. Store credentials of existing accounts \n3. View existing credentials \n4. Logout")
        credentials_option = input()
        if credentials_option == "1":
            print("Do you want a system generated password?")
            option = input("\n1. Yes \n2. No")
            if option == "1":
                pwd =Users.random_password(10)
                acc
        
            elif option == "2":
                account1 = Credentials(account_name = input("Account Name (e.g. Twitter): "), username = input("Username: "), password = input("Password: "))
                credentials.append(account1)
               
                Users.view_credentials()
                Users.delete()
            else:
                print("Invalid input")
                Credentials.my_credentials()

        elif credentials_option == "2":
            account1 = Credentials(account_name = input("Account Name (e.g. Twitter): "), username = input("Username: "), password = input("Password: "))
            credentials.append(account1)
            Users.view_credentials()
            Users.delete()                  
            
        elif credentials_option == "3":
            Users.view_credentials()


class Users:

    def __init__(self, username, password):

        self.username = username
        self.password = password

        """
        Created class users and initialized using the self keyword
        """

    def login():
        print("Put your credentials to login")
        username = input("Username: ")
        password = input("Password: ")

        for x in users:
            if x.username == username and x.password == password:
                print("Login successful")
                Credentials.my_credentials()
            else:
                pass    

    def view_credentials():
        print("choose one of the options below to view your credentials:")
        print("\n1. Yes \n2. No")
        viewers_choice = input()
        if viewers_choice == "1":
            for x in credentials:
                print("Account: " + x.account_name,"Username: " + x.username,"Password: " + x.password)
        elif viewers_choice == "2":
            print("Thanks for checking")
            Users.login()
        else:
            print("invalid choice")

    def delete():
        print("Do you want to delete credentials?")
        print("\n1. Yes \n2. No")
        delete_option = input()
        if delete_option == "1":
            credentials.clear()
            print("You have deleted credentials from the list")
        elif delete_option == "2":
            print("your details are still stored in the application")
        else:
            print("Invalid input.")
            delete() 

    def passwordGenerate(stringLength=8):
        """
        method that generate a random password
        """
        password = string.ascii_lowercase + string.ascii_uppercase + "~!@#$%;:^&*"
        return ''.join(random.choice(password) for i in range(int(stringLength)))     
                