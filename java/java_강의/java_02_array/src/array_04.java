import java.util.Arrays;

public class array_04 {
    public static void main(String[] args) {
        int[] nums = {13, 34, 642, 324, 1};

        int[] tmp = new int[nums.length*2];

        for (int i=0; i < nums.length; i++) {
            tmp[i] = nums[i];
        }
        System.out.println(Arrays.toString(tmp));

        int[] tmp2 = Arrays.copyOf(nums, 10);
        System.out.println(Arrays.toString(tmp2));

        int[] tmp3 = new int[10];
        System.arraycopy(nums, 0, tmp3, 0, nums.length);
        System.out.println(Arrays.toString(tmp3));
    }
}
