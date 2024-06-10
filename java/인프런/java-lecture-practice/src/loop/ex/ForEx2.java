package loop.ex;

public class ForEx2 {
    public static void main(String[] args) {
        int sum = 0;
        int max = 100;
        for (int i = 0; i <= max; i++) {
            sum += i;
            System.out.printf("max = %d\n" + sum + "\n", i);
        }

    }
}
