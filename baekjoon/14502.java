import java.util.*;

public class Main {

    private int n;
    private int m;
    private int result;
    private List<List<Integer>> virusList = new ArrayList<>();
    private int[] dy = {1, 0, -1, 0};
    private int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) {
        Main app = new Main();
        app.run();
    }

    private int[][] clone(int[][] array) {
        int[][] newArray = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                newArray[i][j] = array[i][j];
            }
        }
        return newArray;
    }

    private int bfs(int[][] board) {
        for (List<Integer> virusIndex : virusList) {
            int y = virusIndex.get(0);
            int x = virusIndex.get(1);

            ArrayDeque<List<Integer>> deque = new ArrayDeque<>();
            deque.addLast(Arrays.asList(y, x));
            while (!deque.isEmpty()) {
                List<Integer> now = deque.pollFirst();

                for (int i = 0; i < 4; i++) {
                    int nextY = dy[i] + now.get(0);
                    int nextX = dx[i] + now.get(1);

                    if (nextY >= 0 && nextX >= 0 && nextY < n && nextX < m && board[nextY][nextX] == 0) {
                        board[nextY][nextX] = 2;
                        deque.addLast(Arrays.asList(nextY, nextX));
                    }
                }
            }
        }

        return count(board);
    }

    private int count(int[][] board) {
        int count = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 0) {
                    count++;
                }
            }
        }
        return count;
    }

    private void dfs(int level, int[][] now) {
        if (level >= 3) {
            result = Math.max(result, bfs(clone(now)));
            return;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (now[i][j] == 0) {
                    now[i][j] = 1;
                    dfs(level + 1, now);
                    now[i][j] = 0;
                }
            }
        }
    }

    private void run() {
        Scanner scan = new Scanner(System.in);
        String[] nm = scan.nextLine().trim().split(" ");
        n = Integer.parseInt(nm[0]);
        m = Integer.parseInt(nm[1]);
        int[][] board = new int[n][m];

        for (int i = 0; i < n; i++) {
            String[] line = scan.nextLine().trim().split(" ");
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(line[j]);
                if (board[i][j] == 2) {
                    virusList.add(Arrays.asList(i, j));
                }
            }
        }

        dfs(0, board);
        System.out.println(result);
    }
}
