class Solution {
    public int maxProfit(int[] prices) {
        int buy = 0, profit = 0, tempProfit = 0;

        for (int i = 0; i < prices.length; i++) {
            if (i == 0) {
                buy = prices[i];
                continue;
            }

            if (prices[i] < buy)
                buy = prices[i];

            if (prices[i] > buy)
                tempProfit = prices[i] - buy;

            if (tempProfit > profit)
                profit = tempProfit;

            tempProfit = 0;
        }

        return profit;
    }
}