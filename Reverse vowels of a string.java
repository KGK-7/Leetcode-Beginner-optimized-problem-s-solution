class Solution {
    public String reverseVowels(String s) {
        HashSet<Character> vowels = new HashSet<>(Arrays.asList('a','e','i','o','u','A','E','I','O','U'));
        char[] arr = s.toCharArray();
        int left=0, right=arr.length-1;

        while(left < right){
            while(left < right && !vowels.contains(arr[left])) left++;
            while(left < right && !vowels.contains(arr[right])) right--;

            char temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;

            left++ ;
            right-- ;
        }
        return new String(arr);
    }

}