class Plot:
    def __init__(self,*arg,**kwargs):
        self.col = kwargs['col']
        self.row = kwargs['row']
        self.mat = [[0 for i in range(self.col)] for i in range(self.row)]
    def mark(self,points):
        for (row,col) in points:
            self.mat[row][col] = '*'
    def print(self):
        for row in reversed(range(len(self.mat))):
            for col in range(len(self.mat[0])):
                if(col == 0):
                    print("|",end="")
                    continue
                if(row == 0):
                    print("-",end="")
                    continue
                if(self.mat[row][col]==0):
                    print(" ",end="")
                    continue
                print(self.mat[row][col],end="")
            print()

if __name__ == "__main__":
    p = Plot(row=8,col=8)
    points = [(3,4),(4,4),(5,7),(2,3)]
    p.mark(points)
    p.print()
