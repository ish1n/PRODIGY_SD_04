def print_board(board):
    # Print the board in a readable format
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("- " * 11)
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(num)
            else:
                print(str(num) + " ", end="")

def find_empty(board):
    # Find the next empty space (denoted by 0)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(board, num, pos):
    # Check if the number can be placed in the position (pos)
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    # Recursive function to solve the board using backtracking
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def get_board_from_user():
    board = []
    print("Enter the Sudoku puzzle row by row.")
    print("Use 0 for empty cells. Separate numbers with spaces.")
    for i in range(9):
        while True:
            try:
                row = input(f"Enter row {i + 1}: ").strip().split()
                if len(row) != 9:
                    raise ValueError("Each row must have exactly 9 numbers.")
                row = [int(num) for num in row]
                if any(num < 0 or num > 9 for num in row):
                    raise ValueError("Numbers must be between 0 and 9.")
                board.append(row)
                break
            except ValueError as ve:
                print(f"Invalid input: {ve}")
    return board

def main():
    print("Welcome to the Sudoku Solver!")
    board = get_board_from_user()
    print("\nOriginal board:")
    print_board(board)
    if solve(board):
        print("\nSolved board:")
        print_board(board)
    else:
        print("\nThis Sudoku puzzle cannot be solved.")

if __name__ == "__main__":
    main()
