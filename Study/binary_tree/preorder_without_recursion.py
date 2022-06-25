"""
Write a program which takes as input a binary tree and performs a preorder traversal of the tree.
Do not use recursion. Nodes do not contain parent references.
"""

# Algorithm Preorder(tree)
#    1. Visit the root.
#    2. Traverse the left subtree, i.e., call Preorder(left-subtree)
#    3. Traverse the right subtree, i.e., call Preorder(right-subtree)

# Use a stack and push right child and then left child
# Pass left child later on as that should be popped first

# Time complexity - O(n)
# Space complexity - O(h)
def preorder_traversal(tree):
    path , resul = [tree], []

    while path:
        curr = path.pop()
        if curr:
            result.append(curr.data)
            path += [curr.right , curr.left]

    return result
