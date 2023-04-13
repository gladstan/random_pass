
user_create = input("Hi do you want to view or create a password ")

def view():
    with open('passwords.txt', 'r') as f:
        for i in f:
            da = i.rstrip()
            vw = da.strip()
            print(vw)

def create():
    name = input("Enter Your name ")
    password = input("Enter your password ")
    if type(password) != str:
        print("The password must be string")
    elif len(password) >= 4:
        print("THE PASSWORD MUST BE 4 CHARACTERS")
    with open('passwords.txt', 'a') as new:
        new.write(name+' '+password)

while True:
    if user_create == "create":
        create()
        break
    if user_create == "view":
        view()
        break


