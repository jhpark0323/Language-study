package casting;

public class Casting {
    public static void main(String[] args) {
        double doubleValue = 1.5;
        int intValue = 0;

        // 오류 발생
        // intValue = doubleValue;

        intValue = (int) doubleValue;
        System.out.println("doubleValue = " + doubleValue);
        System.out.println("intValue = " + intValue);

    }
}
