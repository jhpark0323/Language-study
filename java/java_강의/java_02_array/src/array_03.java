import java.util.Arrays;

public class array_03 {
    public static void main(String[] args) {
        int[] nums = {13, 34, 642, 324, 1};

        for (int i=0; i < nums.length; i++) {
            System.out.println(nums[i]);
        }

        for (int num : nums) {
            System.out.println(num);
        }

        System.out.println(Arrays.toString(nums));
    }
}
