from collections import deque
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        head = None
        queue = deque()
        queue.append(root)
        while queue and head == None:
            node = queue.popleft()
            if node:
                if node.val == val:
                    head = node
                queue.append(node.right)
                queue.append(node.left)
        return head
