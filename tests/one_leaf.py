"""
the count of unordered rooted trees with exactly 1 leaf and n nodes
is 1
"""

from hypothesis import given, strategies as st

from tree_enumeration import tree_gen

@given(st.integers(0,100))
def test_1_leaf_trees(input_size: int):
    """
    the count of unordered rooted trees with exactly 1 leaf and n nodes
    is 1
    """
    count_trees = 0
    for cur_tree in tree_gen(input_size,1,1):
        count_trees += 1
        assert cur_tree.level_sequence() == list(range(input_size))
    assert count_trees == (1 if input_size>0 else 0)
