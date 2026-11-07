class KthLargest {
    private  PriorityQueue<Integer> minHeap;
    private  int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.minHeap = new PriorityQueue<>((a,b) -> a - b);
        buildHeap(nums);
        
    }

    private  void heapPop() {
        if(this.minHeap.size() > this.k) {
            this.minHeap.poll();
        }
    }

    private void buildHeap(int[] nums) {
        for(int i = 0; i < nums.length; i++) {
            this.minHeap.offer(nums[i]);
            heapPop();
        }

    }
    
    public int add(int val) {
        this.minHeap.offer(val);
        heapPop();
        return this.minHeap.peek();
    }
}
