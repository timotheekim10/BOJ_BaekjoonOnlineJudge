import java.io.*;
import java.util.*;

class Main {
    public static int nx, ny, px, py;

    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ArrayList<String> visit = new ArrayList<>();
        String start = br.readLine();

        int sx = start.charAt(0);
        int sy = start.charAt(1);
        px = sx;
        py = sy;

        visit.add(start);

        for (int i = 0; i < 35; i++) {
            String now = br.readLine();
            nx = now.charAt(0);
            ny = now.charAt(1);

            if (visit.contains(now)) {
                System.out.println("Invalid");
                return;
            }

            if (Math.abs(nx - px) == 2 && Math.abs(ny - py) == 1 || Math.abs(nx - px) == 1 && Math.abs(ny - py) == 2) {

            } else {
                System.out.println("Invalid");
                return;
            }

            visit.add(now);
            px = nx;
            py = ny;
        }

        if (Math.abs(nx - sx) == 2 && Math.abs(ny - sy) == 1 || Math.abs(nx - sx) == 1 && Math.abs(ny - sy) == 2) {

        } else {
            System.out.println("Invalid");
            return;
        }

        System.out.println("Valid");
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}