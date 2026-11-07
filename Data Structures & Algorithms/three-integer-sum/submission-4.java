class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        Arrays.sort(nums);

        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            int target = -nums[i];
            int start = i + 1;
            int end = nums.length - 1;
            

            System.out.println("i = "+ i + " start = "+start+" end = "+end);
            while(start < end) {
                if(nums[start] + nums[end] == target) {
                    result.add(List.of(nums[i], nums[start], nums[end]));
                    while(i < nums.length -2 && nums[i] == nums[i + 1])i++;
                    
                    while(start < end && nums[start] == nums[start+1]) start++;

                    while(end > start && nums[end] == nums[end - 1]) end--;
                    start++;
                    end--;
                } else if(nums[start] + nums[end] > target) {
                    end--;
                } else {
                    start++;
                }
            }
        }

        return result;
        
    }
}
