"""
the examples provided in the spec document
"""

from tree_enumeration import tree_gen

#pylint:disable=duplicate-code
def test_4_3():
    """
    there are the explicitly described 4 unordered rooted trees
    with exactly 4 nodes and up to 3 leaves
    """
    count_trees = 0
    expected_level_sequences = [
        [0,1,2,3],
        [0,1,2,2],
        [0,1,2,1],
        [0,1,1,1]
    ]
    for cur_tree in tree_gen(4,1,4):
        cur_level_sequence = cur_tree.level_sequence()
        assert cur_level_sequence in expected_level_sequences
        expected_level_sequences.remove(cur_level_sequence)
        count_trees += 1
    assert count_trees == 4

def test_7_2():
    """
    there are the explicitly described 10 unordered rooted trees
    with exactly 7 nodes and up to 2 leaves
    """
    count_trees = 0
    expected_level_sequences = [
        [0,1,2,3,4,5,6],
        [0,1,2,3,4,5,5],
        [0,1,2,3,4,5,4],
        [0,1,2,3,4,5,3],
        [0,1,2,3,4,3,4],
        [0,1,2,3,4,5,2],
        [0,1,2,3,4,2,3],
        [0,1,2,3,4,5,1],
        [0,1,2,3,4,1,2],
        [0,1,2,3,1,2,3],
    ]
    for cur_tree in tree_gen(7,1,2):
        cur_level_sequence = cur_tree.level_sequence()
        assert cur_level_sequence in expected_level_sequences
        expected_level_sequences.remove(cur_level_sequence)
        count_trees += 1
    assert count_trees == 10

def test_8_5():
    """
    there are 108 unordered rooted trees
    with exactly 8 nodes and up to 5 leaves
    """
    count_trees = 0
    expected_count = 108
    for _ in tree_gen(8,1,5):
        count_trees += 1
    assert count_trees == expected_count

def test_8_3():
    """
    there are 48 unordered rooted trees
    with exactly 8 nodes and up to 3 leaves
    """
    count_trees = 0
    # 35 is the 8'th entry of OEIS A055278
    # the second term is for exactly 2 vertices as in two_leaf property test (12 in this case)
    # and 1 for the 1 leaf case
    expected_count = 35+sum((p-1)//2 for p in range(3,8+1))+1
    for _ in tree_gen(8,1,3):
        count_trees += 1
    assert count_trees == expected_count


def test_30_3():
    """
    there are 13661 unordered rooted trees
    with exactly 30 nodes and up to 3 leaves
    """
    count_trees = 0
    # 13450 is the 30'th entry of OEIS A055278
    # the second term is for exactly 2 vertices as in two_leaf property test
    # and 1 for the 1 leaf case
    expected_count = 13450+sum((p-1)//2 for p in range(3,30+1))+1
    for _ in tree_gen(30,1,3):
        count_trees += 1
    assert count_trees == expected_count
