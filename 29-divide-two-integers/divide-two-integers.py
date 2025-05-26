class Solution:
    def divide(self, dividend, divisor):
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        
        for shift in range(31, -1, -1):
            if (dividend >> shift) >= divisor:
                dividend -= divisor << shift
                quotient += 1 << shift

        
        quotient = quotient if sign > 0 else -quotient

       
        return max(min(quotient, INT_MAX), INT_MIN)
