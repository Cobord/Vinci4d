"""
small examples
"""

from tree_enumeration import beyer_hedetniemi, tree_gen

def test_1_1():
    """
    there are the explicitly described 1 unordered rooted trees
    with exactly 1 nodes and exactly 1 leaves
    """
    count_trees = 0
    expected_level_sequences = [
        [0],
    ]
    for cur_tree in tree_gen(1,1,1):
        assert cur_tree.num_nodes == 1
        assert cur_tree.num_leaves == 1
        cur_level_sequence = cur_tree.level_sequence()
        assert cur_level_sequence in expected_level_sequences
        expected_level_sequences.remove(cur_level_sequence)
        count_trees += 1
    assert count_trees == 1

def test_2_1():
    """
    there are the explicitly described 1 unordered rooted trees
    with exactly 2 nodes and exactly 1 leaves
    """
    count_trees = 0
    expected_level_sequences = [
        [0,1],
    ]
    for cur_tree in tree_gen(2,1,1):
        assert cur_tree.num_nodes == 2
        assert cur_tree.num_leaves == 1
        cur_level_sequence = cur_tree.level_sequence()
        assert cur_level_sequence in expected_level_sequences
        expected_level_sequences.remove(cur_level_sequence)
        count_trees += 1
    assert count_trees == 1

def test_3_1():
    """
    there are the explicitly described 1 unordered rooted trees
    with exactly 3 nodes and exactly 1 leaves
    """
    count_trees = 0
    expected_level_sequences = [
        [0,1,2],
    ]
    for cur_tree in tree_gen(3,1,1):
        assert cur_tree.num_nodes == 3
        assert cur_tree.num_leaves == 1
        cur_level_sequence = cur_tree.level_sequence()
        assert cur_level_sequence in expected_level_sequences
        expected_level_sequences.remove(cur_level_sequence)
        count_trees += 1
    assert count_trees == 1

def test_3_2():
    """
    there are the explicitly described 1 unordered rooted trees
    with exactly 3 nodes and exactly 2 leaves
    """
    count_trees = 0
    expected_level_sequences = [
        [0,1,1],
    ]
    for cur_tree in tree_gen(3,2,2):
        assert cur_tree.num_nodes == 3
        assert cur_tree.num_leaves == 2
        cur_level_sequence = cur_tree.level_sequence()
        assert cur_level_sequence in expected_level_sequences
        expected_level_sequences.remove(cur_level_sequence)
        count_trees += 1
    assert count_trees == 1

#pylint:disable=duplicate-code
def test_5_1():
    """
    there are the explicitly described 1 unordered rooted trees
    with exactly 5 nodes and exactly 1 leaves
    """
    count_trees = 0
    expected_level_sequences = [
        [0,1,2,3,4],
    ]
    for cur_tree in tree_gen(5,1,1):
        assert cur_tree.num_nodes == 5
        assert cur_tree.num_leaves == 1
        cur_level_sequence = cur_tree.level_sequence()
        assert cur_level_sequence in expected_level_sequences
        expected_level_sequences.remove(cur_level_sequence)
        count_trees += 1
    assert count_trees == 1

#pylint:disable=duplicate-code
def test_5_2():
    """
    there are the explicitly described 3 unordered rooted trees
    with exactly 5 nodes and exactly 2 leaves
    """
    count_trees = 0
    expected_level_sequences = [
        [0,1,2,3,3],
        [0,1,2,3,2],
        [0,1,2,3,1],
        [0,1,2,1,2],
    ]
    for cur_tree in tree_gen(5,2,2):
        assert cur_tree.num_nodes == 5
        assert cur_tree.num_leaves == 2
        cur_level_sequence = cur_tree.level_sequence()
        assert cur_level_sequence in expected_level_sequences
        expected_level_sequences.remove(cur_level_sequence)
        count_trees += 1
    assert count_trees == 4

#pylint:disable=duplicate-code
def test_5_3():
    """
    there are the explicitly described 3 unordered rooted trees
    with exactly 5 nodes and exactly 3 leaves
    """
    count_trees = 0
    expected_level_sequences = [
        [0,1,2,2,2],
        [0,1,2,2,1],
        [0,1,2,1,1],
    ]
    for cur_tree in tree_gen(5,3,3):
        assert cur_tree.num_nodes == 5
        assert cur_tree.num_leaves == 3
        cur_level_sequence = cur_tree.level_sequence()
        assert cur_level_sequence in expected_level_sequences
        expected_level_sequences.remove(cur_level_sequence)
        count_trees += 1
    assert count_trees == 3

def test_5_4():
    """
    there are the explicitly described 1 unordered rooted trees
    with exactly 5 nodes and exactly 4 leaves
    """
    count_trees = 0
    expected_level_sequences = [
        [0,1,1,1,1],
    ]
    for cur_tree in tree_gen(5,4,4):
        assert cur_tree.num_nodes == 5
        assert cur_tree.num_leaves == 4
        cur_level_sequence = cur_tree.level_sequence()
        assert cur_level_sequence in expected_level_sequences
        expected_level_sequences.remove(cur_level_sequence)
        count_trees += 1
    assert count_trees == 1

def test_5_n():
    """
    there are the explicitly described 9 unordered rooted trees
    with exactly 5 nodes and up to 4 leaves
    """
    count_trees = 0
    expected_level_sequences = [
        [0,1,1,1,1],
        [0,1,2,2,2],
        [0,1,2,2,1],
        [0,1,2,1,1],
        [0,1,2,3,3],
        [0,1,2,3,2],
        [0,1,2,3,1],
        [0,1,2,1,2],
        [0,1,2,3,4],
    ]
    expected_count = len(expected_level_sequences)
    for cur_tree in tree_gen(5,1,4):
        assert cur_tree.num_nodes == 5
        assert 1 <= cur_tree.num_leaves <= 4
        cur_level_sequence = cur_tree.level_sequence()
        assert cur_level_sequence in expected_level_sequences
        expected_level_sequences.remove(cur_level_sequence)
        count_trees += 1
    assert count_trees == expected_count


def test_5_any():
    """
    there are the explicitly described 9 unordered rooted trees
    with exactly 5 nodes and any number of leaves
    """
    count_trees = 0
    expected_level_sequences = [
        [0,1,1,1,1],
        [0,1,2,2,2],
        [0,1,2,2,1],
        [0,1,2,1,1],
        [0,1,2,3,3],
        [0,1,2,3,2],
        [0,1,2,3,1],
        [0,1,2,1,2],
        [0,1,2,3,4],
    ]
    expected_count = len(expected_level_sequences)
    for cur_tree in tree_gen(5,0,100):
        assert cur_tree.num_nodes == 5
        assert 0 <= cur_tree.num_leaves <= 100
        cur_level_sequence = cur_tree.level_sequence()
        assert cur_level_sequence in expected_level_sequences
        expected_level_sequences.remove(cur_level_sequence)
        count_trees += 1
    assert count_trees == expected_count
    count_beyer = 0
    for _ in beyer_hedetniemi(5):
        count_beyer += 1
    assert count_beyer == expected_count

def test_n_3():
    """
    number of unordered unlabelled rooted trees
    with exactly 3 leaves on n nodes
    OEIS A055278
    """
    expected_counts = [0, 0, 0, 0, 1, 3, 8, 18, 35, 62, 103, 161, 241, 348, 487, 664, 886]
    for size,expected_count in enumerate(expected_counts):
        count_this_size = 0
        for cur_tree in tree_gen(size, 3,3):
            assert cur_tree.num_nodes == size
            assert cur_tree.num_leaves == 3
            count_this_size += 1
        assert count_this_size == expected_count
