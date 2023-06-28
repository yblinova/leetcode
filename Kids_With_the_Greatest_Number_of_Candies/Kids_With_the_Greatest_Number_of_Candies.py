class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        n = len(candies)
        result = candies
        for i in range(n):
            if candies[i] + extraCandies >= max_candies:
                result[i] = True
            elif candies[i] + extraCandies < max_candies:
                result[i] = False
        return result