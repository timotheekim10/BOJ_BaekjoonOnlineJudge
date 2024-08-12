import java.io.*;
import java.util.*;

public class Main {
	static int N;
	static int[] population;
	static ArrayList[] graph;
	static ArrayList<Integer> a;
	static ArrayList<Integer> b;
	static int ans = Integer.MAX_VALUE;
	
	private void solution() throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		population = new int[N];
		graph = new ArrayList[N+1];
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			population[i] = Integer.parseInt(st.nextToken());
		}
		for (int i = 1; i <= N; i++) {
			graph[i] = new ArrayList<Integer>();
			st = new StringTokenizer(br.readLine());
			int cnt = Integer.parseInt(st.nextToken());
			for (int j = 0; j < cnt; j++) {
				int area = Integer.parseInt(st.nextToken());
				graph[i].add(area);
			}
		}
		powerSet(new boolean[N], 0);
		if (ans != Integer.MAX_VALUE) {
			System.out.println(ans);
		} else {
			System.out.println(-1);
		}
	}
	
	private void powerSet(boolean[] visited, int idx) {
	    if(idx == N) {
	    	a = new ArrayList<>();
	    	b = new ArrayList<>();
	        for (int i = 0; i < N; i++) {
	        	if (visited[i]) {
	        		a.add(i+1);
	        	} else {
	        		b.add(i+1);
	        	}
	        }
	        if (a.size() != 0 && b.size() != 0) {
	        	bfs(a, b);
	        }
	        return;
	    }
	    visited[idx] = false;
	    powerSet(visited, idx + 1);
	    visited[idx] = true;
	    powerSet(visited, idx + 1);
	}
	
	private void bfs(ArrayList<Integer> aList, ArrayList<Integer> bList) {
		int aCnt = 1;
		int bCnt = 1;
		Queue<Integer> q = new ArrayDeque<>();
		boolean[] v = new boolean[N+1];
		q.offer(a.get(0));
		v[a.get(0)] = true;
		while (!(q.isEmpty())) {
			int x = q.poll();
			for (int i = 0; i < graph[x].size(); i++) {
				if (!v[(int) graph[x].get(i)] && aList.contains((int) graph[x].get(i))) {
					q.offer((Integer) graph[x].get(i));
					v[(int) graph[x].get(i)] = true;
					aCnt++;
				}
			}
		}
		q = new ArrayDeque<>();
		v = new boolean[N+1];
		q.offer(b.get(0));
		v[b.get(0)] = true;
		while (!(q.isEmpty())) {
			int x = q.poll();
			for (int i = 0; i < graph[x].size(); i++) {
				if (!v[(int) graph[x].get(i)] && bList.contains((int) graph[x].get(i))) {
					q.offer((Integer) graph[x].get(i));
					v[(int) graph[x].get(i)] = true;
					bCnt++;
				}
			}
		}
		if (aList.size() == aCnt && bList.size() == bCnt) {
			int aSum = 0;
			for (int i = 0; i < aList.size(); i++) {
				aSum += population[(int) aList.get(i) - 1];
			}
			int bSum = 0;
			for (int i = 0; i < bList.size(); i++) {
				bSum += population[(int) bList.get(i) - 1];
			}
			ans = Math.min(ans, Math.abs(aSum - bSum));
		}
	}

	public static void main(String[] args) throws Exception {
		new Main().solution();
	}
}