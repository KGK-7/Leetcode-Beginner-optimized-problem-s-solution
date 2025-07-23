class Solution {
    public int countDigits(int num) {
        int result = 0;
        int n = num;
        while(n > 0){
            result += (num % (n % 10) == 0) ? 1 : 0;
            n/=10;
        }
        return result;
    }
}