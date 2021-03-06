class Cell(object):
    row = 0
    col = 0
    value = None

    def __init__(self, row, col, value=None):
        self.row = row
        self.col = col
        self.value = value

    def get_coords(self):
        return self.row, self.col


class Completed(object):
    def __init__(self, result):
        self.result = result


class Matrix(object):
    dim = 0
    data = []
    vector = []
    constants = {}
    out = []

    def __init__(self, conf):
        self.dim = int(conf.splitlines()[0])
        for line in conf.splitlines()[1:self.dim + 1]:
            row = [c for c in line.split(';') if c != '']
            self.out.append(row)
        self.data = [[int(cell.split()[0]) for cell in row] for row in self.out]

        # initial grid digits different from first and last
        for row, digits in enumerate(self.data):
            for col, digit in enumerate(digits):
                if digit > 0:
                    self.constants[(row, col)] = digit

        self.vector = [[cell.split()[1] for cell in row if len(cell.split()) > 1] for row in self.out]
        self.vector[self.dim - 1].append('END')

    def refresh(self):

        self.data = [[int(cell.split()[0]) for cell in row] for row in self.out]
        print('refreshing data', self.data)
