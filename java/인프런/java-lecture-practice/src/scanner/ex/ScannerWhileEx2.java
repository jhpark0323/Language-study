package scanner.ex;

import java.util.Scanner;

public class ScannerWhileEx2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int sum = 0;
        int count = 0;

//        while (true) {
//            int num = scanner.nextInt();
//            if (num == -1) {
//                break;
//            }
//            sum += num;
//            count++;
//        }

        int num = 0;
        while ((num = scanner.nextInt()) != -1) {
            sum += num;
            count++;
        }


        System.out.println("입력한 숫자들의 합계 : " + sum);

        double average = (double) sum / count;

        System.out.println("입력한 숫자들의 평균 : " + average);
    }
}
