class MinStack {
private:
    stack<int> mainStack;
    stack<int> minStack;
public:
    MinStack() {
    }
    
    void push(int val) {
        mainStack.push(val);
        if(minStack.empty() || val <= minStack.top()){
            minStack.push(val);
        }
    }
    
    void pop() {
        if(mainStack.empty()) return;
        int val = mainStack.top();
        if(minStack.top() == val){
            minStack.pop();
        }
        mainStack.pop();
    }
    
    int top() {
        return mainStack.top();
    }
    
    int getMin() {
        return minStack.top();
    }
};
