from collections import deque
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                if node.val == val:
                    return node
                queue.append(node.left)
                queue.append(node.right)
        return None
