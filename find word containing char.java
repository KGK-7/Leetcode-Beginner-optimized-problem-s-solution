class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        List<Integer> char_index = new ArrayList<>(); 
        for (int i = 0 ; i< words.length ; i++) {
            if ( words[i].indexOf(x) != -1){
                char_index.add(i);
            }
        }
        return char_index;
    }
}