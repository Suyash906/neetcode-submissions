class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        local_sum = 0
        global_sum = float('-inf')

        for num in nums:
            local_sum += num

            if local_sum < num:
                local_sum = num

            if local_sum > global_sum:
                global_sum = local_sum


        return global_sum