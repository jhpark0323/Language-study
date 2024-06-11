package scanner;

import java.util.Scanner;

public class Scanner2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("입력: ");
        int num1 = scanner.nextInt();

        System.out.print("입력: ");
        int num2 = scanner.nextInt();
        
        int sum = num1 + num2;
        System.out.println("sum = " + sum);
    }
}
