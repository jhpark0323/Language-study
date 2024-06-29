import java.util.HashSet;
import java.util.Iterator;

public class SetDemo {
    public static void main(String[] args) {
        HashSet<Integer> A = new HashSet<Integer>();
        A.add(1);
        A.add(2);
        A.add(3);

        Iterator hi = (Iterator) A.iterator();
        while (hi.hasNext()) {
            System.out.println(hi.next());
        }

        HashSet<Integer> B = new HashSet<Integer>();
        B.add(3);
        B.add(4);
        B.add(5);

//        A.addAll(B);
//        A.retainAll(B);
//        A.removeAll(B);

        Iterator hi1 = (Iterator) A.iterator();
        while (hi1.hasNext()) {
            System.out.println(hi1.next());
        }

        HashSet<Integer> C = new HashSet<Integer>();
        C.add(1);
        C.add(2);
        C.add(3);

    }
}