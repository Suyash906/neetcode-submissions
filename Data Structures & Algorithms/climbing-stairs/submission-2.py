class Solution:
    def helperRecursion(self, n) -> int:
        result = 0
    
        def helper(n):
            nonlocal result
            if n == 0:
                result += 1
            if n < 0:
                return
            
            helper(n-1)
            helper(n-2)

        helper(n)

        return result

    def helper_dp(self, n):

        if n < 3:
            return n

        f1 = 1
        f2 = 2
        i = 2
        while i < n:
            f = f1 + f2
            f1 = f2
            f2 = f
            i += 1

        return f2

    def climbStairs(self, n: int) -> int:
        return self.helper_dp(n)
        