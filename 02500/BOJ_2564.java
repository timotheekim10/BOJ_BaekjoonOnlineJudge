import java.io.*;
import java.util.*;

class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int W = Integer.parseInt(st.nextToken());
        int H = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr.add(new ArrayList<>());
            arr.get(i).add(a);
            arr.get(i).add(b);
        }
        st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int ans = 0;
        for (int i = 0; i < N; i++) {
            if (x == 1) {
                if (arr.get(i).get(0) == 1) {
                    ans += Math.abs(y - arr.get(i).get(1));
                } else if (arr.get(i).get(0) == 2) {
                    ans += H + Math.min(y + arr.get(i).get(1), 2*W - (y+arr.get(i).get(1)));
                } else if (arr.get(i).get(0) == 3) {
                    ans += y + arr.get(i).get(1);
                } else if (arr.get(i).get(0) == 4) {
                    ans += W-y + arr.get(i).get(1);
                }
            } else if (x == 2) {
                if (arr.get(i).get(0) == 2) {
                    ans += Math.abs(y - arr.get(i).get(1));
                } else if (arr.get(i).get(0) == 1) {
                    ans += H + Math.min(y + arr.get(i).get(1), 2*W - (y+arr.get(i).get(1)));
                } else if (arr.get(i).get(0) == 3) {
                    ans += y + H-arr.get(i).get(1);
                } else if (arr.get(i).get(0) == 4) {
                    ans += W-y + H-arr.get(i).get(1);
                }
            } else if (x == 3) {
                if (arr.get(i).get(0) == 3) {
                    ans += Math.abs(y - arr.get(i).get(1));
                } else if (arr.get(i).get(0) == 4) {
                    ans += W + Math.min(y + arr.get(i).get(1), 2*H - (y+arr.get(i).get(1)));
                } else if (arr.get(i).get(0) == 1) {
                    ans += y + arr.get(i).get(1);
                } else if (arr.get(i).get(0) == 2) {
                    ans += H-y + arr.get(i).get(1);
                }
            } else if (x == 4) {
                if (arr.get(i).get(0) == 4) {
                    ans += Math.abs(y - arr.get(i).get(1));
                } else if (arr.get(i).get(0) == 3) {
                    ans += W + Math.min(y + arr.get(i).get(1), 2*H - (y+arr.get(i).get(1)));
                } else if (arr.get(i).get(0) == 1) {
                    ans += y + W-arr.get(i).get(1);
                } else if (arr.get(i).get(0) == 2) {
                    ans += H-y + W-arr.get(i).get(1);
                }
            }
        }
        System.out.println(ans);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}