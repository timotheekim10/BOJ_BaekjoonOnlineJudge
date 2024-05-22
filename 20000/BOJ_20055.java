import java.util.*;
import java.io.*;

class Main {
    static int n, k;
    static int[] a;
    static boolean[] r;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        a = new int[2*n];
        r = new boolean[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 2*n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }
        System.out.println(solution());
    }

    static int solution() {
        int ans = 0;

        while (isPossible()) {
            int temp = a[2*n-1];
            for (int i = 2*n-1; i > 0; i--) {
                a[i] = a[i-1];
            }
            a[0] = temp;

            for (int i = n-1; i > 0; i--) {
                r[i] = r[i-1];
            }
            r[0] = false;
            r[n-1] = false;

            for (int i = n-1; i > 0; i--) {
                if (r[i-1] && !r[i] && a[i]>=1) {
                    a[i] -= 1;
                    r[i] = true;
                    r[i-1] = false;
                }
            }

            if (a[0] > 0) {
                r[0] = true;
                a[0] -= 1;
            }
            ans += 1;
        }

        return ans;
    }

    static boolean isPossible() {
        int cnt = 0;
        for (int i = 0; i < 2*n; i++) {
            if (a[i] == 0) {
                cnt += 1;
            }
            if (cnt >= k) {
                return false;
            }
        }
        return true;
    }
}