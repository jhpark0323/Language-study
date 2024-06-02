import java.util.Scanner;

public class baekjoon_분산처리_1009 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int t = scanner.nextInt();

        for (int test_case=0; test_case < t; test_case++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();

            int start = 1;

            for (int i=0; i < b; i++) {
                start *= a;
                start %= 10;
            }
            if (start == 0) {
                System.out.println(10);
            } else {
            System.out.println(start);
            }
        }

        scanner.close();
    }
}
