import random
import time

def create_player_board(m, n):
    return [['#']*n for _ in range(m)]

def print_board(board, player_board):
    print(' ', ' '.join(str(i) for i in range(1, len(board[0]) + 1)))
    for i in range(len(board)):
        print(i + 1, end=' ')
        for j in range(len(board[0])):
            if player_board[i][j] == '#':
                print('#', end=' ')
            else:
                print(board[i][j], end=' ')
        print()
    print()

def make_move(board, player_board, x, y):
    if board[x][y] == 'M':
        return 0
    player_board[x][y] = board[x][y]
    revealed = 1
    if board[x][y] == 0:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < len(board)) and (0 <= ny < len(board[0])) and player_board[nx][ny] == '#':
                    revealed += make_move(board, player_board, nx, ny)
    return revealed

def create_board(m, n, num_mines):
    board = [[0]*n for _ in range(m)]
    mines = random.sample(range(m*n), num_mines)
    for mine in mines:
        x, y = divmod(mine, n)
        board[x][y] = 'M'
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < m) and (0 <= ny < n) and board[nx][ny] != 'M':
                    board[nx][ny] += 1
    return board   


def play_minesweeper():
    m = int(input("Enter the number of rows: "))
    n = int(input("Enter the number of columns: "))
    num_mines = int(input("Enter the number of mines: "))
    board = create_board(m, n, num_mines)
    player_board = create_player_board(m, n)
    total_cells = m * n - num_mines
    revealed_cells = 0
    start_time = time.time()
    while True:
        print_board(board, player_board)
        elapsed_time = time.time() - start_time
        print(f"Elapsed time: {int(elapsed_time)} seconds")
        try:
            inputs = input("Enter your move (use 'f' for flagging): ").split()
            flag = inputs[0] == 'f'
            x = int(inputs[-2]) - 1
            y = int(inputs[-1]) - 1
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number.")
            continue
        if flag:
            if player_board[x][y] == '#':
                player_board[x][y] = 'F'
            elif player_board[x][y] == 'F':
                player_board[x][y] = '#'
        else:
            if player_board[x][y] == 'F':
                print("Cell is flagged. Unflag it first.")
                continue
            revealed = make_move(board, player_board, x, y)
            if revealed == 0:
                print("Game Over")
                print("Final Board:")
                print_board(board, board)
                break
            revealed_cells += revealed
            if revealed_cells == total_cells:
                print("Congratulations! You've cleared the board in", int(elapsed_time), "seconds")
                print("Final Board:")
                print_board(board, board)
                break

play_minesweeper()