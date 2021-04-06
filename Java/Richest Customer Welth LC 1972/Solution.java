class Solution {

    public static void main(String[] args) {
        // Define 2D array test case
        int[][] twoD_arr = { { 1, 2, 3 }, { 3, 2, 1 } };
        int a = maximumWealth(twoD_arr);
        System.out.println(a);
    }

    public static int maximumWealth(int[][] accounts) {
        int maxsum = 0;
        for (int i = 0; i < accounts.length; i++) {

            int sum = 0;
            for (int j = 0; j < accounts[i].length; j++) {
                sum += accounts[i][j];
            }
            if (sum > maxsum) {
                maxsum = sum;
            }
        }
        return maxsum;
    }
}