import java.util.Scanner;

public class 카드게임_5522 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int sum = 0;

        for (int i = 0; i < 5; i++) {
            int score = scanner.nextInt();
            sum += score;
        }
        System.out.println(sum);

        scanner.close();
    }
}
