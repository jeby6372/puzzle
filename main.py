from models.exception import PathCompleted, EmptyPath, CellFound
from models.matrix import Matrix, Cell
from process import Process
from runner import Runner
from scanner import PathScanner

conf_7 = '''7
1 O;0 ZO;0 Z;0 ZW;0 O;0 W;0 ZW;
0 O;0 ZO;0 ZO;0 W;0 ZW;0 W;0 Z;
0 O;0 ZO;0 W;0 Z;0 NW;0 Z;0 ZW;
0 N;0 O;0 W;0 Z;0 NO;0 N;0 NW;
0 O;0 O;0 ZW;0 W;0 NW;0 N;0 ZW;
0 NO;0 O;0 N;0 NW;0 W;0 ZO;0 NW;
0 O;0 NW;0 NO;0 W;0 N;0 NW;49;
'''
conf_5 = '''5
1 Z;0 O;0 ZO;0 W;0 W;
0 NO;0 ZO;0 O;0 Z;0 ZW;
0 ZO;0 ZW;0 N;0 ZW;0 ZW;
17 N;0 NO;0 NW;0 NW;0 N;
0 O;0 W;0 W;0 NO;25;
'''
conf_3 = '''3
1 ZO;0 ZW;0 Z;
0 Z;0 N;0 N;
0 O;0 NO;9;'''

if __name__ == '__main__':
    # conf = Array(sys.argv[1:]).join()
    # with open('input.txt') as f:
    #   conf = f.read()
    matrix = Matrix(conf_3)
    scanner = PathScanner(matrix.data)
    print('-> data', matrix.data)
    print('-> vector', matrix.vector)

    # Input cell
    y = 3  # row
    x = 1  # col
    ref = Cell(y, x, matrix.data[y][x])

    result = scanner.scan[matrix.vector[ref.row][ref.col]](ref)
    for c in result:
        print(c.__dict__)

