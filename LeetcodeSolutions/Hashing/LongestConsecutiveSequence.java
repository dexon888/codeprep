import java.util.HashSet;
public class LongestConsecutiveSequence {
    public static void main(String[] args) {
        int[] nums = new int[] {100, 4, 200, 1, 3, 2};
        System.out.println(longestConsecutive(nums));
    }

    public static int longestConsecutive(int[] nums) {
        HashSet<Integer> numSet = new HashSet<>();

        for (int num : nums) numSet.add(num);

        int maxSequenceLength = 0;

        for (int i = 0; i < nums.length; i++) {
            int currentNum = nums[i];
            int currentSequenceLength = 1;

            if (!numSet.contains(currentNum - 1)) {
                while (numSet.contains(currentNum + 1)) {
                    currentNum += 1;
                    currentSequenceLength +=1;
                }

                maxSequenceLength = Math.max(maxSequenceLength, currentSequenceLength);
            }
        }
        return maxSequenceLength;
    }
}