class EmptyPath(Exception):

    def __init__(self, expression):
        self.expression = expression


class PathCompleted(Exception):

    def __init__(self, expression):
        self.expression = expression


class CellFound(Exception):

    def __init__(self, expression):
        self.expression = expression


class Completed(Exception):

    def __init__(self, expression):
        self.expression = expression
