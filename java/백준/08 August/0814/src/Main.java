import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        long[][] arr = new long[2][n+1];
        arr[0][1] = 1;
        if (n >= 2) {
            arr[0][2] = 1;
        }

        for (int i = 3; i <= n; i++) {
            // 전단계에서 마지막이 0으로 끝나는거 + 마지막이 1로 끝나는거
            arr[0][i] = arr[0][i-1] + arr[1][i-1];
            // 전단계에서 마지막이 0으로 끝나는거
            arr[1][i] = arr[0][i-1];
        }

        System.out.println(arr[0][n] + arr[1][n]);

    }
}