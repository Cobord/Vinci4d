"""
an ordered unlabelled tree
they may be used as canonical representatives of unordered trees
but do not have to be
"""
from __future__ import annotations
from typing import List

class OrderedTree:
    """
    an ordered unlabelled tree
    """
    def __init__(self, children: List[OrderedTree], sort_children: bool):
        if len(children) > 0:
            if any(not isinstance(child,OrderedTree) for child in children):
                raise TypeError(f"Expect OrderedTree Got {[type(child) for child in children]}")
        if sort_children:
            children.sort(key = lambda child_tree:
                (child_tree.num_nodes, child_tree.level_sequence()),
                reverse=True,
            )
        self.children = children
        self.num_nodes = sum(child.num_nodes for child in children) + 1
        if len(children) == 0:
            self.num_leaves = 1
        else:
            self.num_leaves = sum(child.num_leaves for child in children)

    @staticmethod
    def degenerate() -> OrderedTree:
        """
        only a root
        """
        return OrderedTree([], False)

    @staticmethod
    def degenerate_path(size: int) -> OrderedTree:
        """
        straight line each having one child
        """
        assert size > 0
        if size == 1:
            return OrderedTree.degenerate()
        return OrderedTree([OrderedTree.degenerate_path(size-1)], False)

    def __str__(self):
        """
        representation as a balanced set of parentheses
        () means just a degenerate tree where it is just the root
        (() ... ()) means a tree with however many children and all of them are leaves
            that only has level 0 for the root and the rest are all at level 1
        """
        to_print = ""
        for child in self.children:
            to_print += str(child)
        return f"({to_print})"

    @staticmethod
    def from_level_sequence(level_sequence: List[int]) -> OrderedTree:
        """
        OrderedTree with the given level sequence
        """
        if len(level_sequence) == 0 or level_sequence[0] != 0:
            raise ValueError("Not a valid level sequence")
        if len(level_sequence) == 1:
            return OrderedTree.degenerate()
        if level_sequence[1] != 1:
            raise ValueError("Not a valid level sequence")
        all_children = []
        one_idcs = (idx for (idx,level) in enumerate(level_sequence) if level == 1)
        current_one_idx = next(one_idcs)
        for next_one_idx in one_idcs:
            child_level_sequence = [z-1 for z in level_sequence[current_one_idx:next_one_idx]]
            all_children.append(OrderedTree.from_level_sequence(child_level_sequence))
            current_one_idx = next_one_idx
        last_child_level_sequence = [z-1 for z in level_sequence[current_one_idx:]]
        all_children.append(OrderedTree.from_level_sequence(last_child_level_sequence))
        return OrderedTree(all_children, False)

    def level_sequence(self):
        """
        as a level sequence of it's preorder traversal
        """
        return self.__level_sequence_helper(0)

    def __level_sequence_helper(self, level_of_root : int) -> List[int]:
        """
        as a level sequence of it's preorder traversal
        """
        to_return = [level_of_root]
        for child in self.children:
            #pylint:disable=protected-access
            to_return.extend(child.__level_sequence_helper(level_of_root+1))
        return to_return

    def good_representative(self) -> bool:
        """
        the children are sorted such that
        - larger subtrees occur before smaller subtrees
        - if two adjacent sibling subtrees are equal in number of nodes, then
            the level sequence of the first is less than or equal to the second
        """
        child_sizes = [child.num_nodes for child in self.children]
        for (idx,(a,b)) in enumerate(zip(child_sizes, child_sizes[1:])):
            if b>a:
                return False
            if a==b:
                a_level_seq = self.children[idx].level_sequence()
                b_level_seq = self.children[idx+1].level_sequence()
                if a_level_seq<b_level_seq:
                    return False
        return True
