from typing import List


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]: # type: ignore
        self.prev = None
        self.max_count = 0
        self.current_count = 0
        self.modes = []
        
        # First pass to find max_count
        self.inorder(root, True)
        
        # Reset for the second pass
        self.prev = None
        self.current_count = 0
        
        # Second pass to collect modes
        self.inorder(root, False)
        
        return self.modes

    def inorder(self, node, is_first_pass):
        if not node:
            return
        
        self.inorder(node.left, is_first_pass)
        
        # Update the current count based on previous value
        if self.prev == node.val:
            self.current_count += 1
        else:
            self.current_count = 1
        
        if is_first_pass:
            # First pass: just track the max_count
            if self.current_count > self.max_count:
                self.max_count = self.current_count
        else:
            # Second pass: collect modes if count matches max_count
            if self.current_count == self.max_count:
                self.modes.append(node.val)
        
        # Update prev to the current node's value
        self.prev = node.val
        
        self.inorder(node.right, is_first_pass)