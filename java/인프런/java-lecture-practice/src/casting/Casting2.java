package casting;

public class Casting2 {
    public static void main(String[] args) {
        
        long maxIntValue = 1000;
        long maxIntOver = 2147483648L;
        int intValue = 0;
        
        intValue = (int) maxIntValue;
        System.out.println("intValue = " + intValue);

        // 초과범위
        // 자신의 타입을 벗어나면 제일 작은수부터 다시 표현
        // 시계 61분 -> 1분 느낌
        intValue = (int) maxIntOver;
        System.out.println("intValue = " + intValue);
    }
}
