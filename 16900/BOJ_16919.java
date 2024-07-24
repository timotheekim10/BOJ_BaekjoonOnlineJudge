import java.io.*;
import java.util.*;

class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        String[][] graphA = new String[R][C];
        String[][] graphB = new String[R][C];
        String[][] graphC = new String[R][C];
        String[][] graphD = new String[R][C];
        ArrayList<Integer> listX = new ArrayList<>();
        ArrayList<Integer> listY = new ArrayList<>();

        for (int i = 0; i < R; i++) {
            String[] arr = br.readLine().split("");
            for (int j = 0; j < C; j++) {
                graphA[i][j] = arr[j];
                if (graphA[i][j].equals("O")) {
                    listX.add(i);
                    listY.add(j);
                }
            }
        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                graphB[i][j] = "O";
            }
        }
        
        for (int i = 0; i < R; i++) {
            graphC[i] = graphB[i].clone();
            graphD[i] = graphB[i].clone();
        }

        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};

        for (int i = 0; i < listX.size(); i++) {
            int x = listX.get(i);
            int y = listY.get(i);
            graphC[x][y] = ".";
            for (int j = 0; j < 4; j++) {
                int nx = x + dx[j];
                int ny = y + dy[j];
                if (0 <= nx && nx < R && 0 <= ny && ny < C) {
                    graphC[nx][ny] = ".";
                }
            }
        }

        listX.clear();
        listY.clear();

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (graphC[i][j].equals("O")) {
                    listX.add(i);
                    listY.add(j);
                }
            }
        }

        for (int i = 0; i < listX.size(); i++) {
            int x = listX.get(i);
            int y = listY.get(i);
            graphD[x][y] = ".";
            for (int j = 0; j < 4; j++) {
                int nx = x + dx[j];
                int ny = y + dy[j];
                if (0 <= nx && nx < R && 0 <= ny && ny < C) {
                    graphD[nx][ny] = ".";
                }
            }
        }

        if (N == 1) {
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    System.out.print(graphA[i][j]);
                }
                System.out.println();
            }
        } else if (N%2 == 0) {
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    System.out.print(graphB[i][j]);
                }
                System.out.println();
            }
        } else if (N%4 == 3) {
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    System.out.print(graphC[i][j]);
                }
                System.out.println();
            }
        } else if (N > 1 && N%4 == 1) {
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    System.out.print(graphD[i][j]);
                }
                System.out.println();
            }
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}