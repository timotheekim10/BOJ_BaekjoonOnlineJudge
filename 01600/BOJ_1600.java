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
	static int[][] graph;
	static boolean[][][] v;
	static int H, W, K;
	static int[] dx1 = { 1, -1, 0, 0 };
	static int[] dy1 = { 0, 0, 1, -1 };
	static int[] dx2 = { 2, 2, 1, 1, -1, -1, -2, -2 };
	static int[] dy2 = { 1, -1, 2, -2, 2, -2, 1, -1 };

	private void solution() throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		K = Integer.parseInt(br.readLine());
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		W = Integer.parseInt(st.nextToken());
		H = Integer.parseInt(st.nextToken());
		graph = new int[H][W];
		v = new boolean[H][W][K + 1];
		for (int i = 0; i < H; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < W; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		bfs();
		System.out.println(-1);
	}

	private void bfs() {
		Queue<Point> q = new ArrayDeque<>();
		q.offer(new Point(0, 0, 0, 0));
		v[0][0][0] = true;
		while (!(q.isEmpty())) {
			Point current = q.poll();
			int x = current.x;
			int y = current.y;
			int d = current.d;
			int c = current.c;
			
			if (x == H - 1 && y == W - 1) {
				System.out.println(d);
				System.exit(0);
			}
			
			for (int i = 0; i < 4; i++) {
				int nx1 = x + dx1[i];
				int ny1 = y + dy1[i];
				if (0 <= nx1 && nx1 < H && 0 <= ny1 && ny1 < W && !v[nx1][ny1][c] && graph[nx1][ny1] == 0) {
					q.offer(new Point(nx1, ny1, d + 1, c));
					v[nx1][ny1][c] = true;
				}
			}
			
			if (c < K) {
				for (int i = 0; i < 8; i++) {
					int nx2 = x + dx2[i];
					int ny2 = y + dy2[i];
					if (0 <= nx2 && nx2 < H && 0 <= ny2 && ny2 < W && !v[nx2][ny2][c + 1] && graph[nx2][ny2] == 0) {
						q.offer(new Point(nx2, ny2, d + 1, c + 1));
						v[nx2][ny2][c + 1] = true;
					}
				}
			}
		}
	}

	public static void main(String[] args) throws Exception {
		new Main().solution();
	}
}