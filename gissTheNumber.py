import random
import sys

user_name = input('Type your name please: ')
min_num = 0
max_num = 30
random_num = random.randint(min_num, max_num) 
play = True
guess= 0
times= 0

# create and write to a new file.
def print_the_result (user_name: str, times: int):
    fh = open(f'files/{user_name}_result.txt', 'w')
    fh.write(f'yaaaay, GOD JOB {user_name} you did it after {times} tries!.')
    fh.close()

# read the file and get the high score
def get_high_score():
    high_score= 0
    high_score_file= open('high_score.txt','r')
    high_score = int(high_score_file.read())
    '''Return the high score to use it for check'''
    return high_score

# write the new score to the file
def save_high_score(score: int):
    # Write to the file
    high_score_file = open("high_score.txt", "w")
    high_score_file.write(str(score))
    high_score_file.close()

while play and __name__ == "__main__":
    try:
        while guess != random_num:
            guess= (input(f'Hello {user_name} Guess a number between {min_num} and {max_num}: '))
            stop=str(guess)
            # to stop the game.
            if guess == 'Q' or guess == 'q': 
                play= False
                break
            # check the numbers.
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
            # if the user guess the right number.  
            else:
                print(f'yaaaay, GOD JOB {user_name} you did it after {times} times.')
                high_score = get_high_score()
                if high_score > times:
                    save_high_score(times)
            # create a file function.
                print_the_result(user_name,times )
                play_again = input(f'{user_name} do yo want to play again?')
                if play_again.lower() == "n":
                    play= False
                    break
                elif play_again.lower() == 'y':
                    times= 0
                    guess= 0
                    random_num = random.randint(min_num, max_num) 
                    play= True
                elif play_again != 'y' or play_again != 'n':
                    print('You are just allowed to answer with y or n.')
                    play_again = input(f'{user_name} do yo want to play again?')
    except:
         '''if the user answer whit non numeric answer'''
         print("You are just allowed to add numbers here, Thanks :)")            