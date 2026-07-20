class Solution(object):
    def setZeroes(self, matrix):
        rows=len(matrix)
        colm=len(matrix[0])
        row_set=set()
        col_set=set()
        for i in range(0,rows):
            for j in range(0,colm):
                if matrix[i][j]==0:
                    row_set.add(i)
                    col_set.add(j)
        for r in row_set:
            for c in range(0,colm):
                matrix[r][c]=0
        for c in col_set:
            for r in range(0,rows):
                matrix[r][c]=0
        

