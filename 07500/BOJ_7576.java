import java.io.*;
import java.util.*;

class Point {
	int x, y;

	public Point(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

class Main {
	static int M, N;
	static int[][] graph;
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	static Queue<Point> q = new ArrayDeque<>();
	
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        graph = new int[N][M];
        boolean tmp = true;
        for (int i = 0; i < N; i++) {
        	st = new StringTokenizer(br.readLine());
        	for (int j = 0; j < M; j++) {
        		graph[i][j] = Integer.parseInt(st.nextToken());
        		if (graph[i][j] == 1) {
        			q.offer(new Point(i, j));
        		}
        		if (graph[i][j] == 0) {
        			tmp = false;
        		}
        	}
        }
        if (tmp) {
        	System.out.println(0);
        	return;
        }
        bfs();
        int ans = 0;
        for (int i = 0; i < N; i++) {
        	for (int j = 0; j < M; j++) {
        		if (graph[i][j] == 0) {
        			System.out.println(-1);
        			return;
        		}
        		if (graph[i][j] >= 1) {
        			ans = Math.max(ans, graph[i][j]-1);
        		}
        	}
        }
        System.out.println(ans);
    }
    
    private static void bfs() {
    	while (!q.isEmpty()) {
    		Point p = q.poll();
    		for (int i = 0; i < 4; i++) {
    			int nx = p.x + dx[i];
    			int ny = p.y + dy[i];
    			if (0<=nx && nx<N && 0<=ny && ny<M && graph[nx][ny]==0) {
    				graph[nx][ny] = graph[p.x][p.y] + 1;
    				q.offer(new Point(nx, ny));
    			}
    		}
    	}
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}