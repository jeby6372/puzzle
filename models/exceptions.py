class Completed(Exception):

    def __init__(self, expression):
        self.expression = expression


class InvalidPath(Exception):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class ConstantMismatch(Exception):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
