class ConnectFour:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        
    def print_board(self):
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')
            print('+---' * self.cols + '+')
        
        col_numbers = '   '.join(str(i+1) for i in range(self.cols))
        print('  ' + col_numbers)
        
    def add_piece(self, col, player):
        if col < 0 or col >= self.cols:
            print("Invalid column! Column should be between 1 and", self.cols)
            return False
        
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = player
                return True
        print("Column is already full!")
        return False
    
    def check_win(self, player):
       # Check horizontally
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row][col+i] == player for i in range(4)):
                    return True
        
        # Check vertically
        for col in range(self.cols):
            for row in range(self.rows - 3):
                if all(self.board[row+i][col] == player for i in range(4)):
                    return True
        
        # Check diagonally (top-left to bottom-right)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if all(self.board[row+i][col+i] == player for i in range(4)):
                    return True
        
        # Check diagonally (top-right to bottom-left)
        for row in range(self.rows - 3):
            for col in range(3, self.cols):
                if all(self.board[row+i][col-i] == player for i in range(4)):
                    return True
        
        return False

# Create a Connect Four game with a 7x6 board
game = ConnectFour(6, 7)

# Example gameplay with user input
game.print_board()

current_player = 'X'
while True:
    try:
        column = int(input(f"Player {current_player}, choose a column (1-{game.cols}): ")) - 1
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid column number.")
        continue
    
    if game.add_piece(column, current_player):
        game.print_board()
        
        if game.check_win(current_player):
            print(f"Player {current_player} wins!")
            break
        
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
    else:
        print("Please try again.")

    # Check for a draw
    if all(game.board[0][col] != ' ' for col in range(game.cols)):
        print("It's a draw!")
        break