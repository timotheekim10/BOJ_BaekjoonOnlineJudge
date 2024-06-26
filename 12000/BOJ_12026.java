import java.io.*;
import java.util.*;

class Main {
    static int n;
    static char[] arr;
    static int[] dp;

    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = br.readLine().toCharArray();
        dp = new int[n];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        for (int i = 1; i < dp.length; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] == Integer.MAX_VALUE) {
                    continue;
                }
                if (arr[i] == 'O' && arr[j] == 'B') {
                    dp[i] = Math.min(dp[i], dp[j] + (i - j) * (i - j));
                } else if (arr[i] == 'J' && arr[j] == 'O') {
                    dp[i] = Math.min(dp[i], dp[j] + (i - j) * (i - j));
                } else if (arr[i] == 'B' && arr[j] == 'J') {
                    dp[i] = Math.min(dp[i], dp[j] + (i - j) * (i - j));
                }
            }
        }
        if (dp[n - 1] != Integer.MAX_VALUE) {
            System.out.println(dp[n - 1]);
        } else {
            System.out.println(-1);
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}