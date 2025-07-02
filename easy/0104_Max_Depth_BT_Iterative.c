/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root) {
    if(root == NULL){
        return 0;
    }
    int depth[10000];
    struct TreeNode *stack[10000];
    int max_depth = 0, top = 0;
    
    stack[top] = root; 
    depth[top] = 1; 
    top++; 
    while(top > 0){
        top--; 
        struct TreeNode *node = stack[top];
        int curr_depth = depth[top];

        if(node->left != NULL){
            stack[top] = node->left;
            depth[top] = curr_depth +1;
            top++; 
            
        }
        if(node->right != NULL){
            stack[top] = node->right;
            depth[top] = curr_depth +1;
            top++;
        }
        if(max_depth< curr_depth){
            max_depth = curr_depth;
        }
    }

    return max_depth;

    }
