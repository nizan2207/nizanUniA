import SubGrid
""" find the column number function it get the number of the ubgrid and the column inside of it"""
def find_column(i,y):
    #i is the index of the internal subgrid and the y is the index of the column in the internal subgrid
    if i % 3 == 0:# the column is the same as y
        return y
    elif i==1 or i == 4 or i == 7:#the column is the y + 3
        return y+3
    elif i == 2 or i == 5 or i == 8:#the column is the y + 6
        return y+6
class Grid:
    """ building the object grid"""
    def __init__(self, sub_grids=None) :
        self.rows = [[],[],[],[],[],[],[],[],[]]
        self.column = [[],[],[],[],[],[],[],[],[]]
        self.sub_grids = []
        for i in range(9):
            self.sub_grids.append(SubGrid.SubGrid(i))
        if len(sub_grids)>0:
            for i in range(len(sub_grids)):
                self.sub_grids[sub_grids[i].i] = sub_grids[i]
    """ updating the values of the subgrid so we can solve the problem"""
    def update_values(self):
        for i in range(9):
            for j in range(3):
                for y in range(3):
                    if len((self.sub_grids[i])[j][y].values) == 1: 
                        if i >=0 and i <3:# the rows are the same as the j
                            if (self.sub_grids[i])[j][y].values[0] not in self.rows:
                                self.rows[j] = (self.sub_grids[i])[j][y].values[0]
                            if (self.sub_grids[i])[j][y].values[0] not in self.column:
                                self.column[find_column(i,y)] = (self.sub_grids[i])[j][y].values[0]
                        elif i >=3 and i <6:# the rows are the j+3
                            if (self.sub_grids[i])[j][y].values[0] not in self.rows:
                                self.rows[j+3] = (self.sub_grids[i])[j][y].values[0]
                            if (self.sub_grids[i])[j][y].values[0] not in self.column:
                                self.column[find_column(i,y)] = (self.sub_grids[i])[j][y].values[0]
                        elif i >=6:#the rows are the j+6
                            if (self.sub_grids[i])[j][y].values[0] not in self.rows:
                                self.rows[j+6] = (self.sub_grids[i])[j][y].values[0]
                            if (self.sub_grids[i])[j][y].values[0] not in self.column:
                                self.column[find_column(i,y)] = (self.sub_grids[i])[j][y].values[0]
                        
    """ remove the wrong values of the subgrids"""          
    def remove_values(self, cell, grid_num):
        index_i = 0
        index_j = 0
        for i in range(3):
            for j in range(3):
                if self.sub_grids[grid_num][i][j] == cell:
                    index_i = i
                    index_j = j
                    break
        if index_i >=0 and index_i<3:
            for i in range(len(cell.values)):
                if cell.values[i] in self.rows[index_i]:
                    cell.values.remove(cell.values[i])
        if index_i >=3 and index_i<6:
            for i in range(len(cell.values)):
                if cell.values[i] in self.rows[index_i+3]:
                    cell.values.remove(cell.values[i])
        if index_i >=6 and index_i<8:
            for i in range(len(cell.values)):
                if cell.values[i] in self.rows[index_i+3]:
                    cell.values.remove(cell.values[i])
        for i in range(cell.values):
            if cell.values[i] in self.column[find_column(grid_num,index_j)]:
                cell.values.remove(cell.values[i])
        self.update_values()
    """ the function check the possobelites of th8e values that are true"""
    def check_possibilities(self):
        for i in range(9):
            self.sub_grids[i].check_cells_possibilities()
        self.update_values()
        for i in range(9):
            for j in range(3):
                for y in range(3):
                    self.remove_values((self.sub_grids[i])[j][y],i)
    """check if it is a solved grid solve the grid"""
    def is_solved(self):
        for i in range(9):
            for j in range(3):
                for y in range(3):
                    if len(self.sub_grids[i].grid[j][y].values) != 1:
                        return False
        return True
    """ solve the grid"""
    def solve(self):
        while self.is_solved() == False:
            self.check_possibilities
    """ print the grid object"""
    def __repr__(self):
        res = ''
        for i in range(9):
            if i % 3 == 0:
                res = res + '\n\n'
            for j in range(9):
                if j % 3 == 0:
                    res = res + '    '
                res = res + str(self.sub_grids[3 * int(i / 3)+ int(j / 3)].grid[i % 3][j % 3]) + ' '
            res = res + '\n'
        return res