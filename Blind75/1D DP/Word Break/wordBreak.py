class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        #if reach end it is true
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if len(w) + i <= len(s) and w == s[i:i+len(w)]:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
        
if __name__ == "__main__":
    obj = Solution()
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    print(obj.wordBreak(s, wordDict))