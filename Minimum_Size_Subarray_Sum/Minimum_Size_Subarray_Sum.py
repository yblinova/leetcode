class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end, _sum, min_len = 0 , 0 , 0, len(nums) + 1

        while end < len(nums):
            _sum += nums[end]
            end += 1
            while _sum >= target:
                min_len = min(min_len, end - start)
                _sum -= nums[start]
                start+= 1
        return min_len if min_len != len(nums) + 1 else 0