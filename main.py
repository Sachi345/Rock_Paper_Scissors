import random

my_choice = ''
com_choice = []

com_choice = random.choice(['r', 'p', 's'])
my_choice = input("choice from 'r', 'p', or 's' : ")

if (com_choice == 'r' and my_choice == 'p') or (com_choice == 'r' and my_choice == 's') \
        or (com_choice == 'p' and my_choice == 's'):
    print(f'you win because {my_choice} beats {com_choice}')
elif my_choice == com_choice:
    print('it\'s a tie')
else:
    print(f'you lose because {com_choice} beats {my_choice}')

