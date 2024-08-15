package test;

import java.io.*;
import java.util.*;

class Enemy {
	int x, y;
	boolean dead;
	
	public Enemy(int x, int y, boolean dead) {
		this.x = x;
		this.y = y;
		this.dead = dead;
	}
	
	@Override
    protected Enemy clone() {
        return new Enemy(this.x, this.y, this.dead);
    }
}

public class Main {
	static int N; // 행
	static int M; // 열
	static int D; // 궁수의 공격 거리 제한
	static int[] arr; // 모든 열 배열
	static ArrayList<Enemy> enemies; // 모든 적의 위치 배열에 저장
	static ArrayList<Integer> sel;
	static int ans = 0;
	
	private void solution() throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		D = Integer.parseInt(st.nextToken());
		enemies = new ArrayList<Enemy>();
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				int x = Integer.parseInt(st.nextToken());
				if (x == 1) {
					enemies.add(new Enemy(i, j, false));
				}
			}
		}
		Collections.sort(enemies,(o1, o2) -> Integer.compare(o2.x, o1.x)); // 행 좌표에 대해서 내림차순 정렬
		arr = new int[M];
		for (int i = 0; i < M; i++) {
			arr[i] = i;
		}
		sel = new ArrayList<Integer>();
		combination(0);
		System.out.println(ans);
	}
	
	private void combination(int idx) { // 궁수의 위치 M개 중 3개를 선택하는 조합
		if (sel.size() == 3) {
			gameStart(sel);
			return;
		}
		
		for (int i = idx; i < M; i++) {
			sel.add(arr[i]);
			combination(i + 1);
			sel.remove(sel.size()-1);
		}
	}
	
	private void gameStart(ArrayList<Integer> sel) {
		int cnt = 0;
		ArrayList<Enemy> enemiesClone = new ArrayList<Enemy>();
	    for (Enemy enemy : enemies) { // 객체 리스트 깊은 복사
	        enemiesClone.add(enemy.clone());
	    }
		ArrayList<int[]> archerList = new ArrayList<int[]>();
		for (int i = 0; i < 3; i++) { // 조합을 궁수의 행, 열 좌표로 변환해서 리스트에 저장
			archerList.add(new int[] {N, sel.get(i)});
		}
		for (int i = 0; i < N; i++) {
			ArrayList<Enemy> deadList = new ArrayList<Enemy>();
			for (int j = 0; j < 3; j++) {
				int minD = Integer.MAX_VALUE;
				ArrayList<Enemy> targetList = new ArrayList<Enemy>(); // 가장 가까운 적 리스트
				for (int k = 0; k < enemiesClone.size(); k++) {
					if (enemiesClone.get(k).x >= N) { // 적이 성안으로 들어오면
						continue;
					}
					if (enemiesClone.get(k).dead) { // 적이 죽었으면
						continue;
					}
					// d : 궁수와 적의 맨하탄 거리
					int d = Math.abs(archerList.get(j)[0] - enemiesClone.get(k).x) + Math.abs(archerList.get(j)[1] - enemiesClone.get(k).y);
					if (d <= D) {
						if (d < minD) { // 더 가까운 적이 있다면
							minD = d;
							targetList.clear();
							targetList.add(enemiesClone.get(k));
						} else if (d == minD) { // 가장 가까운 적이 또 있다면
							targetList.add(enemiesClone.get(k));
						}
					}
				}
				if (minD != Integer.MAX_VALUE) {
					Collections.sort(targetList, (o1, o2) -> Integer.compare(o1.y, o2.y)); // 가장 왼쪽에 있는 적을 찾음
					deadList.add(targetList.get(0));
				}
			}
			for (int j = 0; j < deadList.size(); j++) {
				deadList.get(j).dead = true;
			}
			for (int j = 0; j < enemiesClone.size(); j++) {
				enemiesClone.get(j).x++;
			}
		}
		for (Enemy enemy: enemiesClone) {
			if (enemy.dead) {
				cnt++;
			}
		}
		ans = Math.max(ans, cnt);
	}
	
	public static void main(String[] args) throws Exception {
		new Main().solution();
	}
}