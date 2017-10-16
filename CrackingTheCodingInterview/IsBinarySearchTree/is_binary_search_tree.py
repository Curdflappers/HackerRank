""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    return checkBST_helper(root, -1, 10001)

def checkBST_helper(root, min, max):
    """Make sure all elements in the tree are
        < n if left_side
        > n if !left_side
    """
    if root == None or root.left == None and root.right == None:
        return True
    
    if root.left != None \
    and (root.left.data >= root.data or root.left.data <= min) \
    or root.right != None \
    and (root.right.data <= root.data or root.right.data >= max):
        return False
    
    return checkBST_helper(root.left, min, root.data) \
            and checkBST_helper(root.right, root.data, max)