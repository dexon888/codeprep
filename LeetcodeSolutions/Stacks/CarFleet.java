import java.util.Arrays;
import java.util.Stack;
public class CarFleet {
    public static void main(String[] args) {
        int target = 12;
        int[] position = {10, 8, 0, 5, 3};
        int[] speed = {2,4,1,1,3};
        System.out.println(carFleet(target, position, speed));
    }

    public static int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        if (n == 0) return 0;

        //Make a car array to store position and time
        Car[] cars = new Car[n];
        for (int i = 0; i < n; i++) {
            cars[i] = new Car(position[i] , (double)(target - position[i]) / speed[i]);
        }
        //Sort the cars based on increasing position from least to greatest
        Arrays.sort(cars, (a,b) -> a.position - b.position);

        //Initialize a montonic decreasing stack
        Stack<Double> stack = new Stack<>();
        //For each element from the back, we're trying to find an arrival time which is greater than the top of the stack (which means it joins the fleet)
        for (int i = cars.length - 1; i >= 0; i--) {
            if (!stack.isEmpty() && cars[i].time <= stack.peek()) continue;
            else stack.push(cars[i].time);
        }
        //Simply return the size of the stack
        return stack.size();
    }

    private static class Car {
        int position;
        double time;

        Car(int position, double time) {
            this.position = position;
            this.time = time;
        }
    }
}
