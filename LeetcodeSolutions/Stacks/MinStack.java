import java.util.Stack;
public class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> minStack;
    public static void main(String[] args) {
        MinStack obj = new MinStack();
        obj.push(3);
        System.out.println(obj.top());
        System.out.println(obj.getMin());
    }
    
    public MinStack() {
        stack = new Stack<Integer>();
        minStack = new Stack<Integer>();
    }

    public void push (int val) {
        stack.push(val);

        int minValue = Math.min(val, minStack.isEmpty() ? val : minStack.peek());
        minStack.push(minValue);
    }

    public void pop() {
        stack.pop();
        minStack.pop();
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return minStack.peek();
    }
}
