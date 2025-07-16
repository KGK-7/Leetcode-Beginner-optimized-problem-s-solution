class Solution {
    public int minimumSum(int num) {
        char[] digits = String.valueOf(num).toCharArray();
        Arrays.sort(digits);
        int n1 = Integer.parseInt("" + digits[0] + digits[2]);
        int n2 = Integer.parseInt("" + digits[1] + digits[3]);

        return n1 + n2;
    }
}