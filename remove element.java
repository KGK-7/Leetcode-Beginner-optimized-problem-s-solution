
class Solution {

    public int removeElement(int[] nums, int val) {
        int k = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[k] = nums[i];
                k += 1;
            }
        }
        return k;
    }
}

// Time Complexity: O(n)
// Space Complexity: O(1)
// The function iterates through the array once, checking each element.
// If the element is not equal to val, it is moved to the front of the array.
// The variable k keeps track of the number of elements that are not equal to val.
// The function returns k, which is the new length of the array after removing elements equal to val.
// The original array is modified in place, and the elements that are not equal to val are moved to the front.
// The elements that are equal to val are effectively removed from the array, as they are not included in the first k elements.
// Example usage:
// int[] nums = {3, 2, 2, 3};
// int val = 3;
// Solution solution = new Solution();
// int newLength = solution.removeElement(nums, val);
// System.out.println(newLength); // Output: 2
// System.out.println(Arrays.toString(Arrays.copyOf(nums, newLength))); // Output: [2, 2]
// The first two elements of nums are now 2, and the length of the modified array is 2.
// The elements that were equal to 3 have been removed, and the array has been modified in place.
// Note: The order of the elements that are not equal to val is preserved in the modified array.
// The elements that are equal to val are not included in the first k elements, effectively removing them from the array.
// The function does not create a new array, so it uses O(1) space.
// The function can be used to remove any specified value from an array, and it works for any integer array.
// The function is efficient and works well for large arrays, as it only requires a single pass through the array.
// The function can be used in various scenarios where elements need to be removed from an array based on a specific value.
// The function is generic and can be used with any integer array and any integer value to be removed.
// The function is simple and easy to understand, making it suitable for various applications.
