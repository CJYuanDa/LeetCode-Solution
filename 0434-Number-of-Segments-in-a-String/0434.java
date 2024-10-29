class Solution {
    public int countSegments(String s) {
        if (s == null || s.trim().isEmpty())
            return 0;
        // use trim to erase the front or rear spaces, " foo bar " -> "foo bar"
        String[] arrayS = s.trim().split("\\s+");
        return arrayS.length;
    }
}