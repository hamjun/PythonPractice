class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        ans = set()
        for num in nums:
            if num in ans:
                return True
            ans.add(num)
        return False
    

if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    obj = Solution()
    print(obj.containsDuplicate(nums))

