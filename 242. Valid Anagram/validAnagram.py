class Solution:
    def validAnagram(self, s: str, t: str) -> bool:
        if (len(s) !=  len(t)):
            return False
        for letter in s:
            try:
                t = t.replace(letter, '', 1)
            except:
                return False
        if len(t) == 0:
            return True
        return False

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    obj = Solution()
    print(obj.validAnagram(s, t))