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

    struct TreeNode *queue[10000];
    
    int front = 0;
    int rear = 0;
    int depth = 0;

    queue[rear++] = root;

    while(front < rear){
        int size = rear - front;

        for(int i =0; i < size; i++){
            struct TreeNode *node = queue[front++];

            if(node->left != NULL){
                queue[rear++] = node->left;
            }
            if(node->right != NULL){
                queue[rear++] = node -> right;
            }
        }
        depth ++;
    }
    return depth;

}
