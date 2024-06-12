package array.ex;

import java.util.Scanner;

public class ArrayEx6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("입력받을 숫자의 개수를 입력하세요 : ");
        int n = scanner.nextInt();
//        scanner.nextLine();

        System.out.println(n + "개의 정수를 입력하세요 : ");

        int[] arr = new int[n];

        int min = Integer.MAX_VALUE;
        int max = 0;

        for (int i=0; i < arr.length; i++) {
            arr[i] = scanner.nextInt();
            if (arr[i] < min) {
                min = arr[i];
            }
            if (max < arr[i]) {
                max = arr[i];
            }
        }

        System.out.println("가장 작은 정수 : " + min);
        System.out.println("가장 큰 정수 : " + max);




    }
}
