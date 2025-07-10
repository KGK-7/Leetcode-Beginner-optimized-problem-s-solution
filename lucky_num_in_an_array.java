import java.util.HashMap;

public class LuckyIntegerFinder {

    public static int findLucky(int[] arr) {
        
        HashMap<Integer, Integer> freq = new HashMap<>();

        for (int num : arr) {
            if (freq.containsKey(num)) {
                freq.put(num, freq.get(num) + 1);
            } else {
                freq.put(num, 1);
            }
        }

        int lucky = -1;
        for (int num : freq.keySet()) {
            int count = freq.get(num);
            if (num == count) {
                lucky = Math.max(lucky, num);
            }
        }

        return lucky;
    }

    public static void main(String[] args) {
        int[] arr1 = {2, 2, 3, 4};           // Output: 2
        int[] arr2 = {1, 2, 2, 3, 3, 3};     // Output: 3
        int[] arr3 = {2, 2, 2, 3, 3};        // Output: -1

        System.out.println("Lucky in arr1: " + findLucky(arr1));
        System.out.println("Lucky in arr2: " + findLucky(arr2));
        System.out.println("Lucky in arr3: " + findLucky(arr3));
    }
}
