# register
# - first name, last name, password, email
# - generate user account


# login
# - account number & password


# bank operations

# Initializing the system
import random

database = {9904416501: ['timphemhyjose@gmail.com', 'Femi', 'Ogunsola', 'goal', '1200'],
            9055442034: ['freddie@gmail.com', 'Amos', 'Adekunle', 'food', '5000']}


def init():
    print("Welcome to The Bank of Manchester")

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:
        login()

    elif have_account == 2:
        register()

    else:
        print("You have selected invalid option")
        init()


def login():
    print("********* Login ***********")

    account_number_from_user = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber, userDetails in database.items():
        if accountNumber == account_number_from_user:
            if userDetails[3] == password:
                bank_operation(userDetails)

            else:
                print('Invalid account or password')
                login()


def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")

    account_number = generation_account_number()

    database[account_number] = [first_name, last_name, email, password]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % account_number)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()


def bank_operation(user):
    print("Welcome %s %s " % (user[1], user[2]))

    selected_option = int(input("What would you like to do?\n 1) deposit\n 2) withdrawal\n 3) Logout\n 4) Exit\n"))

    if selected_option == 1:
        deposit_operation(user)

    elif selected_option == 2:
        withdrawal_operation(user)

    elif selected_option == 3:
        logout(user)

    elif selected_option == 4:
        exit()
    else:
        print("Invalid option selected")
        bank_operation(user)


def withdrawal_operation(user):
    print("Withdrawal Operations")
    print(f"Your current balance is ${user[4]}")
    avail_bal = int(user[4])
    msg = int(input('How much would you like to withdraw?\n'))
    new_bal = avail_bal - msg
    if msg <= avail_bal:
        print('Please take your cash')
        print(f'${new_bal}')
        logout(user)
    else:
        print('insufficient funds')
        logout(user)


def deposit_operation(user):
    print("Deposit Operations")
    print(f"Your current balance is ${user[4]}")
    msg = int(input("How much do you want to deposit?\n"))
    avail_bal = int(user[4])
    curr_bal = avail_bal + msg
    print(f'You deposited ${msg}')
    print(f'Your current balance is ${curr_bal}')
    logout(user)


def generation_account_number():
    return random.randrange(0000000000, 9999999999)


def logout(user):
    msg = input("Do you want to perform another transaction? "
                "Input y/n \n")
    if msg == 'y':
        bank_operation(user)
    else:
        exit()

init()
