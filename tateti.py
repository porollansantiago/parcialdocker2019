class TaTeTi:
    def __init__(self, old_board=[' ' for _ in range(9)]):
        if len(old_board) == 1:
            self.board = old_board
        else:
            self.board = old_board
        self.game_over = False
        self.winner = ''

    def assign(self, position, piece):
        if self.validate(position):
            self.board[position - 1] = piece
        else:
            raise Exception
        self.check_board()
        if not self.game_over:
            self.game_over = self.full()

    def validate(self, position):
        return self.board[position - 1] == ' '

    def full(self):
        return (' ' not in self.board)

    def check_board(self):
        self.check_rows()
        self.check_cols()
        self.check_diag()

    def check_rows(self):
        val = 0
        for _ in range(3):
            self.check(self.board[val:val + 3])
            val += 3

    def check_cols(self):
        for col_number in range(3):
            line = []
            val = 0
            for _ in range(3):
                row = self.board[val:val + 3]
                val += 3
                line.append(row[col_number])
            self.check(line)

    def check_diag(self):
        for step in range(1, -2, -2):
            val = 0
            line = []
            start = 0
            stop = 3
            stop *= step
            if step == -1:
                start += step
                stop += step
            for idx in range(start, stop, step):
                row = self.board[val:val + 3]
                val += 3
                line.append(row[idx])
            self.check(line)

    def check(self, line):
        if len(set(line)) == 1 and ' ' not in set(line):
            self.game_over = True
            self.winner = line[0]

    def win(self):
        self.check_board()
        return self.game_over

    def draw_board(self):
        board = ''
        for idx in range(len(self.board)):
            if idx == 0:
                board += '\n'
            if idx in (3, 6):
                board += ' \n---+---+---\n'
            piece = self.board[idx] if self.board[idx] != ' ' else str(idx + 1)
            board += ' ' + piece
            if idx not in (2, 5, 8):
                board += ' |'
        board += ' \n'
        return board
