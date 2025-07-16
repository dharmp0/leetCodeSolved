class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = [(root, str(root.val))]
        total = 0
        
        while stack:
            
            node, currentstr = stack.pop()
            
            if not node.right and not node.left:
                
                total += int(currentstr)
                
                
            if node.left:
                
                stack.append((node.left, currentstr + str(node.left.val)))
            
            if node.right:

                stack.append((node.right, currentstr + str(node.right.val)))
            
            
        return total
