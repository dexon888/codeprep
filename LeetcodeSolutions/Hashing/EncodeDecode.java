import java.util.List;
import java.util.ArrayList;
public class EncodeDecode {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("Bob");
        list.add("has");
        list.add("three");
        list.add("apples");
        System.out.println(encode(list));
        String result = encode(list);
        System.out.println(decode(result).toString());
    }

    public static String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String str : strs) {
            sb.append(str.length() + "#" + str);
        }
        return sb.toString();
    }

    public static List<String> decode(String str) {
        List<String> result = new ArrayList<>();
        int i = 0; 
        while (i < str.length()) {
            int j = i;
            while (str.charAt(j) != '#') {
                j++;
            }

            Integer number = Integer.parseInt(str.substring(i, j));
            i = j + 1 + number;
            result.add(str.substring(j + 1, i));
        }

        return result;
    }
}
