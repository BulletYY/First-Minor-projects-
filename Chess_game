class ChessGame:
    def __init__(self):
        self.board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ]
        self.current_player = 'white'

    def print_board(self):
        print("  a b c d e f g h")
        for i, row in enumerate(self.board):
            print(f"{8 - i} " + ' '.join(row) + f" {8 - i}")
        print("  a b c d e f g h")

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        piece = self.board[start_row][start_col]
        destination = self.board[end_row][end_col]
        player = piece.isupper()

        if piece == ' ':
            return False

        if (self.current_player == 'white' and not player) or \
           (self.current_player == 'black' and player):
            return False

        if piece.upper() == 'P':
            direction = -1 if player else 1
            if start_col == end_col and self.board[end_row][end_col] == ' ':
                if (start_row + direction == end_row) or \
                   (start_row == 6 and end_row == 4 and player and self.board[5][end_col] == ' ') or \
                   (start_row == 1 and end_row == 3 and not player and self.board[2][end_col] == ' '):
                    return True
            elif abs(start_col - end_col) == 1 and start_row + direction == end_row and destination != ' ':
                return True

        elif piece.upper() == 'R':
            if start_row == end_row:
                step = 1 if start_col < end_col else -1
                for c in range(start_col + step, end_col, step):
                    if self.board[start_row][c] != ' ':
                        return False
                return True
            elif start_col == end_col:
                step = 1 if start_row < end_row else -1
                for r in range(start_row + step, end_row, step):
                    if self.board[r][start_col] != ' ':
                        return False
                return True

        elif piece.upper() == 'N':
            if (abs(start_row - end_row), abs(start_col - end_col)) in [(2, 1), (1, 2)]:
                return True

        return False

    def play(self):
        while True:
            self.print_board()
            print(f"\n{self.current_player}'s turn:")

            try:
                start_pos = input("Enter start position (e.g., e2): ")
                end_pos = input("Enter end position (e.g., e4): ")

                start_col, start_row = ord(start_pos[0]) - ord('a'), 8 - int(start_pos[1])
                end_col, end_row = ord(end_pos[0]) - ord('a'), 8 - int(end_pos[1])

                if not (0 <= start_row <= 7 and 0 <= start_col <= 7 and 0 <= end_row <= 7 and 0 <= end_col <= 7):
                    print("Invalid input. Please enter positions within the board range.")
                    continue

                if self.is_valid_move(start_row, start_col, end_row, end_col):
                    if self.board[end_row][end_col].upper() == 'K':
                        print(f"Game over! {self.current_player} wins!")
                        break

                    self.board[end_row][end_col] = self.board[start_row][start_col]
                    self.board[start_row][start_col] = ' '

                    self.current_player = 'black' if self.current_player == 'white' else 'white'
                else:
                    print("Invalid move. Try again.")
            except (IndexError, ValueError):
                print("Invalid input. Please enter positions in the correct format.")

if __name__ == "__main__":
    game = ChessGame()
    game.play()
