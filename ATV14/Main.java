//Pedro Gabriel Ruiz - 13875571
// Gabriel Noronha - 13727151

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static final int MAX = 35;
    static final int STATES = 8;

    static boolean found;
    static boolean[][] visited = new boolean[MAX][STATES];
    static int id, N, first;
    static String state;

    public static boolean dfs(int n, int curr) {
        if (n == N - 1) {
            return ((curr >> 1) & 1) == ((first >> 2) & 1) && (curr & 1) == ((first >> 1) & 1);
        }

        visited[n][curr] = true;
        for (int i = 0; i < STATES; i++) {
            if (((id >> i) & 1) == (state.charAt(n + 1) - '0') &&
                ((curr >> 1) & 1) == ((i >> 2) & 1) &&
                (curr & 1) == ((i >> 1) & 1)) {
                if (n < N - 1 && !visited[n + 1][i] && dfs(n + 1, i)) {
                    return true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String line;

        while ((line = reader.readLine()) != null && !line.equals("exit")) {
            String[] parts = line.trim().split(" ");
            id = Integer.parseInt(parts[0]);
            N = Integer.parseInt(parts[1]);
            state = parts[2];

            found = false;

            // Try each possible initial state configuration
            for (int i = 0; i < STATES && !found; i++) {
                if (((id >> i) & 1) == (state.charAt(0) - '0')) {
                    first = i;
                    for (boolean[] row : visited) {
                        Arrays.fill(row, false);
                    }
                    found = dfs(0, i);
                }
            }

            System.out.println(found ? "REACHABLE" : "GARDEN OF EDEN");
        }
    }
}
