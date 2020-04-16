import guessing_game
import hangman_game

def which_game():
    print("********************************")
    print("       CHOOSE YOUR GAME         ")
    print("********************************")
    print()

    print("(1) guessing game (2) hangman game")
    print()


    game = int(input('Which game: '))

    if game == 1:
        print('playing guessing game')
        guessing_game.play()
    elif game == 2:
        print('playing hangman game')
        hangman_game.play()

if __name__ == "__main__":
    which_game()