import random


def new_game():
    """Text for new game."""
    txt = """
-------------------------
    Guess the number!
-------------------------
        
Hint - 'h'
Exit - 'x'

You are guessing number between 1 and 100. Try your best!
-------------------------
"""
    print(txt)


def guess_me():
    """Return guessed number from user or h/x/y/n."""
    guess = input('Your guess: ')
    return guess


def get_number(a=1, b=100):
    """Return random number from a to b."""
    return random.randint(a, b)


def num_len(number=None):
    """Get hint what is length of number."""
    print(f'Number has {len(str(number))} digits.')


def divisible_by(number=None):
    """Get hint about numbers divisibility."""
    hint = []
    divider = number if number < 10 else (number//2 + 1)

    for i in range(1, divider):
        if number % i == 0:
            hint.append(str(i))
    if len(hint) == '1':
        print(f'Number is prime number.')
    else:
        print(f"Number is divisible by {', '.join(hint)}.")


def get_hint(number):
    """Return randomly chosen hint."""
    hint_list = [num_len, divisible_by]
    return random.choice(hint_list)(number)


def main():
    """Function for main game."""
    new_game()
    game_is_running = True

    while game_is_running:
        not_guessed = True
        number = get_number()
        incorrect_counter = 1
        while not_guessed:
            guess = guess_me()
            if guess.isdigit() or guess in 'hxyn':
                print(number, guess)
                if guess == 'x':
                    print('Bye.')
                    game_is_running = False
                    not_guessed = False
                elif guess == 'h':
                    get_hint(number)
                elif guess in 'yn':
                    print(f"Incorrect input! Give me number or 'x' for exit and 'h' for hint.")
                elif number == int(guess):
                    print(f'You won! Number of attempts: {incorrect_counter}')
                    what_next = input("New game? y/n\n")
                    if what_next != 'n':
                        new_game()
                        break
                    else:
                        print('Bye.')
                        game_is_running = False
                        not_guessed = False
                elif number < int(guess):
                    print("Incorrect! Try lower number.")
                    incorrect_counter += 1
                elif number > int(guess):
                    print("Incorrect! Try higher number.")
                    incorrect_counter += 1

            else:
                print(f"Incorrect input! Give me number or 'x' for exit and 'h' for hint.")
            print()


if __name__ == '__main__':
    main()
