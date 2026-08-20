class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # equilateral if 3 sides of eq len
        # isosceles if 2 sides only are eq len
        # scalene if all sides have diff len
        num1= nums[0]
        num2 = nums[1]
        num3 = nums[2]
        s1 = num1 + num2
        s2 = num1 + num3
        s3 = num2 + num3
        if (s1 > num3 and s2 > num2 and s3 > num1): 
            if num1 == num2 and num2 == num3:
                return "equilateral"
            if num1 != num2 and num1 != num3 and num2 != num3:
                return "scalene"
            else:
                return "isosceles"
        return "none"