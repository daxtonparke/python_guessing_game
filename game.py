import random
print('welcome')
increment = 0

def logic(rannum,increment):
    guess = raw_input('guess a number between 1-100\n')
    increment += 1
    if type(guess) != int:
        print('please just enter an int')
    elif guess < 0 or guess> 100:
        print('lol enter an int between 1-100')
    elif guess < rannum:
        print('too low')
        logic(rannum,increment)
    elif guess > rannum:
        print('too high')
        logic(rannum,increment)
    else:
        print('spot on')
        print('it only took '+ str(increment) +' guesses')
        
def game():
    global increment
    rannum = random.randint(1,100)
    print(rannum)
    name = raw_input('what is your name? ')
    print('hello '+name+'')
    logic(rannum,increment)
# print('rannum', rannum)
game()