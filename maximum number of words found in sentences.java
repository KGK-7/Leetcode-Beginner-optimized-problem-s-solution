class Solution {
    public int mostWordsFound(String[] sentences) {
        int maxWords = 0;
        for( String sentence : sentences){
            String word[] = sentence.split(" ");
            maxWords = Math.max(maxWords, word.length);
        }
        return maxWords;
    }
}