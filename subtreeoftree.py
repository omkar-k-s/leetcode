class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """

        def sameTree(a, b):
            # Both are empty
            if not a and not b:
                return True

            # One is empty, other is not
            if not a or not b:
                return False

            # Values are different
            if a.val != b.val:
                return False

            # Check left and right subtrees
            return sameTree(a.left, b.left) and sameTree(a.right, b.right)

        # If subRoot is empty, it is a subtree
        if not subRoot:
            return True

        # If root becomes empty, subRoot cannot be found
        if not root:
            return False

        # Check if trees starting at current node are identical
        if sameTree(root, subRoot):
            return True

        # Search in left or right subtree
        return self.isSubtree(root.left, subRoot) or \
               self.isSubtree(root.right, subRoot)