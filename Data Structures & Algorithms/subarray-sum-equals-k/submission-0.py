class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        cumalativeSum = 0
        count = 0
        seen = {0:1}

        for num in nums:
            cumalativeSum += num
            if cumalativeSum - k in seen:
                count += seen[cumalativeSum - k]
            seen[cumalativeSum] = seen.get(cumalativeSum, 0) + 1
        
        return count