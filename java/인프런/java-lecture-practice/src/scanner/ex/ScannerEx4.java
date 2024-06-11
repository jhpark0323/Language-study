package scanner.ex;

import java.util.Scanner;

public class ScannerEx4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("구구단의 단 수를 입력해주세요 : ");
        int num = scanner.nextInt();

        System.out.printf("%d단의 구구단\n", num);

        for (int i=1; i <= 9; i++) {
            int ans = num * i;
            System.out.printf("%d x %d = %d\n", num, i, ans);
        }

    }
}
