class A {
    int m, n;

    void init(int a, int b) {
        int c;
        c = 3;
        this.m = a;
        n = b;
    }
    void work() {
        init(2, 3);
    }
}
public class Main {
    public static void main(String[] args) {
        A a = new A();
        a.work();
        System.out.println(a.m);
        System.out.println(a.n);
    }
}
