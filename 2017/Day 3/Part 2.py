from aocd import get_data
inp = int(get_data(day=3, year=2017))
print(inp)

class Grid:
    grid = [
        [0, 2],
        [1, 1],
    ]
    def print(self):
        [print(row) for row in self.grid]
    def addBottom(self):
        self.grid.append([0 for x in range(len(self.grid[0]))])
    def addRight(self):
        [self.grid[i].append(0) for i in range(len(self.grid))]
    def addTop(self):
        self.grid.insert(0,[0 for x in range(len(self.grid[0]))])
    def addLeft(self):
        [self.grid[i].insert(0,0) for i in range(len(self.grid))]
    def getNextValue(self, x, y):
        tot = 0
        for i in [x-1, x, x+1]:
            for j in [y-1, y, y+1]:
                if -1 not in [i,j]: # To deal with reverse indexing
                    try:
                        tot += self.grid[j][i]
                    except IndexError:
                        pass
        return tot
    def getNextPosition(self, x, y):
        for i in [x-1, x, x+1]:
            for j in [y-1, y, y+1]:
                try:
                    if self.grid[j][i] == 0 and -1 not in [i, j]: # To deal with reverse indexing
                        return (i, j)
                except IndexError:
                    pass
        if x == 0 and y == 0: # Top left
            self.addLeft()
            return (0, 0)
        elif x == 0 and y == (len(self.grid) - 1): # Bottom left
            self.addBottom()
            return (0, y+1)
        elif x == (len(self.grid[0]) - 1) and y == (len(self.grid) - 1): # Bottom right
            self.addRight()
            return (x+1, y)
        elif x == (len(self.grid[0]) - 1) and y == 0: # Top right
            self.addTop()
            return (x, 0)
    def generateUpTo(self, i):
        if i < 1:
            return 1
        elif i == 1:
            return 2
        x = 1
        y = 0
        while self.grid[y][x] < i:
            x,y = self.getNextPosition(x, y)
            self.grid[y][x] = self.getNextValue(x,y)
        self.print()
        return self.grid[y][x]

g = Grid()
print(g.generateUpTo(inp))