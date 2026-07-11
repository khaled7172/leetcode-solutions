class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        if len(nums) == 0:
            return
        for i in range(len(nums)):
            if len(nums) == 0:
                continue
            else:
                min_alice = min(nums)
                nums.remove(min_alice)
                min_bob = min(nums)
                nums.remove(min_bob)
                arr.append(min_bob)
                arr.append(min_alice)
        return arr
        