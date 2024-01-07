
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
        for row in self.board:
            print(' '.join(row))

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        piece = self.board[start_row][start_col]
        destination = self.board[end_row][end_col]
        player = piece.lower()

        if piece == ' ':
            return False

        # Check if the piece belongs to the current player
        if (self.current_player == 'white' and player.islower()) or \
           (self.current_player == 'black' and player.isupper()):
            return False

        # Add more move validation logic here
        # For simplicity, let's just allow any non-capturing move for now

        return True

    def play(self):
        while True:
            self.print_board()
            print(f"\n{self.current_player}'s turn:")
            start_row = int(input("Enter start row: "))
            start_col = int(input("Enter start column: "))
            end_row = int(input("Enter end row: "))
            end_col = int(input("Enter end column: "))

            if self.is_valid_move(start_row, start_col, end_row, end_col):
                self.board[end_row][end_col] = self.board[start_row][start_col]
                self.board[start_row][start_col] = ' '

                # Switch player's turn
                self.current_player = 'black' if self.current_player == 'white' else 'white'
            else:
                print("Invalid move. Try again.")


if __name__ == "__main__":
    game = ChessGame()
    game.play()
