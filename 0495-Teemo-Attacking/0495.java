class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        int total = 0;

        for (int i = 0; i < timeSeries.length - 1; i++) {
            int pois = Math.min(timeSeries[i + 1] - timeSeries[i], duration);
            total += pois;
        }

        return total + duration;
    }
}