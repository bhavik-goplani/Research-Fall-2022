# Rock paper Scissor game with programmed probabilities

import time
import random

def rps(prob_rock, prob_paper, prob_scissor, user_input):
    # The mapping between moves and numbers
    game_map = {0:"rock", 1:"paper", 2:"scissor"}
 
    # Win-lose matrix for traditional game
    rps_table = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]

    if user_input == 'rock': player_move = 0
    if user_input == 'paper': player_move = 1
    if user_input == 'scissor': player_move = 2

    print('Computer is making a move...')
    time.sleep(3)

    comp_move = float(random.randint(1,100)/100)
    if 1 <= comp_move <= prob_rock:
        comp_move = 0
    elif prob_rock < comp_move <= prob_paper + prob_rock:
        comp_move = 1
    elif prob_paper + prob_rock < comp_move <= prob_scissor +prob_paper + prob_rock:
        comp_move = 2

# Print the computer move
    print("Computer chooses ", game_map[comp_move].upper())

    # Find the winner of the match
    winner = rps_table[player_move][comp_move]

    if winner == player_move:
        print('\tYou WIN!!!')
    elif winner == comp_move:
        print('\tComputer WINS!!!')
    else:
        print('\tTie Game')
    
    time.sleep(2)

def main():

    while True:
        print("\n\nSelect an option: ")
        print('Here are your choices (default probabilities are 0.33 for each and enter probabilities between 0 and 1 upto 2 decimal places)\n\n 1. Change the probability of getting a rock\n 2. Change the probability of getting a paper\n 3. Change the probability of getting a scissor\n 4. Enter your choice (rock/paper/scissor)\n 5. Exit\n')
        choice = input('Enter your choice (e.g. 1/2/3): ')
        prob_rock = 0.33
        prob_paper = 0.33
        prob_scissor = 0.33

        if choice == '1':
            try:
                prob_rock = float(input('Enter input for probability of getting a rock: '))
                if 0 <= prob_rock <= 1:
                    pass
                else:
                    raise Exception
            except:
                print('Probability not within the specified range. Range is 0 to 1.')

        elif choice == '2':
            try:
                prob_paper = float(input('Enter input for probability of getting a paper: '))
                if 0 <= prob_paper <= 1:
                    pass
                else:
                    raise Exception
            except:
                print('Probability not within the specified range. Range is 0 to 1.')

        elif choice == '3':
            try:
                prob_scissor = float(input('Enter input for probability of gettng a scissor: '))
                if 0 <= prob_scissor <= 1:
                    pass
                else:
                    raise Exception
            except:
                print('Probability not within the specified range. Range is 0 to 1.')

        elif choice == '4':
            try:
                user_input = input('Enter your input (Rock, Paper, Scissor): ')
                user_input.lower()
                if user_input != 'rock' and user_input != 'paper' and user_input != 'scissor':
                    raise Exception
            except:
                print(f'{user_input} is not Rock/Paper/Scissor') 

        elif choice == '5':
            print('Exiting...')
            break

        else:
            print('Invalid input')

        rps(prob_rock, prob_paper, prob_scissor, user_input)          


if __name__ == '__main__':
    main()
