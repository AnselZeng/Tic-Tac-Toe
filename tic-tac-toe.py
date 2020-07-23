# Tic-Tac-Toe made in python.

'''
File: tic-tac-toe.py
Purpose: A simple two player game, first person with 3 marks in a row wins.
Author: Ansel Zeng
Date: July 23, 2020
'''

theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}
board_keys = []
for key in theBoard:
    board_keys.append(key)

# Function to set up the board
def printBoard(board):
    print('+---+---+---+')
    print('| ' + board['1'] + ' | ' + board['2'] + ' | ' + board['3'] + ' |')
    print('+---+---+---+')
    print('| ' + board['4'] + ' | ' + board['5'] + ' | ' + board['6'] + ' |')
    print('+---+---+---+')
    print('| ' + board['7'] + ' | ' + board['8'] + ' | ' + board['9'] + ' |')
    print('+---+---+---+')

# Welcome and asks for player names
print("|-------------------------------|")
print("|    Welcome to Tic-Tac-Toe!    |")
print("|      Coded by Ansel Zeng      |")
print("|                               |")
print("|         +---+---+---+         |")
print("|         | 1 | 2 | 3 |         |")
print("|         +---+---+---+         |")
print("|         | 4 + 5 + 6 |         |")
print("|         +---+---+---+         |")
print("|         | 7 + 8 + 9 |         |")
print("|         +---+---+---+         |")
print("|                               |")
print("|   Type in the corresponding   |")
print("|  number to a square to place  |")
print("|    down your mark (X or O)    |")
print("|                               |")
print("|    Good luck and have fun!    |")
print("|-------------------------------|")
playerX = input("Player X enter your name: ")
playerO = input("Player O enter your name: ")

# The main function
def game():
    player = playerX
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)

        # Get user input for mark placement
        move = input("It's your turn, " + player + "!\nEnter where you want to place your " + turn + ": ")

        # Fills a square with mark X or O
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That square is already filled, try again.")
            continue

        # After the 5th move check if a player has won
        if count >= 5:
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # top row
                printBoard(theBoard)
                print("\nGame over, " + player + " won!\n")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # middle row
                printBoard(theBoard)
                print("\nGame over, " + player + " won!\n")
                break
            elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # bottom row
                printBoard(theBoard)
                print("\nGame over, " + player + " won!\n")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # left column
                printBoard(theBoard)
                print("\nGame over, " + player + " won!\n")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # middle column
                printBoard(theBoard)
                print("\nGame over, " + player + " won!\n")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # right column
                printBoard(theBoard)
                print("\nGame over, " + player + " won!\n")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal top left to bottom right
                printBoard(theBoard)
                print("\nGame over, " + player + " won!\n")
                break
            elif theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':  # diagonal top right to bottom left
                printBoard(theBoard)
                print("\nGame over, " + player + " won!\n")
                break

        # When neither X nor O wins and the board is full it's a tie
        if count == 9:
            print("\nGame over, it's a tie!\n")

        # Changing the player name and mark after each turn
        if player == playerX:
            player = playerO
        else:
            player = playerX
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    # Asking players if they want to restart and play again
    restart = input("Do want to play Again? Type y or n: ")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "
        game()

if __name__ == "__main__":
    game()