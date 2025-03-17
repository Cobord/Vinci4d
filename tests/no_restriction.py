"""
when the restriction on number of leaves is trivially satisfied
the Beyer-Hedetniemi method which does not account for leaf counts
at all should match with same produced trees

the fact that we are confident of no repeats among the same equivalence
class of ordered unlabelled rooted trees representing the same unordered version
when generating them via Beyer-Hedetniemi and that `tree_gen` is giving those same
numbers when given wide bounds on leaf counts lends evidence that there is no
double counting within the same fiber of the forgetful map
"""

from typing import List, Set, Tuple
from hypothesis import given, strategies as st

from tree_enumeration import beyer_hedetniemi, tree_gen

@given(st.integers(0,6))
def test_no_leaf_restriction_small(input_size: int):
    """
    when the restriction on number of leaves is trivially satisfied
    the Beyer-Hedetniemi method which does not account for leaf counts
    at all should match with same produced trees
    in these cases all the choices of ordered representatives for unordered trees
    match
    """
    count_trees_restricted = 0
    level_sequences_restricted : Set[Tuple[int]] = set()
    for cur_tree in tree_gen(input_size,1,input_size):
        count_trees_restricted += 1
        assert cur_tree.num_nodes == input_size
        assert 1 <= cur_tree.num_leaves <= input_size
        level_sequences_restricted.add(tuple(cur_tree.level_sequence()))
    count_trees_unrestricted = 0
    level_sequences_unrestricted : Set[Tuple[int]] = set()
    for cur_level_sequence in beyer_hedetniemi(input_size):
        count_trees_unrestricted += 1
        level_sequences_unrestricted.add(tuple(cur_level_sequence))
    assert level_sequences_restricted == level_sequences_unrestricted
    assert count_trees_restricted == count_trees_unrestricted

@given(st.integers(7,11))
def test_no_leaf_restriction(input_size: int):
    """
    when the restriction on number of leaves is trivially satisfied
    the Beyer-Hedetniemi method which does not account for leaf counts
    at all should match with same produced trees
    """
    count_trees_restricted = 0
    level_sequences_restricted : Set[Tuple[int]] = set()
    for cur_tree in tree_gen(input_size,1,input_size):
        assert cur_tree.num_nodes == input_size
        assert 1 <= cur_tree.num_leaves <= input_size
        count_trees_restricted += 1
        cur_level_sequence = cur_tree.level_sequence()
        if tuple(cur_level_sequence) in level_sequences_restricted:
            assert False, f"{cur_level_sequence}"
        level_sequences_restricted.add(tuple(cur_level_sequence))
    assert len(level_sequences_restricted) == count_trees_restricted
    count_trees_unrestricted = 0
    level_sequences_unrestricted : Set[Tuple[int]] = set()
    for cur_level_sequence in beyer_hedetniemi(input_size):
        count_trees_unrestricted += 1
        level_sequences_unrestricted.add(tuple(cur_level_sequence))
    assert len(level_sequences_unrestricted) == count_trees_unrestricted
    assert count_trees_restricted == count_trees_unrestricted,\
        f"{level_sequences_restricted.symmetric_difference(level_sequences_unrestricted)}"

def test_small_beyer_hedetniemi():
    """
    Beyer-Hedetniemi on small examples
    """
    for cur_tree in beyer_hedetniemi(1):
        assert cur_tree == [0]
    for cur_tree in beyer_hedetniemi(2):
        assert cur_tree == [0,1]
    count_3 = 0
    for cur_tree in beyer_hedetniemi(3):
        assert cur_tree in [[0,1,2],[0,1,1]]
        count_3 += 1
    assert count_3 == 2
    count_4 = 0
    expected_level_sequences = [
        [0,1,2,3],
        [0,1,2,2],
        [0,1,2,1],
        [0,1,1,1]
    ]
    for cur_tree in beyer_hedetniemi(4):
        assert cur_tree in expected_level_sequences
        expected_level_sequences.remove(cur_tree)
        count_4 += 1
    assert count_4 == 4
    # copied from OEIS A000081
    expected_counts = [0, 1, 1, 2, 4, 9, 20, 48, 115, 286, 719,
                       1842, 4766, 12486, 32973, 87811, 235381]
    for size,expected_count in enumerate(expected_counts):
        count_this_size = 0
        for cur_tree in beyer_hedetniemi(size):
            count_this_size += 1
        assert count_this_size == expected_count

@given(st.integers(0,14))
def test_some_leaf_restriction(input_size: int):
    """
    use the filter argument
    in particular only exclude the trees which are the form of a root
    and then all leaves directly attached to the root
    """
    no_restriction_counts = [0, 1, 1, 2, 4, 9, 20, 48, 115, 286, 719,
                       1842, 4766, 12486, 32973]
    no_restriction_count = no_restriction_counts[input_size]
    count_this_size = 0
    for _ in beyer_hedetniemi(input_size, lambda _: True):
        count_this_size += 1
    assert count_this_size == no_restriction_count

    def exclude_all_level_one(level_sequence: List[int]) -> bool:
        return any(z > 1 for z in level_sequence)
    if no_restriction_count > 0:
        no_restriction_count = no_restriction_count - 1
    count_this_size = 0
    for _ in beyer_hedetniemi(input_size,
                              exclude_all_level_one):
        count_this_size += 1
    assert count_this_size == no_restriction_count
