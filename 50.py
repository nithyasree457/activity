class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        for i in range(n):
            result *= x
        
        return result
