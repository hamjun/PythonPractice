class Solution:
    def countSubstrings(self, s: str) -> int:
        #similar solution as longest palindrome
        ans = []
        
        for i in range(len(s)):
            #odd cases
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans.append(s[l:r+1])
                
                #update pointers
                l -= 1
                r += 1
            
            #evencases
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans.append(s[l:r+1])
                
                #update pointers
                l -= 1
                r += 1
                
        return len(ans)
    
if __name__ == "__main__":
    obj = Solution()
    s = "abc"
    print(obj.countSubstrings(s))