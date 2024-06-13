package method.ex;

public class MethodEx1Ref {
    public static void main(String[] args) {
        int a = 1;
        int b = 2;
        int c = 3;

        int sum = add(a, b, c);
        double average = avg(a, b, c);
        System.out.println("평균값: " + average);

        int x = 15;
        int y = 25;
        int z = 35;

        sum = add(x, y, z);
        average = avg(x, y, z);
        System.out.println("평균값: " + average);
    }
    public static int add(int a, int b, int c) {
        return a+b+c;
    }

    public static double avg(int a, int b, int c) {
        double sum = add(a, b, c);
        return sum / 3.0;
    }

}