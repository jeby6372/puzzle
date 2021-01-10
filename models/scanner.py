from matrix import Matrix, Cell
from models.exception import EmptyPath, PathCompleted
from models.responses import Path


class PathScanner(object):
    matrix = None
    path = []

    def __init__(self, matrix):
        self.matrix = matrix
        # self.path = Path()
        self.scan = {
            'N': self.to_north,
            'NO': self.to_north_east,
            'O': self.to_east,
            'ZO': self.to_south_east,
            'Z': self.to_south,
            'ZW': self.to_south_west,
            'W': self.to_west,
            'NW': self.to_north_west
        }

    def to_north(self, from_cell):
        if from_cell.row - 1 >= 0:
            out = Cell(from_cell.row - 1, from_cell.col)
            if self.matrix.data[from_cell.row - 1][from_cell.col] == 0:
                self.path.append(out)
            self.to_north(out)
        else:
            if len(self.path) == 0:
                raise EmptyPath(from_cell)
            else:
                raise PathCompleted(self.path)

    def to_north_east(self, from_cell):
        if from_cell.row - 1 >= 0 and from_cell.col + 1 < self.matrix.dim:
            out = Cell(from_cell.row - 1, from_cell.col + 1)
            if self.matrix.data[from_cell.row - 1][from_cell.col + 1] == 0:
                self.path.append(out)
            self.to_north_east(out)
        else:
            if len(self.path) == 0:
                raise EmptyPath(from_cell)
            else:
                raise PathCompleted(self.path)

    def to_north_west(self, from_cell):
        if from_cell.row - 1 >= 0 and from_cell.col - 1 >= 0:
            out = Cell(from_cell.row - 1, from_cell.col - 1)
            if self.matrix.data[from_cell.row - 1][from_cell.col - 1] == 0:
                self.path.append(out)
            self.to_north_west(out)
        else:
            if len(self.path) == 0:
                raise EmptyPath(from_cell)
            else:
                raise PathCompleted(self.path)

    def to_south(self, from_cell):
        if from_cell.row + 1 < self.matrix.dim:
            out = Cell(from_cell.row + 1, from_cell.col)
            if self.matrix.data[from_cell.row + 1][from_cell.col] == 0:
                self.path.append(out)
            self.to_south(out)
        else:
            if len(self.path) == 0:
                raise EmptyPath(from_cell)
            else:
                raise PathCompleted(self.path)

    def to_south_east(self, from_cell):

        if from_cell.row + 1 < self.matrix.dim and from_cell.col + 1 < self.matrix.dim:
            out = Cell(from_cell.row + 1, from_cell.col + 1)
            if self.matrix.data[from_cell.row + 1][from_cell.col + 1] == 0:
                self.path.append(out)
            self.to_south_east(out)
        else:
            if len(self.path) == 0:
                raise EmptyPath(from_cell)
            else:
                raise PathCompleted(self.path)

    def to_south_west(self, from_cell):
        if from_cell.row + 1 < self.matrix.dim and from_cell.col - 1 >= 0:
            out = Cell(from_cell.row + 1, from_cell.col - 1)
            if self.matrix.data[from_cell.row + 1][from_cell.col - 1] == 0:
                self.path.append(out)
            self.to_south_west(out)
        else:
            if len(self.path) == 0:
                raise EmptyPath(from_cell)
            else:
                raise PathCompleted(self.path)

    def to_east(self, from_cell):
        if from_cell.col + 1 < self.matrix.dim:
            out = Cell(from_cell.row, from_cell.col + 1)
            if self.matrix.data[from_cell.row][from_cell.col + 1] == 0:
                self.path.append(out)
            self.to_east(out)
        else:
            if len(self.path) == 0:
                raise EmptyPath(from_cell)
            else:
                raise PathCompleted(self.path)

    def to_west(self, from_cell):
        if from_cell.col - 1 >= 0:
            out = Cell(from_cell.row, from_cell.col - 1)
            if self.matrix.data[from_cell.row][from_cell.col - 1] == 0:
                self.path.append(out)
            self.to_west(out)
        else:
            if len(self.path) == 0:
                raise EmptyPath(from_cell)
            else:
                raise PathCompleted(self.path)
