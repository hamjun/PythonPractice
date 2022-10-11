class Solution:
    def trap(self, height: list[int]) -> int:
        
        l, r  = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        ans = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                
                leftMax = max(leftMax, height[l])
                ans += leftMax - height[l]
            else:
                r -= 1
                
                rightMax = max(rightMax, height[r])
                ans += rightMax - height[r]
        return ans
    
if __name__ == "__main__":
    obj = Solution()
    height = [4,2,0,3,2,5]
    print(obj.trap(height))