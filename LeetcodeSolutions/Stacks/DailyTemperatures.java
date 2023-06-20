import java.util.Arrays;
import java.util.Stack;
public class DailyTemperatures {
    public static void main(String[] args) {
        int[] temperatures = new int[] {73, 74, 75, 71, 69, 72, 76, 73};
        System.out.println(Arrays.toString(dailyTemperatures(temperatures)));
    }

    public static int[] dailyTemperatures(int[] temperatures) {
        int[] result = new int[temperatures.length];
        Stack<Integer> stack = new Stack<>();

        for (int currDay = 0; currDay < temperatures.length; currDay++) {
            while (!stack.isEmpty() && temperatures[currDay] > temperatures[stack.peek()]) {
                int prevDay = stack.pop();
                result[prevDay] = currDay - prevDay;
            }
            stack.add(currDay);
        }

        return result;
    }
}
