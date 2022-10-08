class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        result = max(nums) #in case there is only 1 negative element
        cMax, cMin = 1,1
        
        for n in nums:
            if n == 0:
                cMax, cMin = 1,1
                continue
            temp = n * cMax
            cMax = max(temp, n * cMin, n)
            cMin = min(temp, n * cMin, n)
            
            result = max(cMax, result)
        
        return result

if __name__ == "__main__":
    obj = Solution()
    nums = [2,3,-2,4]
    print(obj.maxProduct(nums))