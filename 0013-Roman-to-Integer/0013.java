class Solution {
    public int romanToInt(String s) {
        // last index
        int idx = s.length() - 1;
        int answer = 0;

        for (int i = idx; i >= 0; i--) {
            if (s.charAt(i) == 'I') {
                if (i < idx && (s.charAt(i + 1) == 'V' || s.charAt(i + 1) == 'X'))
                    answer -= 1;
                else
                    answer += 1;
            } else if (s.charAt(i) == 'V') {
                answer += 5;
            } else if (s.charAt(i) == 'X') {
                if (i < idx && (s.charAt(i + 1) == 'L' || s.charAt(i + 1) == 'C'))
                    answer -= 10;
                else
                    answer += 10;
            } else if (s.charAt(i) == 'L') {
                answer += 50;
            } else if (s.charAt(i) == 'C') {
                if (i < idx && (s.charAt(i + 1) == 'D' || s.charAt(i + 1) == 'M'))
                    answer -= 100;
                else
                    answer += 100;
            } else if (s.charAt(i) == 'D') {
                answer += 500;
            } else if (s.charAt(i) == 'M') {
                answer += 1000;
            }
        }
        return answer;
    }
}