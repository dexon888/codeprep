import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.Arrays;
public class TopKFrequentElements {
    public static void main(String[] args) {
        int[] nums = new int[]{1,1,1,2,2,3};
        int k = 2;
        System.out.println(Arrays.toString(topKFrequent(nums, k)));
    }

    public static int[] topKFrequent(int[] nums, int k) {
        if (k == nums.length) return nums;

        HashMap<Integer, Integer> map = new HashMap<>();

        //Place counts for each number in the HashMap
        for (int num: nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(
            (n1, n2) -> map.get(n1) - map.get(n2)
        );

        for (int num: map.keySet()) {
            pq.add(num);
            if (pq.size() > k) pq.poll();
        }

        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = pq.poll();
        }
        return result;
    }
}