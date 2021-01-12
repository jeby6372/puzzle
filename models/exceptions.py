class Completed(Exception):

    def __init__(self, expression):
        self.expression = expression


class ConstantMismatch(Exception):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
