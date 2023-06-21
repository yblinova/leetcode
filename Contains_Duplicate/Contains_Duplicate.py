class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset = set(nums)
        if len(nums) != len(myset):
            return True
        else:
            return False