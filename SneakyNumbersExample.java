import java.util.HashSet;
class Solution {
    public int[] getSneakyNumbers(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        int arr[] = new int[2];
        int index = 0;
        for(int i =0 ; i<nums.length; i++){
            if(!set.contains(nums[i])){
                set.add(nums[i]);
            }
            else{
                arr[index++] = nums[i];
            }
        }
        return arr;
    }
}

// Example usage
public class SneakyNumbersExample {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {1, 2, 3, 2, 4, 5, 3};
        int[] sneakyNumbers = solution.getSneakyNumbers(nums);
        System.out.println("Sneaky Numbers: " + sneakyNumbers[0] + ", " + sneakyNumbers[1]);
    }
}