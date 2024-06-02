public class array_04_2차원배열탐색 {
    public static void main(String[] args) {
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        int [][] arr = {
                {0, 0, 0, 0, 0},
                {0, 1, 0, 0, 0},
                {0, 0, 0, 0, 0},
                {0, 0, 0, 1, 0},
                {0, 0, 0, 0, 0},
        };

        int n = 5;

        for (int r=0; r<n; r++) {
            for (int c=0; c<n; c++) {
                if (arr[r][c] == 1) {
                    System.out.println("r: "+ r+ ", c: "+ c);

                    for (int d=0; d<4; d++) {
                        int nr = r + dr[d];
                        int nc = c + dc[d];
                        if (0 <= nr && nr < n && 0 <= nc && nc < n)
                        arr[nr][nr] = 2;
                    }

                }
            }
        }

        for (int r=0; r<n; r++) {
            for (int c=0; c<n; c++) {
                System.out.printf("%2d", arr[r][c]);
            }
            System.out.println();
        }

    }
}
