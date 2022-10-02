class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #DP START AT THE END!
        #bottom
        bottomRow = [1] * n
        
        #log is is messed up but we only need the number of rows 
        for i in range(m - 1):
            #current = current right + current bottom
            row = [1] * n
            for j in range(n - 2, -1, -1):
                row[j] = row[j + 1] + bottomRow[j]
            bottomRow = row
            
        return bottomRow[0]
    
if __name__ == "__main__":
    m = 3
    n = 7
    obj = Solution()
    print(obj.uniquePaths(n, m))