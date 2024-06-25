import java.io.*;
import java.util.*;

class Main {
    static int n, k, left, right, min, length;
    static ArrayList<Integer> list;

    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (st.nextToken().equals("1")) {
                list.add(i);
            }
        }
        if (list.size() < k) {
            System.out.println(-1);
            return;
        }
        
        left = 0;
        right = k - 1;
        min = Integer.MAX_VALUE;
        length = 0;
        while (right < list.size()) {
            length = list.get(right) - list.get(left) + 1;
            min = Math.min(min, length);
            left++;
            right++;
        }
        System.out.println(min);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}