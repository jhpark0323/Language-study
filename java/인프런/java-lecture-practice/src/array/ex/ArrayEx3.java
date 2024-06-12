package array.ex;

import java.util.Scanner;

public class ArrayEx3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] arr = new int[5];

        for (int i=0; i < arr.length; i++) {
            arr[i] = scanner.nextInt();
        }

        for (int i =  arr.length-1; i > -1; i--) {
            System.out.print(arr[i]);
            if (i == 0) {
                break;
            }
            System.out.print(", ");
        }

    }
}
