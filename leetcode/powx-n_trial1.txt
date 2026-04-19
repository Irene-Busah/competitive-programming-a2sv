class Solution:
    def myPow(self, x: float, n: int) -> float:
        def powCal(x, n):
            if (n == 0): return 1
            if (x == 0): return 0
            
            result = powCal(x * x, n//2)
            
            
            return x * result if n % 2 else result
                
        answer = powCal(x, abs(n))
        return answer if n >= 0 else 1 / answer