# Author: Matheus Reato
# Campinas, São Paulo, Brazil
# December 2023

from random import randint
from time import sleep
from colorama import Fore

# Pair splitting
pair_splitting_table = (
    ('', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'),
    ('AA', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'),
    ('TT', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'),
    ('99', 'S', 'S', 'S', 'S', 'S', 'D', 'S', 'S', 'D', 'D'),
    ('88', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'),
    ('77', 'S', 'S', 'S', 'S', 'S', 'S', 'D', 'D', 'D', 'D'),
    ('66', 'S/D', 'S', 'S', 'S', 'S', 'D', 'D', 'D', 'D', 'D'),
    ('55', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'),
    ('44', 'D', 'D', 'D', 'S/D', 'S/D', 'D', 'D', 'D', 'D', 'D'),
    ('33', 'S/D', 'S/D', 'S', 'S', 'S', 'S', 'D', 'D', 'D','D'),
    ('22', 'S/D', 'S/D', 'S', 'S', 'S', 'S', 'D', 'D', 'D', 'D')
)

# Key for pair splitting
# S = split
# D = don't split
# S/D = split only if "double after split" (DAS) is allowed

# Soft Totals
soft_totals = (
    ('', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'),
    ('A9', 'ST', 'ST', 'ST', 'ST', 'ST', 'ST', 'ST', 'ST', 'ST', 'ST'),
    ('A8', 'ST', 'ST', 'ST', 'ST', 'DS', 'ST', 'ST', 'ST', 'ST', 'ST'),
    ('A7', 'DS', 'DS', 'DS', 'DS', 'DS', 'ST', 'ST', 'H', 'H', 'H'),
    ('A6', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'),
    ('A5', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'),
    ('A4', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'),
    ('A3', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H'),
    ('A2', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H')
)

# Hard Totals
hard_totals = (
    ('', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'),
    ('17', 'ST', 'ST', 'ST', 'ST', 'ST', 'ST', 'ST', 'ST', 'ST', 'ST'),
    ('16', 'ST', 'ST', 'ST', 'ST', 'ST', 'H', 'H', 'H', 'H', 'H'),
    ('15', 'ST', 'ST', 'ST', 'ST', 'ST', 'H', 'H', 'H', 'H', 'H'),
    ('14', 'ST', 'ST', 'ST', 'ST', 'ST', 'H', 'H', 'H', 'H', 'H'),
    ('13', 'ST', 'ST', 'ST', 'ST', 'ST', 'H', 'H', 'H', 'H', 'H'),
    ('12', 'H', 'H', 'ST', 'ST', 'ST', 'H', 'H', 'H', 'H', 'H'),
    ('11', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'),
    ('10', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H', 'H'),
    ('9', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'),
    ('8', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H')
)

# Key for totals (soft and hard)
# H = hit
# ST = stand
# D = double if allowed, else hit
# DS = double if allowed, else stand 

# Simulation
while True:
    # Initializing stats...
    total_rounds = 0
    wins = 0
    losses = 0
    accuracy = 0.0

    # Initializing simulation
    print(f'{Fore.LIGHTBLUE_EX}---------- MENU ----------{Fore.WHITE}')
    print('Welcome!!! Chose a practice mode:')
    sleep(1)
    print('1 - Practice pair splitting')
    sleep(0.2)
    print('2 - Practice soft totals')
    sleep(0.2)
    print('3 - Practice hard totals')
    sleep(0.2)
    print('4 - Practice all')
    sleep(0.2)
    print('5 - Practice pair splitting & soft totals')
    sleep(0.2)
    print('6 - Quit')

    option = int(input('> '))

    # Pair Splitting Practice -----------------------------------------------------------
    if option == 1:
        while True:
            print(f'{Fore.YELLOW}---------- NEW ROUND ----------{Fore.WHITE}')
            sleep(0.2)
            print('Drafting cards...')
            sleep(0.2)

            player_selection = randint(1, 10)    # Adjust these to select which rows to play
            dealer_selection = randint(1, 10)

            player_cards = pair_splitting_table[player_selection][0]
            dealer_upcard = pair_splitting_table[0][dealer_selection]

            print("Player's cards: ", player_cards)
            sleep(0.2)
            print("Dealer's upcard: ", dealer_upcard)
            sleep(0.2)

            response = str(input('Action: ')).upper().rstrip()

            if response == pair_splitting_table[player_selection][dealer_selection]:
                print(f'{Fore.GREEN}Correct!{Fore.WHITE}')
                total_rounds = total_rounds + 1
                wins = wins + 1
                accuracy = wins / total_rounds
                sleep(0.2)

            elif response == 'QUIT':
                print('Printing stats...')
                sleep(1)
                print(f'{Fore.LIGHTMAGENTA_EX}---------- STATISTICS ----------{Fore.WHITE}')
                print('Total rounds: ', total_rounds)
                sleep(0.5)
                print(f'{Fore.LIGHTGREEN_EX}Wins: {Fore.WHITE}', wins)
                sleep(0.5)
                print(f'{Fore.LIGHTRED_EX}Losses: {Fore.WHITE}', losses)
                sleep(0.5)
                print('Accuracy: {:.2f}'.format(accuracy))
                sleep(1.5)
                print('Ending simulation...')
                sleep(1.5)
                break

            else:
                print(f'{Fore.RED}Incorrect...{Fore.WHITE}')
                total_rounds = total_rounds + 1
                losses = losses + 1
                accuracy = wins/total_rounds
                sleep(0.2)
    
    # Soft Totals Practice --------------------------------------------------------------
    elif option == 2:
        while True: 
            print(f'{Fore.CYAN}---------- NEW ROUND ----------{Fore.WHITE}')
            sleep(0.2)
            print('Drafting cards...')
            sleep(0.2)

            player_selection = randint(1, 4)    # Adjust these to select which rows to play
            dealer_selection = randint(1, 10)

            player_cards = soft_totals[player_selection][0]
            dealer_upcard = soft_totals[0][dealer_selection]

            print("Player's cards: ", player_cards)
            sleep(0.2)
            print("Dealer's upcard: ", dealer_upcard)
            sleep(0.2)

            response = str(input('Action: ')).upper().rstrip()

            if response == soft_totals[player_selection][dealer_selection]:
                print(f'{Fore.GREEN}Correct!{Fore.WHITE}')
                total_rounds = total_rounds + 1
                wins = wins + 1
                accuracy = wins / total_rounds
                sleep(0.2)

            elif response == 'QUIT':
                print('Printing stats...')
                sleep(1)
                print(f'{Fore.LIGHTMAGENTA_EX}---------- STATISTICS ----------{Fore.WHITE}')
                print('Total rounds: ', total_rounds)
                sleep(0.5)
                print(f'{Fore.LIGHTGREEN_EX}Wins: {Fore.WHITE}', wins)
                sleep(0.5)
                print(f'{Fore.LIGHTRED_EX}Losses: {Fore.WHITE}', losses)
                sleep(0.5)
                print('Accuracy: {:.2f}'.format(accuracy))
                sleep(1.5)
                print('Ending simulation...')
                sleep(1.5)
                break

            else:
                print(f'{Fore.RED}Incorrect...{Fore.WHITE}')
                total_rounds = total_rounds + 1
                losses = losses + 1
                accuracy = wins/total_rounds
                sleep(0.2)

    # Hard Totals Practice --------------------------------------------------------------
    elif option == 3:
        while True:
            print(f'{Fore.BLUE}---------- NEW ROUND ----------{Fore.WHITE}')
            sleep(0.2)
            print('Drafting cards...')
            sleep(0.2)

            player_selection = randint(1, 10)    # Adjust these to select which rowsto play
            dealer_selection = randint(1, 10)

            player_cards = hard_totals[player_selection][0]
            dealer_upcard = hard_totals[0][dealer_selection]

            print("Player's cards: ", player_cards)
            sleep(0.2)
            print("Dealer's upcard: ", dealer_upcard)
            sleep(0.2)

            response = str(input('Action: ')).upper().rstrip()

            if response == hard_totals[player_selection][dealer_selection]:
                print(f'{Fore.GREEN}Correct!{Fore.WHITE}')
                total_rounds = total_rounds + 1
                wins = wins + 1
                accuracy = wins / total_rounds
                sleep(0.2)

            elif response == 'QUIT':
                print('Printing stats...')
                sleep(1)
                print(f'{Fore.LIGHTMAGENTA_EX}---------- STATISTICS ----------{Fore.WHITE}')
                print('Total rounds: ', total_rounds)
                sleep(0.5)
                print(f'{Fore.LIGHTGREEN_EX}Wins: {Fore.WHITE}', wins)
                sleep(0.5)
                print(f'{Fore.LIGHTRED_EX}Losses: {Fore.WHITE}', losses)
                sleep(0.5)
                print('Accuracy: {:.2f}'.format(accuracy))
                sleep(1.5)
                print('Ending simulation...')
                sleep(1.5)
                break

            else:
                print(f'{Fore.RED}Incorrect...{Fore.WHITE}')
                total_rounds = total_rounds + 1
                losses = losses + 1
                accuracy = wins/total_rounds
                sleep(0.2)

    # Full Practice ---------------------------------------------------------------------
    elif option == 4:
        while True:
            table_selection = randint(1, 3)

            print(f'{Fore.RED}---------- NEW ROUND ----------{Fore.WHITE}')
            sleep(0.2)
            print('Drafting cards...')
            sleep(0.2)

            # Pair splitting ----------------------------------------
            if table_selection == 1:
                player_selection = randint(1, 10)    # Adjust these to select which rows to play
                dealer_selection = randint(1, 10)

                player_cards = pair_splitting_table[player_selection][0]
                dealer_upcard = pair_splitting_table[0][dealer_selection]

                print("Player's cards: ", player_cards)
                sleep(0.2)
                print("Dealer's upcard: ", dealer_upcard)
                sleep(0.2)

                response = str(input('Action: ')).upper().rstrip()

                if response == pair_splitting_table[player_selection][dealer_selection]:
                    print(f'{Fore.GREEN}Correct!{Fore.WHITE}')
                    total_rounds = total_rounds + 1
                    wins = wins + 1
                    accuracy = wins / total_rounds
                    sleep(0.2)

                elif response == 'QUIT':
                    print('Printing stats...')
                    sleep(1)
                    print(f'{Fore.LIGHTMAGENTA_EX}---------- STATISTICS ----------{Fore.WHITE}')
                    print('Total rounds: ', total_rounds)
                    sleep(0.5)
                    print(f'{Fore.LIGHTGREEN_EX}Wins: {Fore.WHITE}', wins)
                    sleep(0.5)
                    print(f'{Fore.LIGHTRED_EX}Losses: {Fore.WHITE}', losses)
                    sleep(0.5)
                    print('Accuracy: {:.2f}'.format(accuracy))
                    sleep(1.5)
                    print('Ending simulation...')
                    sleep(1.5)
                    break

                else:
                    print(f'{Fore.RED}Incorrect...{Fore.WHITE}')
                    total_rounds = total_rounds + 1
                    losses = losses + 1
                    accuracy = wins/total_rounds
                    sleep(0.2)
            
            # Soft Totals -------------------------------------------
            elif table_selection == 2:
                player_selection = randint(1, 8)    # Adjust these to select which rows to play
                dealer_selection = randint(1, 10)

                player_cards = soft_totals[player_selection][0]
                dealer_upcard = soft_totals[0][dealer_selection]

                print("Player's cards: ", player_cards)
                sleep(0.2)
                print("Dealer's upcard: ", dealer_upcard)
                sleep(0.2)

                response = str(input('Action: ')).upper().rstrip()

                if response == soft_totals[player_selection][dealer_selection]:
                    print(f'{Fore.GREEN}Correct!{Fore.WHITE}')
                    total_rounds = total_rounds + 1
                    wins = wins + 1
                    accuracy = wins / total_rounds
                    sleep(0.2)

                elif response == 'QUIT':
                    print('Printing stats...')
                    sleep(1)
                    print(f'{Fore.LIGHTMAGENTA_EX}---------- STATISTICS ----------{Fore.WHITE}')
                    print('Total rounds: ', total_rounds)
                    sleep(0.5)
                    print(f'{Fore.LIGHTGREEN_EX}Wins: {Fore.WHITE}', wins)
                    sleep(0.5)
                    print(f'{Fore.LIGHTRED_EX}Losses: {Fore.WHITE}', losses)
                    sleep(0.5)
                    print('Accuracy: {:.2f}'.format(accuracy))
                    sleep(1.5)
                    print('Ending simulation...')
                    sleep(1.5)
                    break

                else:
                    print(f'{Fore.RED}Incorrect...{Fore.WHITE}')
                    total_rounds = total_rounds + 1
                    losses = losses + 1
                    accuracy = wins/total_rounds
                    sleep(0.2)

            # Hard Totals -------------------------------------------
            else:
                player_selection = randint(1, 10)    # Adjust these to select which ros to play 
                dealer_selection = randint(1, 10)

                player_cards = hard_totals[player_selection][0]
                dealer_upcard = hard_totals[0][dealer_selection]

                print("Player's cards: ", player_cards)
                sleep(0.2)
                print("Dealer's upcard: ", dealer_upcard)
                sleep(0.2)

                response = str(input('Action: ')).upper().rstrip()

                if response == hard_totals[player_selection][dealer_selection]:
                    print(f'{Fore.GREEN}Correct!{Fore.WHITE}')
                    total_rounds = total_rounds + 1
                    wins = wins + 1
                    accuracy = wins / total_rounds
                    sleep(0.2)

                elif response == 'QUIT':
                    print('Printing stats...')
                    sleep(1)
                    print(f'{Fore.LIGHTMAGENTA_EX}---------- STATISTICS ----------{Fore.WHITE}')
                    print('Total rounds: ', total_rounds)
                    sleep(0.5)
                    print(f'{Fore.LIGHTGREEN_EX}Wins: {Fore.WHITE}', wins)
                    sleep(0.5)
                    print(f'{Fore.LIGHTRED_EX}Losses: {Fore.WHITE}', losses)
                    sleep(0.5)
                    print('Accuracy: {:.2f}'.format(accuracy))
                    sleep(1.5)
                    print('Ending simulation...')
                    sleep(1.5)
                    break

                else:
                    print(f'{Fore.RED}Incorrect...{Fore.WHITE}')
                    total_rounds = total_rounds + 1
                    losses = losses + 1
                    accuracy = wins/total_rounds
                    sleep(0.2)

    # Pair Splitting & Soft Totals -----------------------------------------------------
    elif option == 5:
        while True:
            table_selection = randint(1, 2)

            print(f'{Fore.LIGHTGREEN_EX}---------- NEW ROUND ----------{Fore.WHITE}')
            sleep(0.2)
            print('Drafting cards...')
            sleep(0.2)

            # Pair splitting -------------------------------------
            if table_selection == 1:
                player_selection = randint(1, 10)    # Adjust these to select which rows to play
                dealer_selection = randint(1, 10)

                player_cards = pair_splitting_table[player_selection][0]
                dealer_upcard = pair_splitting_table[0][dealer_selection]

                print("Player's cards: ", player_cards)
                sleep(0.2)
                print("Dealer's upcard: ", dealer_upcard)
                sleep(0.2)

                response = str(input('Action: ')).upper().rstrip()

                if response == pair_splitting_table[player_selection][dealer_selection]:
                    print(f'{Fore.GREEN}Correct!{Fore.WHITE}')
                    total_rounds = total_rounds + 1
                    wins = wins + 1
                    accuracy = wins / total_rounds
                    sleep(0.2)

                elif response == 'QUIT':
                    print('Printing stats...')
                    sleep(1)
                    print(f'{Fore.LIGHTMAGENTA_EX}---------- STATISTICS ----------{Fore.WHITE}')
                    print('Total rounds: ', total_rounds)
                    sleep(0.5)
                    print(f'{Fore.LIGHTGREEN_EX}Wins: {Fore.WHITE}', wins)
                    sleep(0.5)
                    print(f'{Fore.LIGHTRED_EX}Losses: {Fore.WHITE}', losses)
                    sleep(0.5)
                    print('Accuracy: {:.2f}'.format(accuracy))
                    sleep(1.5)
                    print('Ending simulation...')
                    sleep(1.5)
                    break

                else:
                    print(f'{Fore.RED}Incorrect...{Fore.WHITE}')
                    total_rounds = total_rounds + 1
                    losses = losses + 1
                    accuracy = wins/total_rounds
                    sleep(0.2)

            # Soft totals --------------------------------
            else:
                player_selection = randint(1, 4)   # Adjust these to select which rows to play
                dealer_selection = randint(1, 10)

                player_cards = soft_totals[player_selection][0]
                dealer_upcard = soft_totals[0][dealer_selection]

                print("Player's cards: ", player_cards)
                sleep(0.2)
                print("Dealer's upcard: ", dealer_upcard)
                sleep(0.2)

                response = str(input('Action: ')).upper().rstrip()

                if response == soft_totals[player_selection][dealer_selection]:
                    print(f'{Fore.GREEN}Correct!{Fore.WHITE}')
                    total_rounds = total_rounds + 1
                    wins = wins + 1
                    accuracy = wins / total_rounds
                    sleep(0.2)

                elif response == 'QUIT':
                    print('Printing stats...')
                    sleep(1)
                    print(f'{Fore.LIGHTMAGENTA_EX}---------- STATISTICS ----------{Fore.WHITE}')
                    print('Total rounds: ', total_rounds)
                    sleep(0.5)
                    print(f'{Fore.LIGHTGREEN_EX}Wins: {Fore.WHITE}', wins)
                    sleep(0.5)
                    print(f'{Fore.LIGHTRED_EX}Losses: {Fore.WHITE}', losses)
                    sleep(0.5)
                    print('Accuracy: {:.2f}'.format(accuracy))
                    sleep(1.5)
                    print('Ending simulation...')
                    sleep(1.5)
                    break

                else:
                    print(f'{Fore.RED}Incorrect...{Fore.WHITE}')
                    total_rounds = total_rounds + 1
                    losses = losses + 1
                    accuracy = wins/total_rounds
                    sleep(0.2)
    
    elif option == 6:
        print(f'{Fore.LIGHTMAGENTA_EX}Thanks for playing!{Fore.WHITE}')
        sleep(1)

        text = "Ending..."

        for char in text:
            print(char, end='', flush=True)
            sleep(0.2)

        print()  
        sleep(0.4)
        break

    else:
        print(f'{Fore.RED}Please select a valid option{Fore.WHITE}')
        sleep(0.5)




    
        




