class Cell(object):
    row = 0
    col = 0
    value = None

    # coord: Tupple(row,line)
    def __init__(self, row, col, value=None):
        self.row = row
        self.col = col
        self.value = value


class Matrix(object):
    dim = 0
    data = []
    vector = []

    def __init__(self, conf):
        self.dim = int(conf.splitlines()[0])
        self.path = []
        out = []
        for line in conf.splitlines()[1:self.dim + 1]:
            row = [c for c in line.split(';') if c != '']
            out.append(row)
        self.data = [[int(cell.split()[0]) for cell in row] for row in out]
        self.vector = [[cell.split()[1] for cell in row if len(cell.split()) > 1] for row in out]

    # def to_north(self, from_cell):
    #     if from_cell.row - 1 >= 0:
    #         out = Cell(from_cell.row - 1, from_cell.col)
    #         if self.data[from_cell.row - 1][from_cell.col] == 0:
    #             self.path.append(out)
    #         self.to_north(out)
    #     else:
    #         if len(self.path) == 0:
    #             raise EmptyPath(from_cell)
    #         else:
    #             return Path(self.path)
    #
    # def to_north_east(self, from_cell):
    #     if from_cell.row - 1 >= 0 and from_cell.col + 1 < self.dim:
    #         out = Cell(from_cell.row - 1, from_cell.col + 1)
    #         if self.data[from_cell.row - 1][from_cell.col + 1] == 0:
    #             self.path.append(out)
    #         self.to_north_east(out)
    #     else:
    #         if len(self.path) == 0:
    #             raise EmptyPath(from_cell)
    #         else:
    #             return Path(self.path)
    #
    # def to_north_west(self, from_cell):
    #     if from_cell.row - 1 >= 0 and from_cell.col - 1 >= 0:
    #         out = Cell(from_cell.row - 1, from_cell.col - 1)
    #         if self.data[from_cell.row - 1][from_cell.col - 1] == 0:
    #             self.path.append(out)
    #         self.to_north_west(out)
    #     else:
    #         if len(self.path) == 0:
    #             raise EmptyPath(from_cell)
    #         else:
    #             return Path(self.path)
    #
    # def to_south(self, from_cell):
    #     if from_cell.row + 1 < self.dim:
    #         out = Cell(from_cell.row + 1, from_cell.col, self.data[from_cell.row + 1][from_cell.col])
    #         if self.data[from_cell.row + 1][from_cell.col] == 0:
    #             self.path.append(out)
    #         self.to_south(out)
    #     else:
    #         if len(self.path) == 0:
    #             raise EmptyPath(from_cell)
    #         else:
    #             return Path(self.path)
    #
    # def to_south_east(self, from_cell):
    #
    #     if from_cell.row + 1 < self.dim and from_cell.col + 1 < self.dim:
    #         out = Cell(from_cell.row + 1, from_cell.col + 1)
    #         if self.data[from_cell.row + 1][from_cell.col + 1] == 0:
    #             print('south_east', from_cell.__dict__, out.__dict__)
    #             self.path.append(out)
    #         self.to_south_east(out)
    #     else:
    #         if len(self.path) == 0:
    #             raise EmptyPath(from_cell)
    #         else:
    #             return Path(self.path)
    #
    # def to_south_west(self, from_cell):
    #     if from_cell.row + 1 < self.dim and from_cell.col - 1 >= 0:
    #         out = Cell(from_cell.row + 1, from_cell.col - 1)
    #         if self.data[from_cell.row + 1][from_cell.col - 1] == 0:
    #             self.path.append(out)
    #         self.to_south_west(out)
    #     else:
    #         if len(self.path) == 0:
    #             raise EmptyPath(from_cell)
    #         else:
    #             return Path(self.path)
    #
    # def to_east(self, from_cell):
    #     if from_cell.col + 1 < self.dim:
    #         out = Cell(from_cell.row, from_cell.col + 1)
    #         if self.data[from_cell.row][from_cell.col + 1] == 0:
    #             self.path.append(out)
    #         self.to_east(out)
    #     else:
    #         if len(self.path) == 0:
    #             raise EmptyPath(from_cell)
    #         else:
    #             return Path(self.path)
    #
    # def to_west(self, from_cell):
    #     if from_cell.col - 1 >= 0:
    #         out = Cell(from_cell.row, from_cell.col - 1)
    #         if self.data[from_cell.row][from_cell.col - 1] == 0:
    #             self.path.append(out)
    #         self.to_west(out)
    #     else:
    #         if len(self.path) == 0:
    #             raise EmptyPath(from_cell)
    #         else:
    #             return Path(self.path)

