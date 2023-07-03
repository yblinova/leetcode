class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        l, r = float('inf'), float('inf')
        for i in nums:
            if i <= l:
                l = i
            elif i <= r:
                r = i
            else:
                return True
        return False