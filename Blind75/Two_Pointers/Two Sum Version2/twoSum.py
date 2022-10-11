class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l , r = 0, len(numbers) - 1
        
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        assert("error")
        
if __name__ == "__main__":
    obj = Solution()
    numbers = [-1,0]
    target = -1
    print(obj.twoSum(numbers, target))