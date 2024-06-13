package method.ex;

public class MethodEx2Ref {
    public static void main(String[] args) {
        printString("Hello Wolrd!", 5);
    }

    public static void printString(String message, int n) {
        for (int i=0; i < n; i++) {
            System.out.println(message);
        }
    }
}
