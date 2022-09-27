import unittest

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
    
if __name__ == "__main__":
    nums = [1,2,3,4]
    obj = Solution()
    assert (obj.productExceptSelf(nums) == [24, 12, 8, 6])
    print("passed")