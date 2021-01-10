class Cell(object):
    row = 0
    col = 0
    value = None

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


