class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        d_sum = 0
        s_sum = 0
        for num in nums:
            if 0 <= num <= 9:
                s_sum += num
            else:
                d_sum += num
        if s_sum > d_sum or d_sum > s_sum:
            return True
        else:
            return False


        