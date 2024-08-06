import java.io.*;
import java.util.*;

public class Main {
	static int N, M, V;
	static boolean[][] graph;
	static boolean[] v_dfs;
	static boolean[] v_bfs;
	
	private void solution() throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		V = Integer.parseInt(st.nextToken());
		graph = new boolean[N+1][N+1];
		v_dfs = new boolean[N+1];
		v_bfs = new boolean[N+1];
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			graph[a][b] = true;
			graph[b][a] = true;
		}
		dfs(V);
		System.out.println();
		bfs();
	}

	private void dfs(int v1) {
		v_dfs[v1] = true;
		System.out.print(v1 + " ");
		for (int v2 = 1; v2 <= N; v2++) {
			if (graph[v1][v2] && !v_dfs[v2]) {
				dfs(v2);
			}
		}
	}
	
	private void bfs() {
		Queue<Integer> q = new LinkedList<>();
		q.offer(V);
		v_bfs[V] = true;
		System.out.print(V + " ");
		while (!(q.isEmpty())) {
			int v1 = q.poll();
			for (int v2 = 1; v2 <= N; v2++) {
				if (graph[v1][v2] && !v_bfs[v2]) {
					q.offer(v2);
					v_bfs[v2] = true;
					System.out.print(v2 + " ");
				}
			} 
		}
	}

	public static void main(String[] args) throws Exception {
		new Main().solution();
	}
}