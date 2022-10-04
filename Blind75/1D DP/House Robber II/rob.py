class Solution:
    def rob(self, nums: list[int]) -> int:
        big = max(self.robber1(nums[1:]), self.robber1(nums[:-1]))
        ans = max(nums[0], big)
        return ans
        
    
    def robber1(self, nums: list[int]):
        
        rob1, rob2 = 0,0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    
if __name__ == "__main__":
    nums = [1,2,3,1]
    obj = Solution()
    print(obj.rob(nums))