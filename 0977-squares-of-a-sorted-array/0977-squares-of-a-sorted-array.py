class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = []
        for n in nums:
            output.append(n*n)
        return sorted(output)

        