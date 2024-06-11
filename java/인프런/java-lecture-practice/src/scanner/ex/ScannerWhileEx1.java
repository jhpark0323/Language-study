package scanner.ex;

import java.util.Scanner;

public class ScannerWhileEx1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            String name = scanner.nextLine();
            if (name.equals("종료")) {
                System.out.println("종료");
                break;
            }
            int age = scanner.nextInt();
            // 입력은 name과 age만 받지만 age를 받을 때 10 누르고 enter치면
            // 10\n이라고 받게 됨
            // 이 때 nextInt는 10만 가져가게 되고
            // \n가 남아서 다음 while문의 name으로 가져가게 됨
            // 그걸 방지하기 위해 nextLine을 하나 더 해줌
            scanner.nextLine();
            System.out.printf("입력한 이름: %s, 나이: %d\n", name, age);
        }
    }
}
