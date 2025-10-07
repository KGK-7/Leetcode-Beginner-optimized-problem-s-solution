import java.util.*;
class UniqueNumberofOccurrences {
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer, Integer> freq = new HashMap<>();
        for( int num : arr){
            freq.put(num, freq.getOrDefault(num, 0) +1);
        }
        HashSet<Integer> s = new HashSet<>(freq.values());
        return freq.size() == s.size();
    }
}