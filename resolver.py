import sys

from models.exception import Completed
from models.matrix import Cell
from scanner import PathScanner


class Resolver(object):
    global_map = {}
    scanner = None
    matrix = None
    current_cell = None

    def __init__(self, matrix):
        self.matrix = matrix
        self.scanner = PathScanner(matrix.data)
        self.refresh()

    def refresh(self):
        for i, row in enumerate(self.matrix.data):
            for j, cell in enumerate(row):
                ref = Cell(i, j, self.matrix.data[i][j])
                if ref.value != pow(self.matrix.dim, 2):
                    self.global_map[(i, j)] = self.scanner.scan[self.matrix.vector[ref.row][ref.col]](ref)
                else:
                    self.global_map[(i, j)] = [Completed(self.matrix.data)]

    def walk(self, level=0):
        # get cell available slots
        cells = self.global_map[(self.current_cell.row, self.current_cell.col)]
        print('from', self.current_cell.row, self.current_cell.col)
        # if no cells found : bad path or process completed
        if len(cells) > 0 and not isinstance(cells[0], Completed):
            print('targets', cells)
            target = cells[level]
            target.value = self.current_cell.value + 1
            self.matrix.data[target.row][target.col] = target.value
            self.current_cell = target
            self.refresh()
            self.walk(level)
        else:
            raise cells[0]

    # return lower digit found in the matrix
    def get_entry_cell(self):
        # get lower digit in the matrix (<> 0)
        digit = sys.maxsize
        for i, row in enumerate(self.matrix.data):
            for j, col in enumerate(row):
                if self.matrix.data[i][j] != 0 and self.matrix.data[i][j] < digit:
                    digit = self.matrix.data[i][j]
                    x = i
                    y = j
        return Cell(x, y, self.matrix.data[x][y])
