package scanner;

import java.util.Scanner;

public class ScannerWhile2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("입력: ");
            int num1 = scanner.nextInt();

            System.out.print("입력: ");
            int num2 = scanner.nextInt();

            if (num1 == 0 && num2 == 0) {
                break;
            }
            int sum = num1 + num2;
            System.out.println("sum = " + sum);
        }

    }
}
