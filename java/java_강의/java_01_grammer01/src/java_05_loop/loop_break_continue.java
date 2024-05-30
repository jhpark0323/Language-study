package java_05_loop;

public class loop_break_continue {
    public static void main(String[] args) {
        // label을 통해 내가 빠져나갈 블록을 지정할 수도 있음
        // 이중 for문이라도 label으로 첫번째 for문을 지정해두면 한번에 빠져나올 수 있음
        out: for (int i = 2; i <= 9; i++) {
        System.out.println(i + "단");
        for (int j = 1; j <= 9; j++) {
            if (j > 5)
                break out;
            System.out.printf("%d + %d = %d\n", i, j, i * j);
        }
        }
    }
}
