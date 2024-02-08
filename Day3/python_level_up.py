#write a function which allows a user to input two integers
#generate 6 random numbers between these values and sorts them in order of highest to lowest
#print

# import random

# integer_1 = int(input("Enter your first integer: "))
# integer_2 = int(input("Enter your second integer: "))

# num_range = range(integer_1, integer_2)

# for i in num_range:
#     num_range2 = random.randint(integer_1, integer_2)
#     print(num_range2)

# dinosaurs = [
#     "Triceratops",
#     "Velociraptor",
#     "Ankylosaurus",
#     "Archaeopteryz",
#     "Tyrannosaurus Rex",
#     "Stegosaurus",
#     "Iguanodon"
# ]

# saurus_dinosaurs = []

# for i in dinosaurs:
#     if "saurus" in i:
#         saurus_dinosaurs.append(i)

# print(saurus_dinosaurs)

# saurus_dinosaurs=[i for i in dinosaurs if "saurus" in i]
# print (saurus_dinosaurs)

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
    
guest_list = ["sophia", "olivia", "emma", "jackson", "isabella", "lucas", "josh"]

banned_list = ["ava", "aiden", "matan"]

while True:
    enter_name = input("Type your name here: ").lower()
    if enter_name in guest_list:
        print("You can come in")
    elif enter_name in banned_list:
        print("You shall not pass")
    else:
        end = input("You have to wait, would you like to enter another name? (y/n)" )
        if end != "y":
            break




