import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> MyMap=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int diff=target-nums[i];
            if(MyMap.containsKey(diff)){
                return new int[]{MyMap.get(diff),i};
            }
            MyMap.put(nums[i], i);
        }
        return new int[]{};
        
    }
}