class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        count=0
        if grid[0][0] !=0 or grid[n-1][n-1]!=0:
            return -1
        i=0
        j=0
        
        def func(grid, x,y):
            if x<n and y<n:
                if grid[x][y]==0:
                    return 1
            else:
                return -1
        while i<n and j<n :

            if grid[i][j]==0:
                count+=1

            if func(grid,i+1,j):
                
                i+=1
            elif func(grid,i+1,j+1):
                
                i+=1
                j+=1
            elif func(grid,i,j+1):
                j+=1
            else :
                return -1
            
            if i==n-1 and j==n-1:
                break
                
        if i== n-1 and j== n-1 and grid[i][j]==0:
            return count +1
        else:
            return -1
            
        
        
