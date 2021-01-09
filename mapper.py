from matrix import Matrix


class Mapper(object):

    def __init__(self, matrix):

        self.scan = {
            'N': matrix.to_north,
            'NO': matrix.to_north_east,
            'O': matrix.to_east,
            'ZO': matrix.to_south_east,
            'Z': matrix.to_south,
            'ZW': matrix.to_south_west,
            'W': matrix.to_west,
            'NW': matrix.to_north_west
        }
