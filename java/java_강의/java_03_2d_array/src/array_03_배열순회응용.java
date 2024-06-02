public class array_03_배열순회응용 {
    public static void main(String[] args) {
        // 1 2 3 4
        //   5 6 7
        //     8 9
        //       10

        int[][] arr = new int [4][4];
        int cnt = 0;

        for (int r=0; r < arr.length; r++) {
            for (int c=r; c < arr[r].length; c++) {
                arr[r][c] = ++cnt;
                System.out.printf("%3d", arr[r][c]);
            }
            System.out.println();
        }

        System.out.println("-----------------------------");

        for (int r=0; r < arr.length; r++) {
            for (int c=0; c < arr[r].length; c++) {
                if (arr[r][c] == 0) {
                    System.out.print("   ");
                } else {
                    System.out.printf("%3d", arr[r][c]);
                }
            }
            System.out.println();
        }

    }
}
