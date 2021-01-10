from models.exception import PathCompleted, EmptyPath, CellFound
from models.scanner import PathScanner
from matrix import Matrix, Cell
from models.process import Process

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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # conf = Array(sys.argv[1:]).join()
    # with open('input.txt') as f:
    #   conf = f.read()
    matrix = Matrix(conf_7)
    print('-> data', matrix.data)
    print('-> vector', matrix.vector)

    # Input cell
    x = 0
    y = 0
    ref = Cell(y, x, matrix.data[y][x])
    p = Process(matrix, ref)


    # Test
    try:
        p.run()
    except PathCompleted as pc:
        print('path', [(c.row, c.col) for c in pc.expression])
    except EmptyPath as ep:
        print('Empty path for', ep.expression)
    except CellFound as cf:
        print('Cell found', cf.expression.row, cf.expression.col, cf.expression.value)
        matrix.data[cf.expression.row][cf.expression.col] = ref.value + 1

    print('output', matrix.data)

    # for ri, row in enumerate(matrix.vector):
    #     for ci, col in enumerate(row):
    #         cell = Cell(ri, ci, matrix.data[ri][ci])
    #         # print('check', cell.__dict__)
    #         mapper.scan[matrix.vector[ri][ci]](cell)
    #         matrix.path = []

