class Solution {
public:
    void generateParenthesisHelper(int open, int close, string current, vector<string>& result) {
    // Base case: if no more parentheses can be added, add the current string to the result
    if (open == 0 && close == 0) {
        result.push_back(current);
        return;
    }

    // If there are open parentheses left to add, add one and recurse
    if (open > 0) {
        generateParenthesisHelper(open - 1, close, current + "(", result);
    }

    // If there are more closing parentheses available than open ones, add a closing parenthesis and recurse
    if (close > open) {
        generateParenthesisHelper(open, close - 1, current + ")", result);
    }
}

vector<string> generateParenthesis(int n) {
    vector<string> result;
    generateParenthesisHelper(n, n, "", result); // Start with n open and close parentheses available
    return result;
}
};
