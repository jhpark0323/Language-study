import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        long[][] arr = new long[101][10];

        for (int i = 1; i < 10; i++) {
            arr[1][i] = 1;
        }

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < 10; j++) {
                if (j == 0) {
                    arr[i+1][1] += arr[i][0] % 1000000000;
                } else if (j == 9) {
                    arr[i + 1][8] += arr[i][9] % 1000000000;
                } else {
                    arr[i+1][j-1] += arr[i][j] % 1000000000;
                    arr[i+1][j+1] += arr[i][j] % 1000000000;
                }
            }
        }

        long ans = 0;
        for (int i = 0; i < 10; i++) {
            ans += arr[n][i];
        }
        System.out.println(ans % 1000000000);

    }
}