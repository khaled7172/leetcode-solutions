class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # 1 if x > 0
        # -1 if x < 0
        # 0 if x == 0
        product = 1
        for num in nums:
            product *= num
        if product == 0:
            return 0
        elif product < 0:
            return -1
        else:
            return 1
        