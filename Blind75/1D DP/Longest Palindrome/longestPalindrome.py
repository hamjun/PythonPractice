class Solution:
    def longestPalindrome(self, s: str) -> str:
        #find the center
        ans = ""
        ansLen = 0
        for i in range(len(s)):
            #odd cases first
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                temp = s[l:r+1]
                if len(temp) > ansLen:
                    ans = temp
                    ansLen = len(ans)
                
                #update pointers
                l -= 1
                r += 1
                
            #even cases
            l, r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                temp = s[l:r+1]
                if len(temp) > ansLen:
                    ans = temp
                    ansLen = len(ans)
                
                #update pointers
                l -= 1
                r += 1
            
        return ans
    
if __name__ == "__main__":
    s = "babad"
    obj = Solution()
    print(obj.longestPalindrome(s))