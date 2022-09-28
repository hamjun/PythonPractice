class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        ans = []
        for i in range(len(nums)-1):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    poten = [nums[i], nums[l] , nums[r]]
                    ans.append(poten)
                    l += 1
                    while (l < r and nums[l] == nums[l-1]):
                        l += 1
                    
                        
        return ans
    
if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    obj = Solution()
    print(obj.threeSum(nums))