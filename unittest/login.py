import re

emailSyntax = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
passwordSpec = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'] 

def email(n):
    #username can only be 50 characters long
    if len(n)>50:
        print("too long")
        return False
    else:
        #checks to see if email has correct syntax
        if re.search(emailSyntax,n):
            print("valid email")
            return True
        else:
            print("invalid email")
            return False

def password(n):
    if len(n)<6:
        print("too short")
        return False
    elif len(n)>25:
        print("too long")
        return False
    else:
        if not any(char in passwordSpec for char in n):
            print("password needs atleast one special character")
            return False
        else:
            print("valid email")
            return True




email('bob@123.com')
email('bob.com')
email('bob@y.com')

password('11111111111111111111111111111')
password('password')
password('password%')
