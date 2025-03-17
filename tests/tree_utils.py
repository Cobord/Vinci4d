"""
the methods on OrderedTree
"""

from typing import List
from hypothesis import given, strategies as st
from tree_enumeration.brute_recurse import OrderedTree

def test_simple_trees():
    """
    simply constructed trees give expected level sequence
    """
    tree_test = OrderedTree.degenerate()
    assert str(tree_test) == "()"
    assert tree_test.num_nodes == 1
    assert tree_test.num_leaves == 1
    tree_test = OrderedTree([
        OrderedTree.degenerate(),
        OrderedTree.degenerate(),
        OrderedTree.degenerate()], False)
    assert tree_test.num_nodes == 4
    assert tree_test.num_leaves == 3
    assert str(tree_test) == "(()()())"
    assert tree_test.level_sequence() == [0,1,1,1]
    assert OrderedTree.from_level_sequence([0,1,1,1]).level_sequence() == [0,1,1,1]
    tree_test = OrderedTree([OrderedTree.degenerate(), tree_test], False)
    assert tree_test.num_nodes == 6
    assert tree_test.num_leaves == 4
    assert str(tree_test) == "(()(()()()))"
    assert tree_test.level_sequence() == [0,1,1,2,2,2]
    assert OrderedTree.from_level_sequence([0,1,1,2,2,2]).level_sequence() == [0,1,1,2,2,2]
    cur_str = "()"
    for idx in range(2,10):
        tree_test = OrderedTree.degenerate_path(idx)
        assert tree_test.num_nodes == idx
        assert tree_test.num_leaves == 1
        assert tree_test.level_sequence() == list(range(idx))
        assert str(tree_test) == f"({cur_str})"
        cur_str = f"({cur_str})"
        assert OrderedTree\
            .from_level_sequence(list(range(idx)))\
            .level_sequence() == list(range(idx))

@given(st.lists(st.integers(0,5),min_size=1,max_size=10))
def round_trip(trial_level_sequence: List[int]):
    """
    constructing a tree from level sequence
    and then giving back that same level sequence
    """
    try:
        found_tree = OrderedTree.from_level_sequence(trial_level_sequence)
        redone_level_sequence = found_tree.level_sequence()
        assert redone_level_sequence == trial_level_sequence
    except ValueError:
        pass
