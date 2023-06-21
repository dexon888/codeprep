import java.util.List;
import java.util.ArrayList;

public class GenerateParentheses {
    public static void main(String[] args) {
        System.out.println(generateParentheses(3).toString());
    }

    public static List<String> generateParentheses(int n) {
        List<String> result = new ArrayList<>();
        generateParentheses(result, "", 0, 0, n);
        return result;
    }

    private static void generateParentheses(List<String> result, String s, int open, int close, int n) {
        if (open == n && close == n) {
            result.add(s);
            return;
        }

        if (open < n) {
            generateParentheses(result, s + "(" , open + 1, close, n);
        }

        if (close < open) {
            generateParentheses(result, s + ")", open, close + 1, n);
        }
    }
}