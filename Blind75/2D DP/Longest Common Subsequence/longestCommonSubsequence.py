class Solution:
    #MINE! :)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        bottomRow = [0] * (len(text1) + 1) # 6
        
        for i in range(len(text2) - 1, -1, -1):         # 2,1,0
            row = [0] * (len(text1) + 1) # 6
            for j in range(len(text1) - 1, -1, -1):     # 4,3,2,1,0
                if text1[j] == text2[i]:
                    row[j] = 1 + bottomRow[j + 1]
                else:
                    row[j] = max(row[j + 1] , bottomRow[j])
                
            bottomRow = row
        return bottomRow[0]
    
    
if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace" 
    obj = Solution()
    print(obj.longestCommonSubsequence(text1, text2))
    '''
    #NEETCODE'S
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]
    '''