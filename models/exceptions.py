class Completed(Exception):

    def __init__(self, expression):
        self.expression = expression
