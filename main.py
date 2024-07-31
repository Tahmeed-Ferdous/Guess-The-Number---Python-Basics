import random
def num_guess():
    inp=input('pl:Player or Cm:Computer (Type: pl/cm): ')
    if inp=='pl':
        print('\nPlayer - 1')
        player1=int(input('Enter a Number (1-10): '))
        print('\n\n\n\n\n\n\n')

    else:
        print('\nComputer')
        print('Try to find my number, muhahaha')
        player1=random.randint(1, 10)
    
    tries, count= 5, 5
    print("\nPlayer - 2")
    print(f'You have {tries} tries')
    print('Guess the number:')
    for i in range(tries):
        player2=int(input('Enter a Number (1-10): '))
        print('\n')
        if player2==player1 and count>0:
            print('---------------------------------------')
            print('Its a match')
            print('Player 2 Wins')
            break
        else:
            count-=1
            if count==0:
                print('---------------------------------------')
                print('You ran out of tries')
                print('The Number was', player1)
                print('Player 1 wins')
            else:
                if count==1:
                    print('Whoops, Try again')
                    print(count, 'Try Left')
                else:
                    print('Whoops, Try again')
                    print(count, 'Tries Left')

def main():
    print('\nWELCOME TO NUMBER GUESSING GAME\n')
    print('Player 1: Types The Number')
    print('Player 2: Guesses The Number\n')
    play=input("\nType 'P' to start the game: ").upper()
    num_guess()
    flag=True
    while flag:
        if play=='P':
            print('---------------------------------------')
            play=input("\n To Play Again:'P'\n To Exit:'E'\nType: ").upper()
            if play=='P':
                num_guess()
            else:
                print('Thanks for playing')
                print('Game Over')
                flag=False
        else:
            print('Game Over')
            print('Thanks for playing')
            flag=False
            
main()


