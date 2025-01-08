import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_20125 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        char[][] arr = new char[n][n];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < n; j++) {
                arr[i][j] = line.charAt(j);
            }
        }
        int row=1, col=1;

        a: for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (arr[i][j] == '*') {
                    row = i + 2;   // 행 3
                    col = j + 1;   // 열 8
                    break a;
                }
            }
        }

        // 왼팔
        int left = 0;
        for (int i = 0; i < col -1; i++) {
            if (arr[row - 1][i] == '*') {
                left++;
            }
        }

        // 오른팔
        int right = 0;
        for (int i = col; i < n; i++) {
            if (arr[row - 1][i] == '*') {
                right++;
            }
        }

        // 허리
        int waist = 0;
        for (int i = row; i < n; i++) {
            if (arr[i][col-1] == '*') {
                waist++;
            }
        }

        // 왼다리
        int lLeg = 0;
        for (int i = row-1+waist; i < n; i++) {
            if (arr[i][col - 2] == '*') {
                lLeg++;
            }
        }

        // 오른다리
        int rLeg = 0;
        for (int i = row-1+waist; i < n; i++) {
            if (arr[i][col] == '*') {
                rLeg++;
            }
        }

        System.out.println(row + " " + col);
        System.out.println(left + " " + right + " " + waist + " " + lLeg + " " + rLeg);

    }
}
