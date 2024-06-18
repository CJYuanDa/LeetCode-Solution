import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        char[] charArray = s.toCharArray();
        for (char c : charArray) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else if (!stack.empty() && c == ')' && stack.peek() == '(') {
                stack.pop();
            } else if (!stack.empty() && c == '}' && stack.peek() == '{') {
                stack.pop();
            } else if (!stack.empty() && c == ']' && stack.peek() == '[') {
                stack.pop();
            } else {
                return false;
            }
        }
        return stack.empty();
    }
}