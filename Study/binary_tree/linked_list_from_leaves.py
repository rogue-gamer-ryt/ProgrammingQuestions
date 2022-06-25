"""
In some applications of a binary tree, only the leaf nodes contain actual information. For example,
the outcomes of matches in a tennis toumament can be represented by a binary tree where leaves
are players. The internal nodes correspond to matches, with a single winner advancing. For such a
tree, we can link the leaves to get a list of participants.

Given a binary tree, compute a linked list from the leaves of the binary tree. The leaves should
appear in left-to-right order. For example, when
"""

# Time complexity O(n)
# Space complexity O(h)
def create_list_of_leaves(tree):
    if not tree:
        return []
    if not tree.left and not tree.right:
        return [tree]
    return create_list_of_leaves(tree.left) + create_list_of_leaves(tree.right)