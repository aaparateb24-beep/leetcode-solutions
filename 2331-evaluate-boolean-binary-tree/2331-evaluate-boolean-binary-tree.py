class Solution:

    def evaluateTree(self, root):

        # Base Case:
        # If this is a leaf node,
        # return its boolean value.
        if not root.left and not root.right:
            return root.val == 1

        # Evaluate the left subtree.
        left = self.evaluateTree(root.left)

        # Evaluate the right subtree.
        right = self.evaluateTree(root.right)

        # OR operation
        if root.val == 2:
            return left or right

        # AND operation
        return left and right
        