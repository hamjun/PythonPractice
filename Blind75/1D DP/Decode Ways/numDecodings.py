class Solution:
    #recursive solution
    '''
    def numDecodings(self, s: str) -> int:
        
        #cache, memoization
        #base case if s is empty or len 1
        recur = {len(s) : 1}
        
        def dfs(i):
            #base cases
            #if ans already in cache
            #covers if i is out of range because we initlized len(s) = 1 in the dictionary
            if i in recur:
                return recur[i]
            #illegal
            if s[i] == "0":
                return 0
            
            
            
            #recursion
            numsWaysDecode = dfs(i + 1)
            
            #need two digit case
            if (i+1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456"))):
                numsWaysDecode += dfs(i+2)
                
            #store for future
            recur[i] = numsWaysDecode
            
            #return ans for recursion
            return numsWaysDecode
        
        return dfs(0)
    '''
    #dp solution
    def numDecodings(self, s: str) -> int:
        
        #start reverse
        dp = {len(s) : 1}
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                #move it along 1
                #single digit case
                dp[i] = dp[i+1]
            
            #case where 2 digit add aditional methods
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456")):
                dp[i] += dp[i + 2]
                
        return dp[0]
    
if __name__ == "__main__":
    obj = Solution()
    s = "226"
    print(obj.numDecodings(s))