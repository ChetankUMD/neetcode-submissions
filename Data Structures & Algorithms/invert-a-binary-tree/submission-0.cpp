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
    TreeNode* invertTree(TreeNode* root) {
        if(root == NULL){
            return root;
        }
        rInvertTree(root);
        return root;
    }

    void rInvertTree(TreeNode* p){
        queue<TreeNode*> q;
        // cout << p->val << ", " << flush;
        q.emplace(p);
    
        while (! q.empty()){
            p = q.front();
            q.pop();
            TreeNode* temp = p->left;
            p->left = p->right;
            p->right = temp;
            if (p->left){
                // cout << p->left->val << ", " << flush;
                q.emplace(p->left);
            }
    
            if (p->right){
                // cout << p->right->val << ", " << flush;
                q.emplace(p->right);
            }
        }
    }
};