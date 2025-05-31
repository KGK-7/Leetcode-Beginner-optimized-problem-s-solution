
class Solution {

    public String convertToTitle(int columnNumber) {
        StringBuilder sb = new StringBuilder();
        int col = columnNumber;

        while (col > 0) {
            col -= 1;
            sb.insert(0, (char) ('A' + (col % 26)));
            col /= 26;
        }
        return sb.toString();
    }
}

public class excelNumberToTitle {

    public static void main(String[] args) {
        Solution sol = new Solution();
        // Example usage
        System.out.println(sol.convertToTitle(1));   // Output: "A"
        System.out.println(sol.convertToTitle(28));  // Output: "AB"
        System.out.println(sol.convertToTitle(701)); // Output: "ZY"
    }
}
