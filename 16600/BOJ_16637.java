import java.io.*;
import java.util.*;

public class Main {
	static int ans = Integer.MIN_VALUE;
	static List<Integer> num = new ArrayList<>();
	static List<String> op = new ArrayList<>();
	
	private void solution() throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		String[] arr = br.readLine().split("");
		for(int i = 0; i < arr.length; i++) {
			if (i%2 == 0) {
				Integer integerNum = Integer.valueOf(arr[i]);
				num.add(integerNum);
			} else {
				op.add(arr[i]);
			}
		}
		dfs(0, num.get(0));
		System.out.println(ans);
	}
	
	private void dfs(int idx, int result) {
		if (idx == op.size()) {
			ans = Math.max(ans, result);
			return;
		}
		dfs(idx+1, calc(op.get(idx), result, num.get(idx+1)));
		if (idx < op.size() - 1) {
			int temp = calc(op.get(idx+1), num.get(idx+1), num.get(idx+2));
			dfs(idx+2, calc(op.get(idx), result, temp));
		}
	}
	
	private int calc(String op, int a, int b) {
		switch (op) {
		case "+": return a + b;
		case "-": return a - b;
		default: return a * b;
		}
	}
	
	public static void main(String[] args) throws Exception {
		new Main().solution();
	}
}