import random
import time

def create_player_board(m, n):
    # Return a 2D list of dictionaries
    return [[{'value': '#', 'isFlagged': False} for _ in range(n)] for _ in range(m)]


def print_board(board, player_board):
    # Print column numbers
    print(' ', ' '.join(str(i) for i in range(1, len(board[0]) + 1)))
    # Print each row number and row contents
    for i in range(len(board)):
        print(i + 1, end=' ')
        for j in range(len(board[0])):
            # Print 'F' for flagged cells, '#' for unrevealed cells, actual value for revealed cells
            if player_board[i][j]['isFlagged']:
                print('F', end=' ')
            elif player_board[i][j]['value'] == '#':
                print('#', end=' ')
            else:
                print(board[i][j], end=' ')
        print()
    print()



def make_move(board, player_board, x, y, flag=False):
    # If the player is flagging a cell
    if flag:
        # Toggle the 'isFlagged' status of the cell
        player_board[x][y]['isFlagged'] = not player_board[x][y]['isFlagged']
        return 1
    # If the player is revealing a cell
    else:
        # If the selected cell contains a mine, return 0
        if board[x][y] == 'M':
            return 0
        # Reveal the selected cell on the player's board
        player_board[x][y]['value'] = board[x][y]
        return player_board[x][y]['value']

# # Function to make a move
# def make_move(board, player_board, x, y):
#     # If the selected cell contains a mine, return 0
#     if board[x][y] == 'M':
#         return 0
#     # Reveal the selected cell on the player's board
#     player_board[x][y] = board[x][y]
#     revealed = 1
#     # If the selected cell is empty, reveal all adjacent cells
#     if board[x][y] == 0:
#         for dx in [-1, 0, 1]:
#             for dy in [-1, 0, 1]:
#                 nx, ny = x + dx, y + dy
#                 if (0 <= nx < len(board)) and (0 <= ny < len(board[0])) and player_board[nx][ny] == '#':
#                     revealed += make_move(board, player_board, nx, ny)
#     return revealed

# Function to create the actual game board
def create_board(m, n, num_mines):
    # Create an empty board
    board = [[0]*n for _ in range(m)]
    # Randomly select cells to contain mines
    mines = random.sample(range(m*n), num_mines)
    for mine in mines:
        x, y = divmod(mine, n)
        # Place a mine and increment the count of adjacent mines for each neighboring cell
        board[x][y] = 'M'
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < m) and (0 <= ny < n) and board[nx][ny] != 'M':
                    board[nx][ny] += 1
    return board   

# Function to play the game
def play_minesweeper():
    # Get the board dimensions and number of mines from the player
    m = int(input("Enter the number of rows: "))
    n = int(input("Enter the number of columns: "))
    num_mines = int(input("Enter the number of mines: "))
    # Create the game board and the player's board
    board = create_board(m, n, num_mines)
    player_board = create_player_board(m, n)
    # Calculate the total number of safe cells
    total_cells = m * n - num_mines
    revealed_cells = 0
    start_time = time.time()
    while True:
        # Print the current state of the game and the elapsed time
        print_board(board, player_board)
        elapsed_time = time.time() - start_time
        print(f"Elapsed time: {int(elapsed_time)} seconds")
        # Get the player's move
        try:
            inputs = input("Enter your move (use 'f' for flagging): ").split()
            flag = inputs[0] == 'f'
            x = int(inputs[-2]) - 1
            y = int(inputs[-1]) - 1
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number.")
            continue
        # Process the player's move
        if flag:
            # Flag or unflag a cell
            player_board[x][y]['isFlagged'] = not player_board[x][y]['isFlagged']
            continue
        else:
            # Reveal a cell
            if player_board[x][y]['isFlagged']:
                print("Cell is flagged. Unflag it first.")
                continue
            revealed = make_move(board, player_board, x, y)
            if revealed == 0:
                # If a mine was revealed, the game is over
                print("Game Over")
                print("Final Board:")
                print_board(board, player_board)
                break
            revealed_cells += revealed
            if revealed_cells == total_cells:
                # If all safe cells have been revealed, the player wins
                print("Congratulations! You've cleared the board in", int(elapsed_time), "seconds")

play_minesweeper()