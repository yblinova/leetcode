class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        amount = 0
        j = n - 1
        i = 0

        while i < j:
            amount = max(amount , min(height[i], height[j])*(j-i))

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
                
        return amount