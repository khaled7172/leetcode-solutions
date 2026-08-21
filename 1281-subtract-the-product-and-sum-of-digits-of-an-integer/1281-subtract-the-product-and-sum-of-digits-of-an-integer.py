class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        digits = list(map(int, str(n)))
        print(digits)
        for d in digits:
            sum += d
            product *= d
        return product - sum

        