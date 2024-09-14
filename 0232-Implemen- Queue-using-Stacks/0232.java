import java.util.Stack;

class MyQueue {

    Stack<Integer> S1;
    Stack<Integer> S2;

    public MyQueue() {
        S1 = new Stack<>();
        S2 = new Stack<>();
    }

    public void push(int x) {
        S1.push(x);
    }

    public int pop() {
        if (S2.empty()) {
            while (!S1.empty()) {
                S2.push(S1.pop());
            }
        }

        return S2.pop();
    }

    public int peek() {
        if (S2.empty()) {
            while (!S1.empty()) {
                S2.push(S1.pop());
            }
        }

        return S2.peek();
    }

    public boolean empty() {
        return S1.empty() && S2.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */