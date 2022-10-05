from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        res = ""
        resLen = float("inf")
        left = 0
        
        sDict = defaultdict(lambda : 0)
        tDict = defaultdict(lambda : 0)
        
        for element in t:
            tDict[element] += 1
        
        left = 0
        have, need = 0, len(tDict)
        for right in range(len(s)):
            sDict[s[right]] += 1
            if sDict[s[right]] == tDict[s[right]]:
                have += 1
                
            #remove from left if all conditions are met
            #until condition is no longer true
            while have == need:
                if right - left + 1 < resLen:
                    res = s[left:right+1]
                    resLen = right - left + 1
                sDict[s[left]] -= 1
                if sDict[s[left]] < tDict[s[left]]:
                    have -= 1
                left += 1
        
        return res if resLen != float("inf") else ""
                
            
if __name__ == "__main__":
    obj = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(obj.minWindow(s, t))