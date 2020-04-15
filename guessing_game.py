print("********************************")
print("  WELCOME TO THE GUESSING GAME! ")
print("********************************")
print()

secret_number = 42
attempts = 3



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
        print(f'You won!')
        break
    else:
        if bigger:
            print('Your shot is bigger than the secret number')
        elif smaller:
            print('Your shot is smaller than secret number')
  

print('End of the game')