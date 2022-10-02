class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0,0
        
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

if __name__ == "__main__":
    nums = [2,7,9,3,1]
    obj = Solution()
    print(obj.rob(nums))