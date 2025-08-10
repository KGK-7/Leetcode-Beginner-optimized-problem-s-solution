class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int n = nums.length;
        int evenIndex = 0;
        int oddIndex = n -1;
        int arr[] = new int[n];
        for(int i=0 ; i< n; i++){
            if(nums[i] % 2 == 0 ){
                arr[evenIndex] = nums[i];
                evenIndex++ ;   
            }
            else{
                arr[oddIndex] = nums[i];
                oddIndex-- ;
            }
        }
        return arr;
    }
}