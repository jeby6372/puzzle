class Cell(object):
    row = 0
    col = 0
    value = None

    def __init__(self, row, col, value=None):
        self.row = row
        self.col = col
        self.value = value


class Completed(object):
    def __init__(self, result):
        self.result = result


class Matrix(object):
    dim = 0
    data = []
    vector = []
    constants = []

    def __init__(self, conf):
        self.dim = int(conf.splitlines()[0])
        out = []
        for line in conf.splitlines()[1:self.dim + 1]:
            row = [c for c in line.split(';') if c != '']
            out.append(row)
        self.data = [[int(cell.split()[0]) for cell in row] for row in out]
        # initial grid digits different from first and last
        self.constants = [[int(cell.split()[0]) for cell in row if int(cell.split()[0]) > 0] for row in out]
        self.vector = [[cell.split()[1] for cell in row if len(cell.split()) > 1] for row in out]
        self.vector[self.dim - 1].append('END')
