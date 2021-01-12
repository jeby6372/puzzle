from models.exceptions import Completed
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
            'Z': self.to_south,
            'ZW': self.to_south_west,
            'W': self.to_west,
            'NW': self.to_north_west
        }

    def to_north(self, from_cell):
        # print('to north', from_cell.__dict__)
        path = []
        x = from_cell.col
        for i in reversed(range(from_cell.row)):
            # out = Cell(i, x, self.data[i][x])
            out = (i, x)
            path.append(out)
        return path

    def to_east(self, from_cell):
        # print('to east', from_cell.__dict__)
        path = []
        x = from_cell.row
        for i in range(from_cell.col + 1, self.dim):
            # out = Cell(x, i, self.data[x][i])
            out = (x, i)
            path.append(out)
        return path

    def to_south(self, from_cell):
        # print('to south', from_cell.__dict__)
        path = []
        x = from_cell.col
        for i in range(from_cell.row + 1, self.dim):
            # out = Cell(i, x, self.data[i][x])
            out = (i, x)
            path.append(out)
        return path

    def to_west(self, from_cell):
        # print('to west', from_cell.__dict__)
        path = []
        x = from_cell.row
        for i in reversed(range(from_cell.col)):
            # out = Cell(x, i, self.data[x][i])
            out = (x, i)
            path.append(out)
        return path

    def to_north_east(self, from_cell):
        # print('to north-east', from_cell.__dict__)
        path = []
        x = from_cell.row
        for i in range(from_cell.col + 1, self.dim):
            x -= 1
            if x < 0:
                break
            # out = Cell(x, i, self.data[x][i])
            out = (x, i)
            path.append(out)
        return path

    def to_north_west(self, from_cell):
        # print('to north-west', from_cell.__dict__)
        path = []
        x = from_cell.row
        for i in reversed(range(from_cell.col)):
            x -= 1
            if x < 0:
                break
            # out = Cell(x, i, self.data[x][i])
            out = (x, i)
            path.append(out)
        return path

    def to_south_east(self, from_cell):
        # print('to south-east', from_cell.__dict__)
        path = []
        x = from_cell.row
        for i in range(from_cell.col + 1, self.dim):
            x += 1
            if x > self.dim - 1:
                break
            # out = Cell(x, i, self.data[x][i])
            out = (x, i)
            path.append(out)
        return path

    def to_south_west(self, from_cell):
        # print('to south-west', from_cell.__dict__)
        path = []
        x = from_cell.row
        for i in reversed(range(from_cell.col)):
            x += 1
            if x > self.dim - 1:
                break
            out = Cell(x, i, self.data[x][i])
            out = (x, i)
            path.append(out)
        return path

