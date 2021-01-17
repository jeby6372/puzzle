from models.exceptions import Completed, InvalidPath, ConstantMismatch
from models.matrix import Matrix
from resolver import Resolver

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


def revert():
    # remove edge from current node and from parent if single
    i = -1
    # print('reverting path 1/2 i=', i, path)

    if len(path) > 0:
        node = path[i]
        print('removing edge to', r.tree_map[node][r.tree_map[node].index(cell)], 'from node', node)
        del (r.tree_map[node][r.tree_map[node].index(cell)])

    while True:
        # remove parent edge
        if len(r.tree_map[node]) == 0:
            parent = path[i - 1]
            print('removing parent edge to', r.tree_map[parent][r.tree_map[parent].index(node)], 'from node', parent)
            del (r.tree_map[parent][r.tree_map[parent].index(node)])
            print(r.tree_map[parent])
            i -= 1
            node = path[i]
        else:
            break

    print('tree', r.tree_map)


def print_output():
    print('--------------------')
    for data in matrix.data:
        print('\t'.join([str(d) for d in data]))
    print('--------------------')


if __name__ == '__main__':
    # conf = Array(sys.argv[1:]).join()
    # with open('input.txt') as f:
    #   conf = f.read()

    matrix = Matrix(conf_5)
    r = Resolver(matrix)
    path = None
    cell = None
    print('-> data', matrix.data)
    print('-> vector', matrix.vector)
    print('-> constants', matrix.constants)
    print('-> tree', r.tree_map)
    print('start', r.current_cell.__dict__)
    index = 0

    # while index <= 9:
    #     index += 1
    while True:
        try:
            r.set_entry_cell()
            r.walk()
        except Completed as e:
            for r in e.expression:
                print(' '.join(str(i) for i in r))
            exit(0)

        except InvalidPath as e:
            print('invalid path', e.message, 'to target', e.expression)
            path = e.message
            cell = e.expression
            # print('with tree', r.tree_map)
            revert()
            print_output()
            matrix.refresh()


        except ConstantMismatch as e:
            print('constant mismatch in', e.expression, 'using path', e.message)
            path = e.message
            cell = e.expression
            revert()
            matrix.refresh()
