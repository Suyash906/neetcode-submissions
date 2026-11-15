class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        if n < 3:
            return min(cost)

        dp1 = 0
        dp2 = 0
        min_cost = 0
        for i in range(2, n + 1):
            min_cost = min(dp1 + cost[i-1], dp2 + cost[i - 2])
            dp2 = dp1
            dp1 = min_cost

        return min_cost