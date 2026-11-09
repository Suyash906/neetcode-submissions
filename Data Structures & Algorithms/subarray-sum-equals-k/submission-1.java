class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0, sum = 0;
        Map<Integer, Integer> seen = new HashMap<>();
        seen.put(0,1);

        for(int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if(seen.containsKey(sum - k)) {
                count += seen.get(sum - k);
            }
            // seen.put(sum, seen.getOrDefault(sum, 0) + 1);
            seen.merge(sum, 1, Integer::sum);
        }
        return count;
    }
}