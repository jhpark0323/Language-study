public class array_05 {
    public static void main(String[] args) {
        int[] nums = {13, 34, 642, 324, 1};

//        int max = nums[0];
//        int min = nums[0];

        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;

        for (int num :  nums) {
            if (max < num) {
                max = num;
            }
            if (min > num) {
                min = num;
            }
        }

        System.out.println("max: "+max);
        System.out.println("min: "+min);
    }
}
