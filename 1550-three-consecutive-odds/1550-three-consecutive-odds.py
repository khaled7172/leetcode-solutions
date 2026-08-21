class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        prev_prev_num = arr[0]
        prev_num = arr[1]
        for num in arr[2:]:
            if (num % 2 != 0 and prev_num % 2 != 0 and prev_prev_num % 2 != 0):
                return True
            else:
                prev_prev_num = prev_num
                prev_num = num
        return False



        