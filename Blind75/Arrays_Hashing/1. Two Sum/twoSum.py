class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in d:
                return [ d[diff], i]
            d[num] = i
            
if __name__ == "__main__":
    nums = [3,2,4] 
    target = 6
    obj = Solution()
    print(obj.twoSum(nums, 6))
