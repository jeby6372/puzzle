
from models.exception import EmptyPath, PathCompleted, CellFound
from models.matrix import Cell


class PathScanner(object):
    data = None
    dim = 0
    path = []

    def __init__(self, data):
        self.data = data
        self.dim = len(data)
        self.scan = {
            'N': self.to_north,
            'NO': self.to_north_east,
            'O': self.to_east,
            'ZO': self.to_south_east,
            'Z': self.to_south_2,
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
        if y >= 0 and x < self.dim:
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
        if y < self.dim:
            self.__check(x, y, from_cell, self.to_south)
        else:
            self.__complete(from_cell)

    def to_south_2(self, from_cell):
        y = from_cell.row + 1
        x = from_cell.col
        for i in range(1, self.dim):
            out = Cell(i, x, self.data[i][x])
            if self.data[i][x] == 0:
                self.path.append(out)
        return self.path

    def to_south_east(self, from_cell):
        y = from_cell.row + 1
        x = from_cell.col + 1
        if y < self.dim and x < self.dim:
            self.__check(x, y, from_cell, self.to_south_east)
        else:
            self.__complete(from_cell)

    def to_south_west(self, from_cell):
        y = from_cell.row + 1
        x = from_cell.col - 1
        if y < self.dim and x >= 0:
            self.__check(x, y, from_cell, self.to_south_west)
        else:
            self.__complete(from_cell)

    def to_east(self, from_cell):
        y = from_cell.row
        x = from_cell.col + 1
        if x < self.dim:
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
        # print(x,y,func)
        out = Cell(y, x, self.data[y][x])
        if self.data[y][x] == 0:
            self.path.append(out)
        if self.data[y][x] == from_cell.value + 1:
            raise CellFound(out)
        # recurse
        func(out)

    def __complete(self, from_cell):
        if len(self.path) == 0:
            raise EmptyPath(from_cell)
        elif len(self.path) == 1:
            raise CellFound(self.path[0])
        else:
            raise PathCompleted(self.path)
