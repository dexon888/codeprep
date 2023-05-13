import java.util.Arrays;
public class ValidAnagram {
    public static void main(String[] args) {
        String s = "cat";
        String t = "taco";

        System.out.println(validAnagram(s,t));
    }

    public static boolean validAnagram(String s, String t) {
        int[] arr1  = new int[26];
        int[] arr2 = new int[26];

        if (s.length() != t.length()) return false;

        for (int i = 0; i < s.length(); i++) {
            arr1[s.charAt(i) - 'a']++;
            arr2[t.charAt(i) - 'a']++;
        }

        return Arrays.equals(arr1, arr2);
    }
}