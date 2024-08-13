import java.io.*;
import java.util.*;

class Point1 {
	int x, y;

	public Point1(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

class Point2 {
	int x, y, d;

	public Point2(int x, int y, int d) {
		this.x = x;
		this.y = y;
		this.d = d;
	}
}

public class Main {
	static int N;
	static int[][] graph;
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	static int ans = Integer.MAX_VALUE;
	private void solution() throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		graph = new int[N][N];
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int no = 2;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (graph[i][j] == 1) {
					bfs1(i, j, no);
					no++;
				}
			}
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (graph[i][j] != 0) {
					bfs2(i, j, graph[i][j]);
				}
			}
		}
		System.out.println(ans);
	}
	
	private void bfs1(int i, int j, int no) {
		Queue<Point1> q = new ArrayDeque<>();
		q.offer(new Point1(i, j));
		graph[i][j] = no;
		while (!q.isEmpty()) {
			Point1 node = q.poll();
			int x = node.x;
			int y = node.y;
			for (int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if (0<=nx && nx<N && 0<=ny && ny<N && graph[nx][ny]==1) {
					graph[nx][ny] = no;
					q.offer(new Point1(nx, ny));
				}
			}
		}
	}

	private void bfs2(int i, int j, int no) {
		boolean[][] v = new boolean[N][N];
		Queue<Point2> q = new ArrayDeque<>();
		q.offer(new Point2(i, j, 0));
		v[i][j] = true;
		while (!q.isEmpty()) {
			Point2 node = q.poll();
			int x = node.x;
			int y = node.y;
			int d = node.d;
			if (graph[x][y] != 0) {
				if (graph[x][y] != no) {
					ans = Math.min(ans, d-1);
					return;
				}
			}
			for (int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if (0<=nx && nx<N && 0<=ny && ny<N && graph[nx][ny]!=no && !v[nx][ny]) {
					v[nx][ny] = true;
					q.offer(new Point2(nx, ny, d+1));
				}
			}
		}
	}	

	public static void main(String[] args) throws Exception {
		new Main().solution();
	}
}