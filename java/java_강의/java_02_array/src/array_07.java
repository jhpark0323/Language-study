import java.util.Arrays;

public class array_07 {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 6, 3, 2, 4, 3, 2, 1, 3, 4, 5, 6, 7, 8, 9};

        int[] count = new int[10];

        for (int i=0; i <arr.length; i++) {
            count[arr[i]] += 1;
        }

        System.out.println(Arrays.toString(count));
    }
}
