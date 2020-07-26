import random

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


def help():
    print('\n###')
    print('Help/Instructions:\n')
    print('When the program first runs, the Magic 8 Ball will ask the user if')
    print('they would like to ask a yes or no question.')
    print('The user can then enter \'Y\' for yes & proceed to ask a question.')
    print('Or the user can enter \'N\' for no to exit the program.\n')
    print('Entering \'Help\' at any point will result in this screen.')
    print('###')

while True:  # This allows the user to ask again.
    print('\nWould you like to ask the Magic 8 Ball something? ')
    question = input('Enter \'Y\' to ask a question or \'N\' to quit. ')
    if question.lower() == 'y':
        question = input('\nWhat is your question? ')
        if 'meaning of life' in question.lower():
            print('Magic 8 Ball says: "42"')
        elif question.lower() == 'help':
            help()
        else:
            print(f'\n> Magic 8 Ball says: "{random.choice(answers)}"')
    elif question.lower() == 'n':
        break
    elif question.lower() == 'help':
        help()
        continue
    else:
        print(f'\nSorry, I wasn\'t able to understand "{question}".')
        print('Enter \'Help\' for help.')
