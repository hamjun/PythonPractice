class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        ans = 0
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            d[s[r]] = 1 + d.get(s[r], 0) #default 0
            maxf = max(maxf, d[s[r]])
            while (r-l+1) - maxf > k: #window - most freq
                d[s[l]] -= 1
                l += 1
            ans = max(r-l+1, ans)
        return ans
    
if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    obj = Solution()
    print(obj.characterReplacement(s, k))