class Solution {
    public int lengthOfLastWord(String s) {
        String regex = " ";
        String[] array = s.split(regex);
        return array[array.length - 1].length();
    }

    public int otherSolution(String s) {
        // Find the last space in the trimmed string
        s = s.trim();

        // The length of the last word is the difference between the string's length and
        // the last space index
        int lastSpaceIndex = s.lastIndexOf(" ");

        return s.length() - lastSpaceIndex - 1;
    }
}
