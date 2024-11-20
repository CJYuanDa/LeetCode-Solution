class Solution {
    public String[] findRelativeRanks(int[] score) {
        int n = score.length;
        String[] ans = new String[n];
        int[][] pair = new int[n][2];

        // Pair each score with its index
        for (int i = 0; i < n; i++) {
            pair[i][0] = score[i]; // score
            pair[i][1] = i; // index
        }

        // Sort by score in descending order
        Arrays.sort(pair, (a, b) -> b[0] - a[0]);

        // Assign ranks
        for (int i = 0; i < n; i++) {
            int index = pair[i][1];
            if (i == 0) {
                ans[index] = "Gold Medal";
            } else if (i == 1) {
                ans[index] = "Silver Medal";
            } else if (i == 2) {
                ans[index] = "Bronze Medal";
            } else {
                ans[index] = String.valueOf(i + 1);
            }
        }

        return ans;
    }
}