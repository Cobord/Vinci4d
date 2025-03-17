"""
timing on the N=30 example requested in the spec
note the much smaller time per tree using Beyer-Hedetneimi
but that requires no constraint on the number of leaves

the explicit inequalities in the time are taken from a 95%
level on 1.60 GHz Intel i5 ...
for same 95% on another device adjust accordingly

disabled as test -> tst so that GitHub actions can run pytest
without such probability of failure
alternative would be increasing the times, but that would be
less reflective of the actual amortized time per tree
that is typical in favor of the worst case tails of the random fluctuations
"""

import time

from tree_enumeration import beyer_hedetniemi
from tree_enumeration.exhaustive_tree_gen import tree_gen

def tst_perf_30_3():
    """
    timing on the N=30 example requested in the spec
    """
    # 13450 is the 30'th entry of OEIS A055278
    # the second term is for exactly 2 vertices as in two_leaf property test
    # and 1 for the 1 leaf case
    expected_count = 13450+sum((p-1)//2 for p in range(3,30+1))+1
    def perf_30_3():
        """
        there are 13661 unordered rooted trees
        with exactly 30 nodes and up to 3 leaves
        """
        count_trees = 0
        for cur_tree in tree_gen(30,1,3):
            assert cur_tree.num_nodes == 30
            assert 1 <= cur_tree.num_leaves <= 3
            count_trees += 1
        assert count_trees == expected_count
    tic = time.perf_counter_ns()
    perf_30_3()
    toc = time.perf_counter_ns()
    assert (toc - tic) / expected_count < 120_000

def tst_perf_14_any():
    """
    timing on the N=14 example with no constraint on leaves
    """
    expected_count = 32973
    def perf_14_any():
        """
        there are 32973 unordered rooted trees
        with exactly 14 nodes
        """
        count_trees = 0
        for cur_tree in beyer_hedetniemi(14):
            assert len(cur_tree) == 14
            count_trees += 1
        assert count_trees == expected_count
    tic = time.perf_counter_ns()
    perf_14_any()
    toc = time.perf_counter_ns()
    assert (toc - tic) / expected_count < 2_000
