from threading import Thread

from scanner import PathScanner

'''
path discovering for one cell
'''


class Process(Thread):
    matrix = None
    cell = None
    scanner = None
    data = []

    def __init__(self, matrix, cell):
        super().__init__(daemon=True)
        self.matrix = matrix
        self.cell = cell
        self.scanner = PathScanner(matrix)
        self.name = str(cell.row) + '_' + str(cell.col)
        # super().__init__(length, length)

    '''
        try:
            p.run()
        except PathCompleted as pc:
            print(pc.expression)
        except EmptyPath as ep:
            print('Empty path for', ep.expression)
    '''

    def run(self):
        print('running', self.name)
        self.scanner.scan[self.matrix.vector[self.cell.row][self.cell.col]](self.cell)
