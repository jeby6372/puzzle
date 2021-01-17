import sys

from models.exceptions import Completed, ConstantMismatch, InvalidPath
from models.matrix import Cell
from scanner import PathScanner


class Resolver(object):
    tree_map = {}
    path = None
    path_index = 0
    scanner = None
    matrix = None
    current_cell = None

    def __init__(self, matrix):
        self.matrix = matrix
        self.scanner = PathScanner(matrix.data)
        self.set_entry_cell()
        # current run path
        self.path = []
        # build global tree paths
        self.init_tree()

    def walk(self):

        # iterates the tree map
        edges = self.tree_map[(self.current_cell.row, self.current_cell.col)]
        print('-> resolving cell', self.current_cell.get_coords())
        print('edges found', edges)
        if len(edges) > 0:
            for row, col in edges:
                target = Cell(row, col, self.current_cell.value + 1)
                print('-> check cell target ', target.get_coords(), 'content',
                      self.matrix.data[target.get_coords()[0]][target.get_coords()[1]])

                if target.value == pow(self.matrix.dim, 2):
                    raise Completed(self.matrix.data)

                # Check constants
                if (row, col) in self.matrix.constants and self.matrix.constants[(row, col)] != target.value:
                    raise ConstantMismatch((row, col), self.path)

                if self.matrix.data[row][col] == 0:
                    # unused cell : OK
                    self.matrix.data[target.row][target.col] = target.value
                    self.current_cell = target
                    break

                raise InvalidPath((row, col), self.path)

            self.path.append((row, col))
            self.walk()

    ''' Build the tree paths mapping'''

    def init_tree(self):

        for i, row in enumerate(self.matrix.data):
            for j, cell in enumerate(row):
                ref = Cell(i, j, self.matrix.data[i][j])
                if ref.value != pow(self.matrix.dim, 2):
                    self.tree_map[(i, j)] = self.scanner.scan[self.matrix.vector[ref.row][ref.col]](ref)

    # return lower digit found in the matrix
    def set_entry_cell(self):
        # get lower digit in the matrix (<> 0)
        self.path = []

        digit = sys.maxsize
        for i, row in enumerate(self.matrix.data):
            for j, col in enumerate(row):
                if self.matrix.data[i][j] != 0 and self.matrix.data[i][j] < digit:
                    digit = self.matrix.data[i][j]
                    x = i
                    y = j
        self.current_cell = Cell(x, y, self.matrix.data[x][y])
