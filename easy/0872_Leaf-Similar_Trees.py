class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, leaf_list):
            if not node:
                return
            if not node.left and not node.right:
                leaf_list.append(node.val)
            dfs(node.left, leaf_list)
            dfs(node.right, leaf_list)
        
        leaf1 = []
        leaf2 = []

        dfs(root1, leaf1)
        dfs(root2, leaf2)

        return leaf1 == leaf2
