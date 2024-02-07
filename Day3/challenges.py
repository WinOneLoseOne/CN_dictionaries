#challenge 1

#using this list, write a program that checks each item and states if it is a truthy or falsy value


# truthy_or_falsy = [0, "Hello", "", "!!", 12, True, None, "", "0", False, "False"]

# for i in truthy_or_falsy:
#     print (bool(i))

#challenge 2

# Create two lists of names; a guest list and a barred list.
# Create a function which takes a guest’s name.
# If the name appears on the guest list, let the user know
# they can enter.
# If the name doesn’t appear on the guest list, let the
# user know they must wait.
# If the name appears on the barred list, the guest must
# get turned away.
    
# guest_list = ["sophia", "olivia", "emma", "jackson", "isabella", "lucas"]

# banned_list = ["ava", "aiden"]

# while True:
#     enter_name = input("Type your name here: ").lower()
#     if enter_name in guest_list:
#         print("You can come in")
#     elif enter_name in banned_list:
#         print("You shall not pass")
#     else:
#         end = input("You have to wait, would you like to enter another name? (y/n)" )
#         if end != "y":
#             break

# Challenge 3
# Create a cash machine function (or functions!).
# The user must enter a correct pin and have enough
# funds to be allowed to withdraw an amount.
# Be creative.
# Once you have this functionality, expand!
# You could include more options, add a limit to the
# number of times the user can guess their pin, and more!
        
pin = 1234
balance = 1000
pin_attempts = 3

def my_pin():
    return int(input("Enter a pin: "))

def withdraw_amount():
    return int(input("How much would you like to withdraw?: "))

while pin_attempts != 0:
    entered_pin = my_pin()
    if entered_pin == pin:
        withdrawal_amount = withdraw_amount()
        if withdrawal_amount <= balance:
            balance -= withdrawal_amount
            print(f"Withdrawal successful! Your new balance is {balance}")
        else:
            print("Insufficient funds!")
    else:
        print("Wrong pin, try again.")
        pin_attempts -= 1

    if pin_attempts == 0:
        print("You've exceeded the maximum number of attempts.")

