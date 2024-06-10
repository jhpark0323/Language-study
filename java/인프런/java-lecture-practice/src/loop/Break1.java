package loop;

public class Break1 {
    public static void main(String[] args) {
        int sum = 0;
        int i = 1;

        while (true) {
            sum += i;
            i++;
            if (sum > 10) {
                System.out.println(sum);
                break;
            }
        }

    }
}
