package method;

public class MethodValue3 {
    public static void main(String[] args) {
        
        int num1 = 5;
        System.out.println("1. changeNumber 호출 전, num1 : " + num1);
        num1 = changeNumber(num1);
        System.out.println("4. changeNumber 호출 후, num1 : " + num1);
    }
    public static int changeNumber(int number) {
        System.out.println("2. changeNumber 변경 전, number : " + number);
        number = number * 2;
        System.out.println("3. changeNumber 변경 후, number : " + number);
        return number;
    }
}
