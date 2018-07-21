'''In this game, user has to guess a number between 1 to 100 in 5 chances. The number generating machine takes 2 sec to generate the number and then there is the NUMBER. Now, user starts guessing it and the helper comments on the difference in guessed and actual numbers and thus, helping the player to guess the number.'''  

from time import sleep
import random
theNumber = random.randint(0,100)

print('\nInstructions:\n1)The guessed number must be between 1 to 100.\n2)You have 5 lives to guess the correct number.\n3)Helper will help by using comments like very high, high.\n4)If you want to quit type EXIT.')

start_key = input('\n\n Press ENTER to START.')
print('\nWAIT.. Machine is generating number....')
sleep(2)
last_guessed = '--'
lives = 5
while True:
    if not lives:
        print('\nLOSER\n')
        break
    print('\nLast Guessed Number: '+last_guessed+'   '+'|'*30+'   Lives: '+str(lives))
    last_guessed = input('\nGuess the number!\n')
    if last_guessed == 'EXIT': break
    lives-=1
    print('\nHelper:')
    difference = abs(theNumber - int(last_guessed))
    if difference > 40: print("\nSeems like you're on opposite shore. Man sail as fast as possible! ")
    elif difference > 20: print('\nYou are far away from the target!')
    elif difference > 10: print('\nYou can reach the shore be motivated.')
    elif difference > 5: print('\nYes! You are almost closer to WIN the game.')
    elif difference > 0: print('\nYou Are Almost There!')
    else:
        print('\nWINNER\n')
        break
