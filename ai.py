class AI(object):

    def __init__(self):
        self.columnHeights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def trackHeight(self, stone, stone_x, board):
        span = len(stone[0])
        for n in range (stone_x, stone_x+span):
            i = -1
            for x in board:
                i += 1
                if x[n]:
                    self.columnHeights[n] = 22-i
                    break

    def clearHeight(self, cleared_rows):
        for n in range (0, len(self.columnHeights)):
            self.columnHeights[n] -= cleared_rows

    def printHeight(self):
        print(self.columnHeights)