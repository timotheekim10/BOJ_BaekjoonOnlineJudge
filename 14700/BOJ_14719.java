import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

class Main {
    static int h;
    static int w;
    static int[][] arr;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Scanner scan = new Scanner(System.in);
        StringTokenizer st = new StringTokenizer(br.readLine());

        h = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());

        List<Integer> list = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).collect(Collectors.toList());

        arr = new int[w][2];

        for (int i = 0; i < w; i++) {
            arr[i] = new int[]{i, list.get(i)};
        }

        int maxIdx = 0;
        int maxHeight = 0;

        for (int i = 0; i < w; i++) {
            if (arr[i][1] > maxHeight) {
                maxHeight = arr[i][1];
                maxIdx = i;
            }
        }

        int ans = 0;

        int height = arr[0][1];

        for (int i = 0; i < maxIdx; i++) {
            if (height < arr[i+1][1]) {
                height = arr[i+1][1];
            }
            else {
                ans += (height - arr[i+1][1]);
            }
        }

        height = arr[w-1][1];

        for (int i = w-1; i > maxIdx; i--) {
            if (height < arr[i-1][1]) {
                height = arr[i-1][1];
            }
            else {
                ans += (height - arr[i-1][1]);
            }
        }

        System.out.println(ans);
    }
}
