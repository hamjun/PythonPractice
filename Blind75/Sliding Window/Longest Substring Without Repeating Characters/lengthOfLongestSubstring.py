class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        window = set()
        slow = 0
        for fast in range(len(s)):
            while s[fast] in window:
                window.remove(s[slow])
                slow += 1
            window.add(s[fast])
            ans = max(ans, fast - slow + 1)
        return ans
    
if __name__ == "__main__":
    s = "abcabcbb"
    obj = Solution()
    print(obj.lengthOfLongestSubstring(s))