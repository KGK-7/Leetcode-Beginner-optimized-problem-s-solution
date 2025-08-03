class Solution {
    public String removeOuterParentheses(String s) {
        StringBuilder bracket = new StringBuilder();
        int start = 0, balance = 0;

        for( int i =0 ; i<s.length(); i++){
            if ( s.charAt(i) == '('){
                balance++ ;
            }
            else{
                balance-- ;
            }
            if( balance == 0){
                bracket.append(s.substring(start + 1, i));
                start = i+1;
            }
        }
        return bracket.toString();
        
    }
}

// The code defines a class Solution with a method removeOuterParentheses that takes a string s as input.
// The method removes the outermost parentheses from each primitive substring of s.
// It uses a StringBuilder to build the result and keeps track of the balance of parentheses.
// The method iterates through the string, updating the balance for each parenthesis encountered.
// When the balance reaches zero, it appends the substring from the start index (excluding the outer parentheses) to the StringBuilder.
// Finally, it returns the resulting string without the outer parentheses.
// The time complexity of this solution is O(n), where n is the length of the input string s.
// The space complexity is O(n) as well, due to the use of StringBuilder to store the result.
