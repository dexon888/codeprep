import java.util.Stack;
public class EvaluateReversePolishNotation {
    public static void main(String[] args) {
        String[] tokens = new String[] {"2", "1", "+", "3", "*"};
        System.out.println(evalRPN(tokens));
    }

    public static int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for (String str : tokens) {
            if (str.equals("+")) {
                stack.add(stack.pop() + stack.pop());
            } else if (str.equals("-")) {
                int a = stack.pop();
                int b = stack.pop();
                stack.add(b - a);
            } else if (str.equals("*")) {
                stack.add(stack.pop() * stack.pop());
            } else if (str.equals("/")) {
                int a = stack.pop();
                int b = stack.pop();
                stack.add(b / a);
            } else {
                stack.add(Integer.parseInt(str));
            }
        }

        return stack.pop();
    }
}