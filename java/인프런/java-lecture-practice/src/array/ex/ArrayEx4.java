package array.ex;

import java.util.Scanner;

public class ArrayEx4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] arr = new int[5];

        int sum = 0;
        for (int i=0; i<arr.length; i++) {
            arr[i] = scanner.nextInt();
            sum += arr[i];
        }

        System.out.println("입력한 정수의 합계: " + sum);
        System.out.println("입력한 정수의 평균: " + (double) sum / arr.length);

    }
}

/*
1
2
3
4
5
 */
