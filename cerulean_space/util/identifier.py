class Identifier:

    def __init__(self, name: str):
        self.name = name

    def __cmp__(self, other):
        if type(other) != type(self):
            return False
        return self.name.__eq__(other.name)
