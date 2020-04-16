import random

def play():
    print("********************************")
    print("  WELCOME TO THE GUESSING GAME! ")
    print("********************************")
    print()

    secret_number = random.randrange(1, 101)
    attempts = 3
    points = 1000

    print('------ difficulty level ------')
    print()
    print('(1) Easy (2) Medium (3) Hard')
    print()

    level = int(input('Level: '))


    if level == 1:
        attempts = 20
    elif level == 2:
        attempts = 10
    elif level == 3:
        attempts = 5
    else:
        print('Esta opçãoo não existe')


    for game_round in range(1, attempts + 1):
        print(f'Attempt: {game_round} of {attempts}')
        shot = int(input('Type a number between 1 and 100: '))

        if shot < 1 or shot > 100:
            print('You must be enter a number between 1 and 100!')
            continue

        won = shot == secret_number
        bigger = shot > secret_number
        smaller = shot < secret_number

        
        if won:
            print(f'\o/ You won! and made {points} points... \o/')
            break
        else:
            if bigger:
                print('Your shot is bigger than the secret number')
            elif smaller:
                print('Your shot is smaller than secret number')
            lost_points = abs(secret_number - shot)
            points -= lost_points

    print('End of the game')

if __name__ == "__main__":
     play()