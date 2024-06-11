package scanner.ex;

import java.util.Scanner;

public class ScannerWhileEx4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int sum = 0;
        while (true) {
            System.out.println("1: 상품 입력, 2: 결제, 3: 프로그램 종료");

            int option = scanner.nextInt();
            scanner.nextLine();

            if (option == 1) {
                System.out.print("상품명을 입력하세요: ");
                String name = scanner.nextLine();
                System.out.print("상품의 가격을 입력하세요: ");
                int price = scanner.nextInt();
                System.out.print("구매수량을 입력하세요: ");
                int quantity = scanner.nextInt();
                int total = price * quantity;
                sum += total;

                System.out.printf("상품명 : %s, 가격 : %d, 수량 : %d, 합계 : %d\n", name, price, quantity, total);
            }

            else if (option == 2) {
                System.out.println("총 비용: " + sum);
                sum = 0;
            }

            else if (option == 3) {
                System.out.println("프로그램을 종료합니다.");
                break;
            }

            else {
                System.out.println("올바른 값을 입력하세요.");
            }

        }


    }
}
