class Solution {
    public int hammingWeight(int n) {
        String bit = Integer.toBinaryString(n);
        int ans = 0;

        for (int i = 0; i < bit.length(); i++) {
            if (bit.charAt(i) == '1')
                ans++;
        }

        return ans;
    }
}