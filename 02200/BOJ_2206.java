import java.io.*;
import java.util.*;

class Point {
	int x, y, d, c;

	public Point(int x, int y, int d, int c) {
		this.x = x;
		this.y = y;
		this.d = d;
		this.c = c;
	}
}

public class Main {
	static String[][] graph;
	static boolean[][][] v;
	static int N, M;
	static int[] dx = { 1, -1, 0, 0 };
	static int[] dy = { 0, 0, 1, -1 };

	private void solution() throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		graph = new String[N][M];
		v = new boolean[N][M][2];
		for (int i = 0; i < N; i++) {
			String[] arr = br.readLine().split("");
			for (int j = 0; j < M; j++) {
				graph[i][j] = arr[j];
			}
		}
		bfs();
		System.out.println(-1);
	}

	private void bfs() {
		Queue<Point> q = new ArrayDeque<>();
		q.offer(new Point(0, 0, 1, 0));
		v[0][0][0] = true;
		while (!(q.isEmpty())) {
			Point current = q.poll();
			int x = current.x;
			int y = current.y;
			int d = current.d;
			int c = current.c;
			if (x == N - 1 && y == M - 1) {
				System.out.println(d);
				System.exit(0);
				;
			}
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (0 <= nx && nx < N && 0 <= ny && ny < M) {
					if (graph[nx][ny].equals("1") && c < 1 && !v[nx][ny][c + 1]) {
						q.offer(new Point(nx, ny, d + 1, c + 1));
						v[nx][ny][c + 1] = true;
					} else if (graph[nx][ny].equals("0") && !v[nx][ny][c]) {
						q.offer(new Point(nx, ny, d + 1, c));
						v[nx][ny][c] = true;
					}
				}
			}
		}
	}

	public static void main(String[] args) throws Exception {
		new Main().solution();
	}
}