from matrix import Cell
from models.exception import EmptyPath, PathCompleted, CellFound


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
        y = from_cell.row - 1
        x = from_cell.col
        if y >= 0:
            self.__check(x, y, from_cell, self.to_north)
        else:
            self.__complete(from_cell)

    def to_north_east(self, from_cell):
        y = from_cell.row - 1
        x = from_cell.col + 1
        if y >= 0 and x < self.matrix.dim:
            self.__check(x, y, from_cell, self.to_north_east)
        else:
            self.__complete(from_cell)

    def to_north_west(self, from_cell):
        y = from_cell.row - 1
        x = from_cell.col - 1
        if y >= 0 and x >= 0:
            self.__check(x, y, from_cell, self.to_north_west)
        else:
            self.__complete(from_cell)

    def to_south(self, from_cell):
        y = from_cell.row + 1
        x = from_cell.col
        if y < self.matrix.dim:
            self.__check(x, y, from_cell, self.to_south)
        else:
            self.__complete(from_cell)

    def to_south_east(self, from_cell):
        y = from_cell.row + 1
        x = from_cell.col + 1
        if y < self.matrix.dim and x < self.matrix.dim:
            self.__check(x, y, from_cell, self.to_south_east)
        else:
            self.__complete(from_cell)

    def to_south_west(self, from_cell):
        y = from_cell.row + 1
        x = from_cell.col - 1
        if y < self.matrix.dim and x >= 0:
            self.__check(x, y, from_cell, self.to_south_west)
        else:
            self.__complete(from_cell)

    def to_east(self, from_cell):
        y = from_cell.row
        x = from_cell.col + 1
        if y < self.matrix.dim:
            self.__check(x, y, from_cell, self.to_east)
        else:
            self.__complete(from_cell)

    def to_west(self, from_cell):
        y = from_cell.row
        x = from_cell.col - 1
        if x >= 0:
            self.__check(x, y, from_cell, self.to_west)
        else:
            self.__complete(from_cell)

    def __check(self, x, y, from_cell, func):
        out = Cell(y, x, self.matrix.data[y][x])
        if self.matrix.data[y][x] == 0:
            self.path.append(out)
        if self.matrix.data[y][x] == from_cell.value + 1:
            raise CellFound(out)
        func(out)

    def __complete(self, from_cell):
        if len(self.path) == 0:
            raise EmptyPath(from_cell)
        elif len(self.path) == 1:
            raise CellFound(self.path[0])
        else:
            raise PathCompleted(self.path)
