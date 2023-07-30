import random

def display_game():
    print('Lets play ROCK PAPER SCISSORS!')



#Player input for choices rock paper or scissors
def player_choice():
    
    choice = 'wrong'

    while choice not in ['rock','paper','scissors']:

        choice = input('Please choose rock paper or scissors: ')

        if choice not in ['rock','paper','scissors']:
            print('Invalid Choice!')

    return choice

#Randomized bot to choose between rock paper scissors
def bot_choice():
    game_list = ['rock','paper','scissors']

    choice = random.choice(game_list)
    
    return choice

#check choices of player and bot to see who wins
def choice_check(player, bot):
    if player == bot:
        print('Its a tie!')
    elif player == 'rock' and bot == 'scissors':
        print('You Win!')
    elif player == 'paper' and bot == 'rock':
        print('You Win!')
    elif player == 'scissors' and bot == 'paper':
        print('You Win!')
    else: 
        print('Bot Wins :(')

#Choice to quit game
def exit_game():
    choice = 'wrong'

    while choice not in ['y','n']:
        choice = input('Would you like to play again? (y or n): ')

        if choice not in ['y','n']:
            print('Invalid Choice!')

    if choice == 'y':
        return True
    else:
        return False
    
continue_game = True

while continue_game:

    display_game()

    player = player_choice()
    bot = bot_choice()

    print(f'You chose: {player}')
    print(f'The bot chose: {bot}')

    choice_check(player, bot)

    exit_game()

