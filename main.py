"""
the 2 examples requested
also in the tests folder under
spec_examples

in addition in this location
the explicit displaying of trees
as nested parentheses is printed
"""

from typing import List
from tree_enumeration import beyer_hedetniemi
from tree_enumeration.exhaustive_tree_gen import tree_gen


def do_8_5():
    """
    there are 108 unordered rooted trees
    with exactly 8 nodes and up to 5 leaves
    """
    count_trees = 0
    expected_count = 108
    for cur_tree in tree_gen(8,1,5):
        assert cur_tree.num_nodes == 8
        assert 1 <= cur_tree.num_leaves <= 5
        count_trees += 1
        print(cur_tree)
    assert count_trees == expected_count

    def at_most_five_leaves(level_sequence: List[int]) -> bool:
        count_leaves = 0
        for (z,w) in zip(level_sequence,level_sequence[1:]):
            if z>=w:
                count_leaves += 1
        return count_leaves + 1 <= 5
    count_trees = 0
    for _ in beyer_hedetniemi(8, at_most_five_leaves):
        count_trees += 1
    assert count_trees == expected_count

def do_30_3():
    """
    there are 13661 unordered rooted trees
    with exactly 30 nodes and up to 3 leaves
    """
    count_trees = 0
    # 13450 is the 30'th entry of OEIS A055278
    # the second term is for exactly 2 vertices as in two_leaf property test
    # and 1 for the 1 leaf case
    expected_count = 13450+sum((p-1)//2 for p in range(3,30+1))+1
    for cur_tree in tree_gen(30,1,3):
        assert cur_tree.num_nodes == 30
        assert 1 <= cur_tree.num_leaves <= 3
        count_trees += 1
    assert count_trees == expected_count

if __name__ == "__main__":
    do_8_5()
    do_30_3()
