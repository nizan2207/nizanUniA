class Cell:
    """
    building the cell object
    """
    def __init__(self, i, j, value=None):
        self.i = i
        self.j = j
        self.values = []
        self.values.append(value)
        if len(self.values) == 0:
            self.values = [1,2,3,4,5,6,7,8,9]
        
    """ printing the cell object"""
    def __repr__(self):
        if len(self.values) == 1:
            return str(self.values[0])
        return '_'