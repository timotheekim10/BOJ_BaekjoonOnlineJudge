import java.io.*;
import java.util.*;

public class Main {
	static int w, h;
	static int[][] graph;
	static boolean[][] visited;
	static int[] dx = {1, -1, 0, 0, 1, 1, -1, -1};
	static int[] dy = {0, 0, 1, -1, 1, -1, 1, -1};
	
	private void solution() throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while (true) {
			StringTokenizer st;
			st = new StringTokenizer(br.readLine());
			w = Integer.parseInt(st.nextToken());
			h = Integer.parseInt(st.nextToken());
			if (w==0 && h==0) {
				return;
			}
			graph = new int[h][w];
			visited = new boolean[h][w];
			for(int i = 0; i < h; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j = 0; j < w; j++) {
					graph[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			int ans = 0;
			for(int i = 0; i < h; i++) {
				for(int j = 0; j < w; j++) {
					if (graph[i][j]==1 && !visited[i][j]) {
						dfs(i, j);
						ans++;
					}
				}
			}
			System.out.println(ans);
		}
	}
	
	private void dfs(int x, int y) {
		visited[x][y] = true;
		for(int d = 0; d < 8; d++) {
			int nx = x + dx[d];
			int ny = y + dy[d];
			if(0<=nx && nx<h && 0<=ny && ny<w && graph[nx][ny]==1 && !visited[nx][ny]) {
				visited[nx][ny] = true;
				dfs(nx, ny);
			}
		}
	}
	
	public static void main(String[] args) throws Exception {
		new Main().solution();
	}
}