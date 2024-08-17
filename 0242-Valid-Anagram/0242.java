import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;

        Map<Character, Integer> mapS = new HashMap<>();
        Map<Character, Integer> mapT = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            mapS.put(s.charAt(i), mapS.getOrDefault(s.charAt(i), 0) + 1);
            mapT.put(t.charAt(i), mapT.getOrDefault(t.charAt(i), 0) + 1);
        }

        for (var pair : mapS.entrySet()) {
            Character c = pair.getKey();
            Integer times = pair.getValue();
            if (!mapT.containsKey(c) || !mapT.get(c).equals(times))
                return false;
        }

        return true;
    }

    public boolean isAnagram1(String s, String t) {
        if (s.length() != t.length())
            return false;

        // the default value in int array is 0
        int[] char1 = new int[26];
        int[] char2 = new int[26];

        for (int i = 0; i < s.length(); i++) {
            char1[s.charAt(i) - 'a']++;
            char2[t.charAt(i) - 'a']++;
        }

        for (int i = 1; i < 26; i++) {
            if (char1[i] != char2[i])
                return false;
        }

        return true;
    }

}