class NumArray {

    private List<Integer> prefixSum = new ArrayList<>();
    private int sum = 0;

    public NumArray(int[] nums) {
        for (int num : nums) {
            sum += num;
            prefixSum.add(sum);
        }
    }

    public int sumRange(int left, int right) {
        int R = prefixSum.get(right);
        int L = left > 0 ? prefixSum.get(left - 1) : 0;
        return R - L;
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */