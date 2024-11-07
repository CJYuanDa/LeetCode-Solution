class Solution {
    public String[] findWords(String[] words) {
        Set<Character> row1 = new HashSet<>(List.of('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'));
        Set<Character> row2 = new HashSet<>(List.of('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'));
        Set<Character> row3 = new HashSet<>(List.of('z', 'x', 'c', 'v', 'b', 'n', 'm'));

        List<String> ans = new ArrayList<>();

        for (String word : words) {
            if (isSubSet(word, row1) || isSubSet(word, row2) || isSubSet(word, row3)) {
                ans.add(word);
            }
        }

        return ans.toArray(new String[0]);
    }

    public boolean isSubSet(String word, Set<Character> row) {
        char[] wordArr = word.toLowerCase().toCharArray();
        for (char c : wordArr) {
            if (!row.contains(c))
                return false;
        }
        return true;
    }
}