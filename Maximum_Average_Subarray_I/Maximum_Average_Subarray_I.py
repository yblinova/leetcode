class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if k > n:
            return -1
        csum = [0]*n
        csum[0] = nums[0]
        for i in range(1, n):
            csum[i] = csum[i-1] + nums[i]
     
        max_sum = csum[k-1]
        max_end = k-1
    
        for i in range(k, n):
            curr_sum = csum[i] - csum[i-k]
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_end = i

        return (max_sum)/k