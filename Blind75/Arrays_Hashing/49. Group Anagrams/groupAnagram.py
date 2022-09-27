class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = []
        d = []
        for word in strs:
            innerD = {}
            for letter in word:
                if letter not in innerD:
                    innerD[letter] = 1
                else:
                    innerD[letter] += 1
            if innerD not in d:
                d.append(innerD)
                newList = [word]
                ans.append(newList)
            else:
                ans[d.index(innerD)].append(word)
        return ans
    
if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    obj = Solution()
    print(obj.groupAnagrams(strs))