class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            #print(left, s[left], right, s[right])
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"

    obj = Solution()
    print(obj.isPalindrome(s))