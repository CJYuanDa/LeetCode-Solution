class Solution {
    public String addBinary(String a, String b) {
        // find the last index of each string
        int lastIdxA = a.length() - 1;
        int lastIdxB = b.length() - 1;

        // create answer s and sum
        String s = "";
        int sum = 0;

        while (lastIdxA >= 0 || lastIdxB >= 0 || sum > 0) {

            // convert character into int, '1' -> 1
            if (lastIdxA >= 0) {
                sum += Character.getNumericValue(a.charAt(lastIdxA));
                lastIdxA--;
            }
            if (lastIdxB >= 0) {
                sum += Character.getNumericValue(b.charAt(lastIdxB));
                lastIdxB--;
            }

            // put the number in front of the s
            s = Integer.toString(sum % 2) + s;
            sum /= 2;
        }
        return s;
    }
}