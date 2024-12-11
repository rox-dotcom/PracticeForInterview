#Number Guessing Game
import random

def guesing_num(n, guess):
    if guess > n:
        print('Too High')
        return True 
    elif guess < n:
        print('Too Low')
        return True
    else:
        print('That is the number!')
        return False

def main():
    n = random.randint(1,50)
    steps = 0
    while True:
        try: 
            guess = int (input('Guess the number im thinking '))
            steps += 1  
            if not guesing_num(n,guess):
                print(f'You win! After {steps} attempts')
                
                play_again = input('Want to play again? y/n: ').lower()
                if play_again not in ('yes', 'y'):
                    print('Arrivederchi!!')
                    break

        except ValueError:
            print("Error: invalid data, just use 'int' ")

        
if __name__ == '__main__':
    main()