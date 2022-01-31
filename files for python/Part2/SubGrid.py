import Cell
class SubGrid:
    """ biulding the subgrid object"""
    def __init__(self, i, cells=None) :
        self.i = i
        self.cells = cells
        self.grid = [[],[],[]]
        self.collected_values = []
        #if self.cells == None:
        for i in range(3):
            for j in range(3):
                self.grid[i].append(Cell.Cell(i,j))
        if self.cells != None:
            for i in range(3):
                for j in range(3):
                    for x in self.cells:
                        if x.i == i and x.j == j and x.values!=None:
                            self.grid[i][j] = Cell.Cell(i,j,x.values)
                            self.collected_values.append(x.values)
                        else:
                            self.grid[i][j] = Cell.Cell(i,j)
    """ updating the value of the cells in the subgrid"""
    def update_values(self):
        temp = []
        for i in range(3):
            for j in range(3):
                if len(self.grid[i][j].values) == 1:
                    temp.append(self.grid[i][j].values)
        for i in range(temp):
            if temp[i] not in self.collected_values:
                self.collected_values.append(temp[i])
    """ remove the values that are not right from the cells"""
    def remove_values(self, cell):
        if len(cell.values) > 1:
            for i in cell.values:
                if i in self.collected_values:
                    cell.values.remove(i)
        self.update_values()
    """ check the possiblties for the values inside of the cells"""
    def check_cells_possibilities(self):
        for i in range(3):
            for j in range(3):
                self.remove_values(self.grid[i][j])
    