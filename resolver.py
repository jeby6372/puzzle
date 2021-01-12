import sys

from models.exceptions import Completed, ConstantMismatch
from models.matrix import Cell
from scanner import PathScanner


class Resolver(object):
    global_map = {}
    scanner = None
    matrix = None
    graphs_tree = []
    graph_index = 0
    current_cell = None

    def __init__(self, matrix):
        self.matrix = matrix
        self.scanner = PathScanner(matrix.data)
        self.graphs_tree.append([])
        self.current_cell = self.get_entry_cell()
        self.refresh()

    def refresh(self):
        self.graphs_tree[self.graph_index].append((self.current_cell.row, self.current_cell.col))
        for i, row in enumerate(self.matrix.data):
            for j, cell in enumerate(row):
                ref = Cell(i, j, self.matrix.data[i][j])
                if ref.value != pow(self.matrix.dim, 2):
                    self.global_map[(i, j)] = self.scanner.scan[self.matrix.vector[ref.row][ref.col]](ref)

                else:
                    self.global_map[(i, j)] = [Completed(self.matrix.data)]

    def walk(self, graph_index):
        # get cell available edges
        self.graph_index = graph_index
        edges = self.global_map[(self.current_cell.row, self.current_cell.col)]
        print('from', self.current_cell.row, self.current_cell.col, self.current_cell.value)
        # if no cells found : bad path or process completed
        if len(edges) > 0 and not isinstance(edges[0], Completed):
            print('edges', edges)
            row = edges[0][0]
            col = edges[0][1]
            # Check constants

            target = Cell(row, col, self.matrix.data[row][col] + 1)

            if (row, col) in self.matrix.constants and self.matrix.constants[(row, col)] != target.value:
                # wrong path : check next one
                print('constant', self.matrix.constants[(row, col)], 'does not match',target.value,'at', row, col)
                raise ConstantMismatch(self.graphs_tree[self.graph_index], (self.current_cell.row, self.current_cell.col))

            self.matrix.data[target.row][target.col] = target.value
            self.current_cell = target
            self.refresh()
            print(self.global_map)
            self.walk(self.graph_index)
        else:
            raise edges[0]

    def new_graph(self):
        self.graph_index += self.graph_index
        self.graphs_tree.append([])

    def reset_graph(self):
        print(self.graphs_tree[self.graph_index])

    # return lower digit found in the matrix
    def get_entry_cell(self):
        # get lower digit in the matrix (<> 0)
        digit = sys.maxsize
        for i, row in enumerate(self.matrix.data):
            for j, col in enumerate(row):
                if self.matrix.data[i][j] != 0 and self.matrix.data[i][j] < digit:
                    digit = self.matrix.data[i][j]
                    x = i
                    y = j
        return Cell(x, y, self.matrix.data[x][y])
