class Solution {
    public int maxRepeating(String sequence, String word) {
        int count =0;
        String repeated = word;

        while(sequence.contains(repeated)){
            repeated += word;
            count++;
        }
        return count;
    }
}