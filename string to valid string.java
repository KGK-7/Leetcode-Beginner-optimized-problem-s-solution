class Solution {
    public int balancedStringSplit(String s) {
        int balance = 0;
        int count = 0;
        char[] ss = s.toCharArray();

        for( char c : ss ){
            if (c == 'R'){
                balance += 1;
            }
            else{
                balance -= 1;
            }

            if( balance == 0){
                count += 1;
            }
        }
        return count;
    }
}