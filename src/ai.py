# Rotates a stone 90 degrees counter-clockwise, returning the new stone
def rotate(stone):
    return [[stone[y][x] for y in xrange(len(stone))] for x in xrange(len(stone[0]) - 1, -1, -1)]

class AI(object):

    def __init__(self):
        self.aggregate = 1.0
        self.differential = 1.0
        self.holes = 1.0

    def h(self, board, stone):
        max_score = 0
        max_loc = [0, 0]
        # Loops through each column/rotation
        for rotation in range(4):
            stone = rotate(stone)
            for column in range(10):
                # Places stone in given position, creates new board based on position
                new_board = self.drop_stone(board, stone, column)
                heights = self.get_heights(new_board)
                # Evaluates heuristic based on new board
                score = self.get_aggregate(heights) * self.aggregate
                score += self.get_differential(heights) * self.differential
                score += self.get_holes(new_board) * self.holes
                if score > max_score:
                    max_score = score
                    max_loc = [column, rotation]
        return max_loc

    # Drops stone into position provided, returns new board with changes made
    def drop_stone(self, board, stone, column):
        return board

    def get_heights(self, board):
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def get_aggregate(self, heights):
        return 0

    def get_differential(self, heights):
        return 0

    def get_holes(self, board):
        return 0