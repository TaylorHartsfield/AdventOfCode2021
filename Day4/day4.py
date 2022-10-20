file = open('input.txt', 'r')
lines= file.read().split('\n\n')
_draws, *_boards = lines

boards = [[list(map(int, row.split())) for row in board.split('\n')]
                    for board in _boards]
draws = list(map(int, _draws.split(',')))

class Board:

    def __init__(self,board): 

        self.board = board
        self.rows = [set(row) for row in board]
        self.cols = [set(col) for col in zip(*board)]
    
    def check_for_match(self, num):

        for row in self.rows:
            if num in row:
                row.remove(num)

        for col in self.cols:
            if num in col:
                col.remove(num)

        return self.check_for_bingo_rows(num) or self.check_for_bingo_cols(num)

    def check_for_bingo_cols(self,num):
        if any(len(col) == 0 for col in self.cols):
            return sum(list(map(sum, self.cols))) * num
    
    def check_for_bingo_rows(self, num):
        if any(len(row) == 0 for row in self.rows):
            return sum(list(map(sum, self.rows))) * num
    
boards = [Board(board=board) for board in boards]


def play_game():
    for draw in draws:
        for board in boards:
            score = board.check_for_match(draw)
            if score:
                return score

def lose_game():
    bingos, num_boards = set(), len(boards)
    for draw in draws:
        for i, board in enumerate(boards):
            if i not in bingos:
                score = board.check_for_match(draw)
                if score:
                    bingos.add(i)
                if len(bingos) == num_boards:
                    return score
              




#Part 1 // CORRECT ⭐️
print(f'PART 1: {play_game()}')

#Part 2 // CORRECT ⭐️
print(f'PART 2: {lose_game()}')