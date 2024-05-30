package java_04_if_else;

public class switch_case {
    public static void main(String[] args) {
        int month = 12;

        switch (month) {
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                System.out.println("31일");
                break;
            case 4:
            case 6:
                System.out.println("30일");
        }
    }
}
