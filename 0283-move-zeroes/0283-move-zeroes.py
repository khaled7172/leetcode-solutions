class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                del nums[i]
                zero_count += 1
        for _ in range(zero_count):
            nums.append(0)

        