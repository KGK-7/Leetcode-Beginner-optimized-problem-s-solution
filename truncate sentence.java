class Solution {
    public String truncateSentence(String s, int k) {
        String words[] = s.split(" ");
        String result = words[0];

        for ( int i=1 ; i < k; i++){
            result += " " + words[i];
        } 
        return result;
    }
}