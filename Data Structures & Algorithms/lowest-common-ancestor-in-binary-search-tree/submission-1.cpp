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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(p == NULL || q == NULL) return NULL;

        if(p->val > root->val && q->val < root->val){
            return root;
        }
        else if(p->val < root->val && q->val > root->val){
            return root;
        }
        else if(p->val > root->val && q->val > root->val){
            return lowestCommonAncestor(root->right, p , q);
        }
        else if(p->val < root->val && q->val < root->val){
            return lowestCommonAncestor(root->left, p , q);
        }
        else{
            return root;
        }
        return root;
    }
    //     vector<TreeNode*> pathP;
    //     vector<TreeNode*> pathQ;

    //     findPath(root, p, pathP);
    //     findPath(root, q, pathQ);

    //     TreeNode* res = new TreeNode;
    //     res->val = INT_MAX;

    //     for(int i = 0; i<pathP.size();i++){
    //         for(int j=0;j<pathQ.size(); j++){
    //             if(pathP[i]->val == pathQ[j]->val ){
    //                 if(res->val > pathP[i]->val){
    //                     res = pathP[i];
    //                 }
    //             }
    //         }
    //     }

    //     return res;
    // }  

    // bool findPath(TreeNode* root, TreeNode* p, vector<TreeNode*>& path){
    //     if(root == NULL) return false;

    //     path.push_back(root);

    //     if (root->val == p->val){
    //         return true;
    //     }

    //     if(findPath(root->left, p, path) || findPath(root->right,p,path)){
    //         return true;
    //     } 

    //     path.pop_back();
    //     return false;
    // }
};
