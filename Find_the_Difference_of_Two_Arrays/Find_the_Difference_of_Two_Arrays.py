class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = {x for x in nums1}
        set2 = {y for y in nums2}
        set_1_2 = set1.difference(set2)
        set_2_1 = set2.difference(set1)
        answer = (set_1_2 , set_2_1)
        return answer