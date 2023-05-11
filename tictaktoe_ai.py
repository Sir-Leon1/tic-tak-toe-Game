#!/bin/python3

def constboard(board):
    print("Current status of the board:  \n\n");

    for i in range(0,9):

        if (i > 0) and (i%3 == 0):
            print("\n")
        if board[i] == 0:
            print("_ ", end=" ")
        if board[i] == -1:
            print("X ", end=" ")
        if board[i] == 1:
            print("O ", end=" ")

    print("\n\n")



def user_1_turn(board):
    pos = input("Enter X's psition from [1,2...,9]")
    pos = int(pos)

    if (board[pos - 1]):
        print("Wrong move")
        exit(0)

    board[pos - 1] = -1


def user_2_turn(board):
    pos = input("Enter O's position from [1,2...,9]")
    pos = int(pos)

    if (board[pos - 1]) != 0:
        print("Wrong move")
        exit(0)
    board[pos - 1] = 1


def compTurn(board):

def analyze_board(board):
    cb = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    for i in range(0,8):
        if (board[cb[i][0]]) != 0 and board[cb[i][0]] == board[cb[i][1]]
         and board[cb[i][0]] == board[cb[i][2]]:
             return booard[cb[i][0]]

    return 0

def main():
    choice = input("Enter 1 for Single PLayer, 2 for Multiplayer")
    choice = int(choice)

    board = [0,0,0,0,0,0,0,0,0]

    if (choice == 1):
        print("Computer: O Vs You: X");
        player = input("Enter to play 1(st) OR 2(nd)")
        player = int(player)

        for i in range(0,9):
            if analyzeboard(board) != 0:
                break
            if ((i + player)% 2) == 0:
                compTurn(board)
            else:
                ConstBoard(board)
                User1Turn(board)

    else:
        for i in range(0,9):

            if(analyzeboard(board) != 0):
                break
            if(i % 2 == 0):
                constBoard(board)
                user1Turn(board)
            else:
                constBoard(board)
                user2Turn(board)

    x = analyzeboard(board)
    if x == 0:
        constBoard(board)
        print("Draw...!!")
    if x == -1:
        constBoard(board)
        print("Player X wins :::: O looses!!!")
    if x == 1:
        constBoard(board)
        print("Player O wins:::: X looses!!!")
