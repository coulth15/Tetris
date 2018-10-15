

# Rotates a stone 90 degrees counter-clockwise, returning the new stone
def rotate(stone):
    return [[stone[y][x] for y in xrange(len(stone))] for x in xrange(len(stone[0]) - 1, -1, -1)]


def check_collision(board, shape, offset):
    off_x, off_y = offset
    for cy, row in enumerate(shape):
        for cx, cell in enumerate(row):
            try:
                if cell and board[ cy + off_y ][ cx + off_x ]:
                    return True
            except IndexError:
                return True
    return False


def remove_row(board, row):
    del board[row]
    return [[0 for i in xrange(10)]] + board


def join_matrixes(mat1, mat2, mat2_off):

    off_x, off_y = mat2_off
    for cy, row in enumerate(mat2):
        for cx, val in enumerate(row):
            mat1[cy+off_y-1	][cx+off_x] += val
    return mat1


def drop(stone, board, column):
    new_board = board
    stone_y = 0
    finished = False
    while not finished:
        stone_y += 1
        if check_collision(board,
                    stone,
                    (column, stone_y)):
            finished = True
            new_board = join_matrixes(
                board,
                stone,
                (column, stone_y))
            cleared_rows = 0
            while True:
                for i, row in enumerate(new_board[:-1]):
                    if 0 not in row:
                        new_board = remove_row(
                            new_board, i)
                        cleared_rows += 1
                        break
                else:
                    break
        return new_board


class AI(object):

    def __init__(self):
        self.aggregate = -0.1
        self.differential = -.2
        self.holes = -1.0

    def h(self, board, stone):
        max_score = -10000
        max_loc = [0, 0]
        # Loops through each column/rotation
        for rotation in range(4):
            span = len(stone[0])
            stone = rotate(stone)
            for column in range(10-span):
                # Places stone in given position, creates new board based on position
                new_board = drop(stone, board, column)
                heights = self.get_heights(new_board)
                # Evaluates heuristic based on new board
                score = self.get_aggregate(heights) * self.aggregate
                score += self.get_differential(heights) * self.differential
                score += self.get_holes(new_board, heights) * self.holes
                if score > max_score:
                    max_score = score
                    max_loc = [column, rotation]
        return max_loc

    def get_heights(self, board):
        heights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for column in range(10):
            for row in range(22):
                if board[row][column]:
                    heights[column] = 22-row
                    break
        return heights

    def get_aggregate(self, heights):
        total = 0.0
        for x in heights:
            total += x
        return total / len(heights)

    def get_differential(self, heights):
        total = 0.0
        for x in range(9):
            total += abs(heights[x] - heights[x+1])
        return total / len(heights)

    def get_holes(self, board, heights):
        total = 0
        for column in range(10):
            for row in range(22-heights[column], 22):
                if not board[row][column]:
                    total += 1
        return total

    def test(self, board, stone_x):
        stone = [[4, 0, 0], [4, 4, 4]]
        print(drop(stone, board, 2))
