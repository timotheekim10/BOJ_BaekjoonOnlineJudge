import java.io.*;
import java.util.*;

class Main {
    static int n, k, ans;
    static int[] arr;
    static boolean[] visited;

    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        
        visited = new boolean[n];
        ans = 0;
        backtracking(0, 500);
        System.out.println(ans);
    }

    private void backtracking(int cnt, int sum) {
        if (cnt == n) {
            ans++;
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i] && sum + arr[i] - k >= 500) {
                visited[i] = true;
                backtracking(cnt + 1, sum + arr[i] - k);
                visited[i] = false;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}