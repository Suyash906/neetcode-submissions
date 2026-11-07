class Solution {
    public int maxArea(int[] heights) {

        int left = 0, right = heights.length - 1;
        int maxAreaVal = 0;
        while(left < right) {
            int height = Math.min(heights[left], heights[right]);
            int breadth = right - left;
            maxAreaVal = Math.max( height * breadth , maxAreaVal);
            if( heights[left] < heights[right] ) {
                left++;
            } else {
                right--;
            }
        }
        return maxAreaVal;
    }
}
