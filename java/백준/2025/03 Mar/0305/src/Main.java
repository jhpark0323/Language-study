import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    static int[][] dp;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] str1 = br.readLine().toCharArray();
        char[] str2 = br.readLine().toCharArray();

        int len1 = str1.length;
        int len2 = str2.length;

        dp = new int [len1+1][len2+1];

        for (int i=1; i<=len1; i++) {
            for (int j=1; j<=len2; j++) {
                if (str1[i - 1] == str2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        func(str1, len1, len2);
        System.out.println(dp[len1][len2]);
        System.out.println(sb);


    }

    static void func(char[] str, int i, int j) {
        Stack<Character> stack = new Stack<>();
        while (i > 0 && j > 0) {
            if (dp[i][j] == dp[i-1][j]) {
                i--;
            } else if (dp[i][j] == dp[i][j - 1]) {
                j--;
            } else {
                stack.push(str[i-1]);
                i--;
                j--;
            }
        }
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
    }
}