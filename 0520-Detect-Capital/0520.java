class Solution {
    public boolean detectCapitalUse(String word) {
        int count = 0;
        char[] wordArray = word.toCharArray();

        for (char letter : wordArray) {
            if (Character.isUpperCase(letter))
                count++;
        }

        if (count == word.length())
            return true;
        if (count == 1 && Character.isUpperCase(wordArray[0]))
            return true;
        if (count == 0)
            return true;

        return false;
    }
}