class Matrix():
    def __init__(self, R , C):
        self.rows = R
        self.cols = C
        self.matrix = [['@']*C for i in range(R)]
    def draw(self):
        for row in self.matrix:
            print (' '.join(row))
    def set_value(self, R, C, V):
        try:
            self.matrix[R][C] = V
        except:
            #print('Where are you setting?', R, C)
            pass
    def get_value(self, R, C):
        try:
            return self.matrix[R][C]
        except:
            return None
    def get_neigbours(self, r, c):
        #R = self.rows
        #C = self.cols
        neighbors = []
        #neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2) for y2 in range(y-1, y+2) if -1 < x <= X and -1 < y <= Y and (x != x2 or y != y2)]
        if self.rows > 1:
            if self.cols > 1:
                if (r-1>=0):
                    if(c-1>=0):
                        neighbors.append((r-1, c-1))
                    neighbors.append((r-1, c))
                    neighbors.append((r-1, c+1 % C))
                if (c-1>=0):
                    neighbors.append((r+1 % R, c-1))
                neighbors.append((r+1 % R, c))
                neighbors.append((r+1 % R, c+1 % C))
                if (c-1>=0):
                    neighbors.append((r, c-1))
                neighbors.append((r, c+1 % C))
            else:
                if (r-1>=0):
                    neighbors.append((r-1, c))
                neighbors.append((r+1 % R, c))
        else:
            if self.cols > 1:
                if (c-1>=0):
                    neighbors.append((r, c-1))
                neighbors.append((r, c+1 % C))
        return neighbors
