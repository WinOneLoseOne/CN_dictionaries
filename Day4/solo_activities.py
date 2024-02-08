#challenge 1
# import random

# lottery_num = []

# while len(lottery_num) < 6:
#     random_number = random.randint(1, 50)
#     if random_number not in lottery_num:
#         lottery_num.append(random_number)

# print (lottery_num)

#challenge 2
import random
while True:
    random_number = random.randint(1, 100)
    print(random_number)
    user_guess = input("Do you think the next will be higher or lower?: ")
    random_number2 = random.randint(1, 100)

    if random_number < random_number2 and user_guess == "higher":
        print(f"The second number was {random_number2}. You got it right!")
    elif random_number > random_number2 and user_guess == "lower":
        print(f"The second number was {random_number2}. You got it right!")
    else:
        print(f"The second number was {random_number2}. You got it wrong!")
    end_game = input("Do you want to play again? y/n: ")
    if end_game != "y":
        break

#challenge 3

fav_films=["jurrasic park"
           "shrek"
           "spiderman"]
