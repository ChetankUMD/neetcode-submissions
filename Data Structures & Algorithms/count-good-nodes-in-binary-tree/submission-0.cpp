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
    int res = 1;
    int goodNodes(TreeNode* root) {
        if(root == NULL) return 0;
        countgood(root->left, root->val);
        countgood(root->right, root->val);

        return res;
    }

    void countgood(TreeNode* p, int max){
        if(p == NULL) return;
        if(p->val >= max){
            res++;
            max = p->val;
        }
        countgood(p->left, max);
        countgood(p->right, max);
    }
};
