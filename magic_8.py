import os
import random


def help():
    os.system('cls')
    print('//Help & Instructions:')
    print('Users can ask the Magic 8 Ball any yes-or-no question')
    print('by typing out the question and hitting the (ENTER KEY)')
    print('\nEntering \'Quit\' will exit Magic 8 Ball.')
    print('Entering \'Help\' at any point will result in this screen.')

    print('\n//About Magic 8 Ball')
    print('This is a digital Magic 8-Ball made with Python.')
    print('The orignal Magic 8-Ball was a billard\'s 8-ball used for fortune telling.')
    print('Users would ask a yes/no question and the Magic 8-Ball would give a prediction.')

    input('\nPress (ENTER KEY) to continue. ')

answers = [
    'It is certain',
    'It is decidedly so',
    'Yes',
    'Without a doubt',
    'As I see it, yes',
    'Reply hazy try again',
    'Ask again later',
    'Cannot predict at this time',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not good',
    'Very doubtful',
    'My sources say no',
    'Don\'t count on it'
]

while True:
    os.system('cls')
    print('//THE MAGIC 8-BALL')
    print('Type \'help\' for help or \'quit\' to quit.')
    question = input('\nWhat would you like to ask the Magic 8 Ball?\n> ')
    if question.lower() == 'quit':
        break
    elif question.lower() == 'help':
        help()
        continue
    elif 'meaning of life' in question.lower():
        print('Magic 8 Ball says: "42"')
        input('\nPress (ENTER KEY) to continue. ')
    else:
        print(f'\nMagic 8 Ball says: "{random.choice(answers)}"')
        input('\nPress (ENTER KEY) to continue. ')
