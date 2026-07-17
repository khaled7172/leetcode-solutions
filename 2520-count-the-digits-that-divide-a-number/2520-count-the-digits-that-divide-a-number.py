class Solution:
    def countDigits(self, num: int) -> int:
        if num == 0:
            return 0
        count = 0
        tmp = num #tmp = 121
        while(num):#121
            last_digit = num % 10 # gets last digit 1
            if tmp % last_digit == 0: #121 % 1 yes
                count += 1#increment the count
            num //= 10 # integer divide to remove last digit from number
        return count        
        