public class array_01_2차원배열선언 {
    public static void main(String[] args) {
        int[][] arr1;
        int[] arr2[];
        int arr3[][];

        int[][] arr4 = new int[3][4];
        int[][] arr5 = new int[][] {
                {1, 2, 3, 4},
                {5, 6, 7, 8},
                {9, 10, 11, 12}
        };

        int [][] arr6 = {
                {1, 2, 3, 4},
                {5, 6, 7},
                {8}
        };

        int[][] arr7 = new int[3][];

        arr7[0] = new int [] {1, 2, 3};
        arr7[1] = new int [] {4, 5, 6, 7};
        arr7[2] = new int [] {8, 9};

        System.out.println(arr7[0]);
    }
}
