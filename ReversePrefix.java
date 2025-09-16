class Solution {
    public String reversePrefix(String word, char ch) {
        int index = word.indexOf(ch);
        if(index == -1){
            return word;
        }
        StringBuilder rev_part = new StringBuilder(word.substring(0, index+1));
        rev_part.reverse();
        return rev_part.toString() + word.substring(index+1); 
    }
}