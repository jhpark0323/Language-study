import java.util.ArrayList;
import java.util.List;

public class ListTest1 {
    public static void main(String[] args) {
        List<String> names = new ArrayList<String>();

        names.add("가");
        names.add("나");
        names.add("다");
        names.add("나");

        System.out.println(names);

        System.out.println(names.isEmpty());

        names.remove(0);
        System.out.println(names);

        names.remove("다");
        System.out.println(names);


        names.clear();
        System.out.println(names);

        names.add("학생1");
        names.add("학생1");
        names.add("학생2");
        System.out.println(names);

        for (int i=names.size()-1; i >= 0; i--) {
            if (names.get(i).equals("학생1"))
                names.remove(i);
        }
        System.out.println(names);


    }
}