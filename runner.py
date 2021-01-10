from copy import deepcopy

from models.exception import PathCompleted, EmptyPath, CellFound
from process import Process


class Runner(object):

    matrix = None

    def __init__(self):
        pass

    def launch(self, matrix, ref):
        self.matrix = deepcopy(matrix)
        p = Process(self.matrix, ref)
        try:
            p.run()
        except PathCompleted as pc:
            print('Paths', [(c.row, c.col) for c in pc.expression])
        except EmptyPath as ep:
            # bad path found : cancel
            print('Empty path for', ep.expression)
        except CellFound as cf:
            print('Cell found', cf.expression.row, cf.expression.col, cf.expression.value)
            matrix.data[cf.expression.row][cf.expression.col] = ref.value + 1