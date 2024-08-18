import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] arrayS = s.split(" ");
        if (pattern.length() != arrayS.length)
            return false;

        Map<Character, String> mapPattern = new HashMap<>();
        Map<String, Character> mapS = new HashMap<>();

        for (int i = 0; i < pattern.length(); i++) {
            Character c = pattern.charAt(i);
            String w = arrayS[i];

            if (mapPattern.containsKey(c) && !mapPattern.get(c).equals(w))
                return false;
            if (mapS.containsKey(w) && !mapS.get(w).equals(c))
                return false;

            mapPattern.put(c, w);
            mapS.put(w, c);
        }

        return true;
    }
}