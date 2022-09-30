class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        prof = 0
        left = 0
        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            prof = max(prof, prices[right] - prices[left])
            #print(left, right, prof)
        return prof

if __name__ == "__main__":
    nums = [7,1,5,3,6,4]
    obj = Solution()
    print(obj.maxProfit(nums))