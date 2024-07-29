import java.io.*;
import java.util.*;

class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Integer[] arr = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).toArray(Integer[]::new);
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine());
        	int gender = Integer.parseInt(st.nextToken());
        	int X = Integer.parseInt(st.nextToken());
        	int temp1 = 2;
        	int temp2 = 1;
        	if (gender == 1) {
        		arr[X-1] = (arr[X-1] == 1 ? 0 : 1); 
        		while(X * temp1 <= N) {
        			arr[X * temp1 - 1] = (arr[X * temp1 - 1] == 1 ? 0 : 1);
        			temp1++;
        		}
        	} else {
        		arr[X-1] = (arr[X-1] == 1 ? 0 : 1); 
        		while (true) {
        			if (X-temp2-1 < 0 || X+temp2-1 >= N) {
        				break;
            		}
        			if (arr[X-temp2-1] != arr[X+temp2-1]) {
        				break;
        			}
        			arr[X-temp2-1] = (arr[X-temp2-1] == 1 ? 0 : 1);
        			arr[X+temp2-1] = arr[X-temp2-1];
        			temp2++;
        		}
        	}
        }
        for (int i = 0; i < N; i++) {
        	System.out.print(arr[i] + " ");
        	if ((i+1)%20 == 0) {
        		System.out.println();
        	}
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}