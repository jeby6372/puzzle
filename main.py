from mapper import Mapper
from matrix import Matrix, Cell

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
    # conf = Array(sys.argv[1])
    matrix = Matrix(conf_3)
    print('-> data', matrix.data)
    print('-> vector', matrix.vector)
    mapper = Mapper(matrix)

    for ri, row in enumerate(matrix.vector):
        for ci, col in enumerate(row):
            cell = Cell(ri, ci, matrix.data[ri][ci])
            # print('check', cell.__dict__)
            mapper.scan[matrix.vector[ri][ci]](cell)
            matrix.available = []

    print(matrix.graph)
    for slot in matrix.graph:
        print(slot.__dict__)
        # for k, v in slot:
        #     print('cell', k.__dict__)
        #     for c in v:
        #         print('available', c.__dict__)
