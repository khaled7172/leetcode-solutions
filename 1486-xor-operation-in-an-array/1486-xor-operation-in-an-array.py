class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums: List[int] = list(range(n))
        result = 0
        for i in range(n):
            result ^= start + 2 * i
        return result
        