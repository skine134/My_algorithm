def boom_aria(board, i, j):
    boom_set = set()
    for y in range(i-1 , i+2):
        for x in range(j-1,j+2):
            if 0<= x < len(board[0]) and 0<= y < len(board) and not (x == j and y == i):
                boom_set.add((y,x))
    return boom_set

def solution(board):
    boom_set = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                boom_set.update(boom_aria(board,i,j))
    for i,j in boom_set:
        board[i][j] = 1
    sum = 0
    for row in board:
        sum = sum + row.count(0)
    return sum
arr = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]