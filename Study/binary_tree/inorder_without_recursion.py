"""
Write a program which takes as input a binary tree and performs an inorder traversal of the tree.
Do not use recursion. Nodes do not contain parent references.
"""
# 1) Create an empty stack S.
# 2) Initialize current node as root
# 3) Push the current node to S and set current = current->left until current is NULL
# 4) If current is NULL and stack is not empty then 
#      a) Pop the top item from stack.
#      b) append the popped item, set current = popped_item->right 
#      c) Go to step 3.
# 5) If current is NULL and stack is empty then we are done.

# Time complexity - O(n)
# Space complexity - O(h)
def inorder_traversal(tree):
    s, result = [], []

    while s or tree:
        if tree:
            s.append(tree)
            tree = tree.left

        else:
            tree = s.pop()
            result.append(tree.data)
            tree = tree.right
    return result
            
