class EmptyPath(Exception):

    def __init__(self, expression, message=None):
        self.expression = expression
        self.message = message


class PathCompleted(Exception):

    def __init__(self, expression):
        self.expression = expression
