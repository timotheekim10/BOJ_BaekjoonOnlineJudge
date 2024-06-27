import java.io.*;
import java.util.*;

class Main {
    static int n, m, answer;
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    static boolean[] visited;

    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        StringTokenizer st;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        visited = new boolean[n + 1];
        visited[1] = true;
        answer = 0;

        dfs(1, 0);

        for (int i = 2; i < visited.length; i++) {
            if (visited[i]) {
                answer++;
            }
        }
        System.out.println(answer);
    }

    private void dfs(int x, int depth) {
        if (depth == 2) {
            return;
        }
        for (int i = 0; i < graph.get(x).size(); i++) {
            int nx = graph.get(x).get(i);
            visited[nx] = true;
            dfs(nx, depth + 1);
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}