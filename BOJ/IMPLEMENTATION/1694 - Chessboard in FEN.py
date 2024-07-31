'''
BOJ 1694 - Chessboard in FEN (https://www.acmicpc.net/problem/1694)

Given a chessboard in FEN, compute the number of unoccupied squares not attacked by any piece.
'''

import sys


# 2. FUNCTIONS TO IMPLEMENT ATTACKS

def adjacent_attack(row_num, col_num, dy, dx):
    
    global board
    
    for idx in range(len(dy)):
        target_row = row_num + dy[idx]
        target_col = col_num + dx[idx]
        if 0 <= target_row < 8 and 0 <= target_col < 8:
            if board[target_row][target_col] == "X":
                board[target_row][target_col] = "O"

def slide_attack(row_num, col_num, dy, dx):
    
    global board 
    
    for idx in range(len(dy)):
        target_row = row_num + dy[idx]
        target_col = col_num + dx[idx]
        while 0 <= target_row < 8 and 0 <= target_col < 8:
            if board[target_row][target_col] == "X" or board[target_row][target_col] == "O":
                board[target_row][target_col] = "O"
                target_row += dy[idx]
                target_col += dx[idx]
            else:
                break


# 1. TO REPRESENT A CHESSBOARD

while True:
    
    try:
        
        fen = list(sys.stdin.readline().strip().split("/"))
            
        board = [["X" for col_num in range(8)] for row_num in range(8)]
            
        for row_num in range(8):
                
            col_num = 0

            row = fen[row_num]
            for char in row:
                if 48 <= ord(char) <= 57:
                    col_num += int(char)
                else:
                    if char.upper() == "P":
                        board[row_num][col_num] = char
                    else:
                        board[row_num][col_num] = char.upper()
                    col_num += 1


        # 3. TO FILL ATTACKED SQUARES
        # Queen = Rook + Bishop

        for row_num in range(8):
            for col_num in range(8):
                
                now_piece = board[row_num][col_num]
                
                # Unoccupied
                if now_piece == "O" or now_piece == "X":
                    continue
                
                # King
                if now_piece == "K":
                    
                    dy = [1, 1, 1, 0, -1, -1, -1, 0]
                    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
                    adjacent_attack(row_num, col_num, dy, dx)
                    

                # Knight
                elif now_piece == "N":
                    
                    dy = [2, 1, -1, -2, -2, -1, 1, 2]
                    dx = [1, 2, 2, 1, -1, -2, -2, -1]
                    adjacent_attack(row_num, col_num, dy, dx)
                    
                # Queen
                elif now_piece == "Q":
                    
                    dy = [1, 1, 1, 0, -1, -1, -1, 0]
                    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
                    slide_attack(row_num, col_num, dy, dx)

                # Rook 
                elif now_piece == "R":
                    
                    dy = [1, 0, -1, 0]
                    dx = [0, 1, 0, -1]
                    slide_attack(row_num, col_num, dy, dx)

                # Bishop
                elif now_piece == "B":
                    
                    dy = [1, -1, -1, 1]
                    dx = [1, 1, -1, -1]
                    slide_attack(row_num, col_num, dy, dx)

                # Pawn
                elif now_piece == "p":
                    
                    dy = [1, 1]
                    dx = [1, -1]
                    adjacent_attack(row_num, col_num, dy, dx)
                
                elif now_piece == "P":
                    
                    dy = [-1, -1]
                    dx = [1, -1]
                    adjacent_attack(row_num, col_num, dy, dx)


        # 4. TO SOLVE THE PROBLEM
        
        ans = 0
        for row in board:
            ans += row.count("X")
        print(ans)
    
    except:
        
        break
