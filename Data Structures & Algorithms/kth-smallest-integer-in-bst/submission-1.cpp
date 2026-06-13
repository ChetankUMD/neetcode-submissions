/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        int n = 0;
        stack<TreeNode*> st;
        TreeNode* node = root;
        
        while(node != NULL || !st.empty()){
            while(node != NULL){
                st.push(node);
                node = node->left;
            }
            node = st.top();
            st.pop();
            n++;
            if(n==k){
                return node->val;
            }
            node = node->right;
        }
    }

    // int kthSmallest(TreeNode* root, int k) {
    //     vector<int> arr;
    //     dfs(root, arr);
    //     return arr[k-1];
    // }

    // void dfs(TreeNode* root, vector<int>& arr){
    //     if(root==NULL) return;
    //     dfs(root->left, arr);
    //     arr.push_back(root->val);
    //     dfs(root->right, arr);
    // }
};
