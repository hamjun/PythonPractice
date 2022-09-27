class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        largest = 0
        for num in nums:
            big = 1
            if num - 1 not in nums:
                while(num + big) in nums :
                    big += 1  
            largest = max(largest, big)
        return largest


if __name__ == "__main__":
    nums = [0,3,7,2,5,8,4,6,0,1]
    obj = Solution()
    assert (obj.longestConsecutive(nums) == 9)
    print("passed")