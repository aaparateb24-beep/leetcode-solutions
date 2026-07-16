# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
         # This list will store the leaf values of Tree 1
        leaves1 = []
        leaves2 = []
         # DFS function to collect all leaf nodes
        # ---------------------------------------------------
        def dfs(node, leaves):
            if not node:
                return 
                # Check if the current node is a LEAF
            # A leaf has NO left child and NO right child.
            # ------------------------------------------------
            if not node.left and not node.right :
                leaves.append(node.val)
                return 
             # Visit the left subtree
            dfs(node.left, leaves)

            # Visit the right subtree
            dfs(node.right, leaves)

        # Collect leaves from the first tree
        dfs(root1, leaves1)

        # Collect leaves from the second tree
        dfs(root2, leaves2)
        # Compare the leaf sequences
        if leaves1 == leaves2:
            return True 
        else:
            return False        