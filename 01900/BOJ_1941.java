import java.io.*;
import java.util.*;

public class Main {
	static String[][] graph = new String[5][5];
	static List<Integer> sel = new ArrayList<>();
	static int ans = 0;
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	
	private void solution() throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for(int i=0;i<5;i++) {
			String[] arr = br.readLine().split("");
			for(int j=0;j<5;j++) {
				graph[i][j] = arr[j];
			}
		}
		combi(0);
		System.out.println(ans);
	}
	
	private void combi(int idx) {
		if(sel.size() == 7) {
			if (isSevenPrincess()) {
				ans++;
			}
			return;
		}
		for(int i=idx;i<25;i++) {
			sel.add(i);
			combi(i+1);
			sel.remove(sel.size()-1);
		}
	}
	
	private boolean isSevenPrincess() {
		int sCnt = 0;
		for(int i=0;i<7;i++) {
			int idx = sel.get(i);
			int x = idx/5;
			int y = idx%5;
			if(graph[x][y].equals("S")) {
				sCnt++;
			}
		}
		if(!(sCnt>=4)) {
			return false;
		}
		
		Queue<Integer> q = new LinkedList<>();
		boolean[][] v = new boolean[5][5];
		int cnt = 0;
		int start = sel.get(0);
		q.offer(start);
		int sx = start/5;
		int sy = start%5;
		v[sx][sy] = true;
		cnt++;
		while (!(q.isEmpty())) {
			int current = q.poll();
			int cx = current/5;
			int cy = current%5;
			for(int i=0;i<4;i++) {
				int nx = cx + dx[i];
				int ny = cy + dy[i];
				if(0<=nx && nx<5 && 0<=ny && ny<5 && !v[nx][ny]) {
					if(sel.contains(nx*5+ny)) {
						q.offer(nx*5+ny);
						v[nx][ny] = true;
						cnt++;
					}
				}
			}
		}
		return cnt==7;
	}

	public static void main(String[] args) throws Exception {
		new Main().solution();
	}
}
