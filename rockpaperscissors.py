import random

print('ROCK, PAPER, SCISSORS')
wins = 0
losses = 0
ties = 0

pattern_to_win = {'p':'r', 'r':'s', 's':'p'}



while True:
    player_choice = input('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit: ')
    if player_choice == 'q':
        break
    elif player_choice not in ['r', 'p', 's']:
        print('Please enter a valid move.')
        continue
    else:
        computer_choice = random.choice(['r', 'p', 's'])
        print('Computer chose:', computer_choice)
        if player_choice == computer_choice:
            print('It is a tie!')
            ties += 1
        elif pattern_to_win[player_choice] == computer_choice:
            print('You win!')
            wins += 1
        else:  
            # computer wins
            print('You lose!')
            losses += 1
        print(f'Wins: {wins}, Losses: {losses}, Ties: {ties}')
        continue
print('Goodbye!')