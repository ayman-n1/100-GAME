# File: CS112_A1_T2_Game1_20230080
# Purpose: Two players start from 0 and alternatively add a number from 1 to 10 to the sum. The player who reaches 100 wins.
# Author: Ayman Ahmed Abdelsamie
# ID: 20230080


def main():
    #Set sum
    sum = 0


    #Welcome message and display status
    print('Welcome to 100 game😊')
    print('Sum = 0')

    #Game playing
    while sum  < 100:
    #Player 1
        validity = True
        while validity:
            try:
                move = int(input("Player 1: Please add a number from 1 to 10 "))
                validity = False
            except:
                continue

        while move < 1 or move > 10:
            while not validity or (move < 1 or move > 10):
                try:
                    move = int(input("Player 1:\033[91m\033[1m INVALID INPUT\033[0m Please add a number from 1 to 10 "))
                    validity = True
                except:
                    continue
        sum += move

        if sum == 100:
            print(f'\033[93m Now sum = {sum}\033[0m')
            print('👏🥳Player 1 is the winner🥳👏')
            menu()
            break
        elif sum > 100:
            while sum > 100:
                sum -= move
                validity = True
                while validity:
                    try:
                        move = int(input("Player 1:\033[91m\033[1m INVALID INPUT\033[0m please insert a number from 1 to 10 "))
                        validity = False
                    except:
                        continue

                while move < 1 or move > 10:
                    while not validity or (move < 1 or move > 10):
                        try:
                            move = int(input("Player 1:\033[91m\033[1m INVALID INPUT\033[0m please add a number from 1 to 10 "))
                            validity = True
                        except:
                            continue
                sum += move
            if sum == 100:
                print(f'\033[93m Now sum = {sum}\033[0m')
                print('👏🥳Player 1 is the winner🥳👏')
                menu()
                break
        print(f'\033[93m Now sum = {sum}\033[0m')


    #Player 2
        validity = True
        while validity:
            try:
                move = int(input("Player 2:Please add a number from 1 to 10 "))
                validity = False
            except:
                continue
        
        while move < 1 or move > 10:
            while not validity or (move < 1 or move > 10):
                try:
                    move = int(input("Player 2:\033[91m\033[1m INVALID INPUT\033[0m Please insert a number from 1 to 10 "))
                    validity = True
                except:
                    continue
        sum += move

        if sum == 100:
            print(f'\033[93m Now sum = {sum}\033[0m')
            print('👏🥳Player 2 is the winner🥳👏')
            menu()
            break
        elif sum > 100:
            while sum > 100:
                sum -= move
                validity = True
                while validity:
                    try:
                        move = int(input("Player 2:\033[91m\033[1m INVALID INPUT\033[0m please insert a number from 1 to 10 "))
                        validity = False
                    except:
                        continue

                while move < 1 or move > 10:
                    while not validity or (move < 1 or move > 10):
                        try:
                            move = int(input("Player 2:\033[91m\033[1m INVALID INPUT\033[0m please insert a number from 1 to 10 "))
                            validity = True
                        except:
                            continue
                sum += move
            if sum == 100:
                print(f'\033[93m Now sum = {sum}\033[0m')
                print('👏🥳Player 2 is the winner🥳👏')
                menu()
                break
        print(f'\033[93m Now sum = {sum}\033[0m')


#Menu to check if the user wants to play again
def menu():
    valid_menu_choice = ['A' , 'B']
    menu_choice = input('\n Do you want to play again ?\n A) YES\n B) NO\n').upper()
    while menu_choice not in valid_menu_choice:
        menu_choice = input('\033[91m\033[1m INVALID INPUT\033[0m\n Do you want to play again ?\n A) YES\n B) NO\n').upper()
    if menu_choice == 'A':
        main()
    elif menu_choice == 'B':
        exit


main()