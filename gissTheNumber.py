import random
import sys

user_name = input('Type your name please: ')
max_num = 10
min_num = 0
random_num = random.randint(min_num, max_num) 
play = True
guess= 0
times= 0

def print_the_result (user_name: str, times: int):
    fh = open(f'files/{user_name}_result.txt', 'w')
    fh.write(f'yaaaay, GOD JOB {user_name} you did it after {times} tries!.')
    fh.close()

while play:
    while guess != random_num:
        guess= (input(f'Hello {user_name} Guess a number between {min_num} and {max_num}: '))
        stop=str(guess)
        if guess == 'Q' or guess == 'q':
            play= False
            break
        elif int(guess) > max_num:
            print(f'Sorry, but the max number is {max_num}')
        elif int(guess) < min_num:
            print(f'Sorry, but the min number is {min_num}')
        elif int(guess) > random_num:
            print('Sorry, guess again TOO high. :)')
            times += 1
        elif int(guess) < random_num:
            print('Sorry, guess again TOO low. :)')
            times += 1
        else:
            print(f'yaaaay, GOD JOB {user_name} you did it after {times} times.')
            print_the_result(user_name,times )
            play_again = input(f'{user_name} do yo want to play again?')
            if play_again == "N" or play_again == "n":
                play= False
                break
            if play_again == 'Y' or play_again == 'y':
                times= 0
                guess= 0
                random_num = random.randint(1, 10) 
                play= True
                

