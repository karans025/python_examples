from random import randint
random_variable = randint(1,100)
user_guess = int(input("Please Guess A number: "))
counter = 1
if user_guess == random_variable:
    print(f"CORRECT ANSWER, It took you {counter} turns to get to the correct answer")
elif user_guess < 1 or user_guess > 100:
    print("OUT OF BOUNDS")
elif abs(user_guess - random_variable) <= 10:
    print("WARM")
else:
    print("COLD")
while user_guess != random_variable:
    previous_user_input = user_guess
    user_guess = int(input("Please Guess A number: "))
    counter += 1
    if user_guess == random_variable:
        print(f"CORRECT ANSWER, It took you {counter} turns to get to the correct answer")
        break
    elif user_guess < 1 or user_guess > 100:
        print("OUT OF BOUNDS")
    elif abs(user_guess - random_variable) < abs(previous_user_input - random_variable):
        print("WARMER")
    else:
        print("COLDER")
