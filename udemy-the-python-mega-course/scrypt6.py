password=''
while password != 'python123':
    password = input("Enter you password: ")
    if password == 'python123':
        print("You're logged in!")
    else:
        print("Sorry, try again")
