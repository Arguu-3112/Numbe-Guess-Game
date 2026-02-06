import random

levels = {1: "Easy", 2: "Medium", 3: "Hard"}
chances = {"Easy": 10, "Medium": 5, "Hard": 3}
secret_num = random.randint(1, 100)

print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
      
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
""")
print(secret_num)

def attempt_level(n):
    attempt = 0
    while attempt < n:
        try:
            guess_num = int(input("Enter your guess: "))
        except ValueError:
            print("Enter number only!")
            continue
        attempt += 1
        if guess_num == secret_num:
            print(f"Congratulations! You guessed the correct number in {attempt} attempts.")
            break
        elif guess_num > secret_num:
            print(f"Incorrect! The number is less than {guess_num}.")
        else:
            print(f"Incorrect! The number is greater than {guess_num}.")
    else:
        print("Uh oh.. You ran out of chances.")
        
level = int(input("Enter your choice: "))

if level in levels.keys():
    print(f"""
Great! You have selected the "{levels[level]}" difficulty level that will give you {chances[levels[level]]} chances.
Let's start the game!
""")

attempt_level(chances[levels[level]])