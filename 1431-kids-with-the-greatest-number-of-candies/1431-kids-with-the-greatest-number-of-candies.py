class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        greatest = candies[0]
        result = []
        for candy in candies:
            if candy > greatest:
                greatest = candy
        for cn in candies:
            if (cn + extraCandies) >= greatest:
                result.append(True)
            else:
                result.append(False)
        return result        