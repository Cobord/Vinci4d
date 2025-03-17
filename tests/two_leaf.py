"""
the count of unordered rooted trees with exactly 2 leaves and n nodes
is analytically determined
"""

from hypothesis import given, strategies as st

from tree_enumeration import tree_gen

@given(st.integers(0,30))
def test_2_leaf_trees(input_size: int):
    """
    the count of unordered rooted trees with exactly 2 leaves and n nodes
    is analytically determined
    """
    count_trees = 0
    for _ in tree_gen(input_size,2,2):
        count_trees += 1
    expected_count = sum((p-1)//2 for p in range(3,input_size+1))
    assert count_trees == expected_count
