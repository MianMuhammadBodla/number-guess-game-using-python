import random

number_to_guess = random.randint(1, 10)  # Random number between 1 and 10
# def get_user_guess():
#     while True:
#         try:
#             guess = int(input("Guess a number between 1 and 10: "))
#             return guess
#         except ValueError:
#             print("That's not a valid number. Please try again.")


# def play_game():
#     while True:
#         guess = get_user_guess()
#         if guess < number_to_guess:
#             print("Too low! Try again.")
#         elif guess > number_to_guess:
#             print("Too high! Try again.")
#         else:
#             print("Congratulations! You guessed the number!")
#             break


# if __name__ == "__main__":
#     print("Welcome to the Number Guessing Game!")
#     play_game()                    