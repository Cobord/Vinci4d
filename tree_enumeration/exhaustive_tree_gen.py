"""
generating ordered unlabelled trees
with a prescribed range of leaves
and restriction on children sizes and their level sequences
in order to make them canonical representatives of
the fiber of the forgetful map to unordered unlabelled trees
"""
from itertools import product
from typing import Generator, List, Optional, Tuple

from tree_enumeration.ordered_tree import OrderedTree

def tree_gen(num_nodes: int,
                    min_num_leaves: int,
                    max_num_leaves: int,
                    _top_level: bool = True) -> \
                        Generator[OrderedTree, None, None]:
    """
    generating ordered unlabelled trees
    with a prescribed range of leaves
    and restriction on children sizes and their level sequences
    in order to make them canonical representatives of
    the fiber of the forgetful map to unordered unlabelled trees
    """
    if num_nodes == 0:
        return
    if num_nodes == 1:
        if min_num_leaves <= 1 <= max_num_leaves:
            yield OrderedTree.degenerate()
        return
    if max_num_leaves <= 1:
        if min_num_leaves <= 1 <= max_num_leaves:
            yield OrderedTree.degenerate_path(num_nodes)
        return
    if _top_level:
        max_num_leaves = min(max_num_leaves, num_nodes-1)
        min_num_leaves = max(min_num_leaves, 1)
    for (node_sizes,leaf_sizes) in nodes_and_leaves_counts_for_children(
        num_nodes-1, min_num_leaves,max_num_leaves):
        generators_for_child_trees = (
            tree_gen(node_this_child,leaf_this_child,leaf_this_child, False)
                for (node_this_child,leaf_this_child) in zip(node_sizes,leaf_sizes)
        )
        for cur_children in product(*generators_for_child_trees):
            to_yield = OrderedTree(list(cur_children), False)
            if to_yield.good_representative():
                yield to_yield


def nodes_and_leaves_counts_for_children(
    num_nodes: int,
    min_num_leaves: int,
    max_num_leaves: int) -> Generator[Tuple[List[int],List[int]],None,None]:
    """
    divide num_nodes and num_leaves into parts
    node_sizes and leaf_sizes so that
    - len(node_sizes)=len(leaf_sizes)
    - sum(node_sizes)=num_nodes
    - min_num_leaves<=sum(leaf_sizes)<=max_num_leaves
    - with the exception of node_size = 1 and leaf_size = 1 when the root is a leaf too
        there should be at least one more (for at least the root) node than the number of leaves
        on each child
    """
    if num_nodes < min_num_leaves:
        return
    if num_nodes == min_num_leaves:
        yield ([1 for _ in range(num_nodes)], [1 for _ in range(num_nodes)])
        return
    max_num_children = min(num_nodes, max_num_leaves)
    for node_sizes in partitions(num_nodes, 1, 1, max_num_children):
        for leaf_count in range(max(min_num_leaves,len(node_sizes)), max_num_leaves+1):
            for leaf_sizes in leaf_partition(leaf_count,node_sizes):
                node_sizes.reverse()
                leaf_sizes.reverse()
                yield (node_sizes, leaf_sizes)
                node_sizes.reverse()

def partitions(n: int,
               min_part_size: int = 1,
               min_number_of_parts: Optional[int] = None,
               max_number_of_parts: Optional[int] = None) -> Generator[List[int],None,None]:
    """
    integer partitions
    possibly with
    - lower bound on part sizes
    - bounds on how many parts
    """
    if min_number_of_parts is None:
        min_number_of_parts = 1
    if max_number_of_parts is None:
        max_number_of_parts = n
    if min_number_of_parts>max_number_of_parts:
        return
    if min_number_of_parts<=1<=max_number_of_parts and n>=min_part_size:
        yield [n]
    for i in range(min_part_size, n//2 + 1):
        for p in partitions(n-i, i, min_number_of_parts-1, max_number_of_parts-1):
            yield [i] + p

def leaf_partition(n: int,
                   nodes_per_child: List[int],
                   which_child: int = 0) -> Generator[List[int],None,None]:
    """
    divide n into many parts
    with order mattering
    there are given number of nodes per part
    and so the number of leaves for that part must fit within that constraint
    
    we are trying to mimic taking slices with this strategy
    without copying over `nodes_per_child[which_child:]` as new `List[int]`
    """
    how_many_parts = len(nodes_per_child) - which_child
    if how_many_parts>n:
        return
    if how_many_parts == n:
        yield [1 for _ in range(how_many_parts)]
        return
    this_leaf_capacity = max(nodes_per_child[which_child]-1,1)
    if how_many_parts == 1:
        if n<=this_leaf_capacity:
            yield [n]
        return
    for part_0 in range(1,this_leaf_capacity+1):
        for rest in leaf_partition(n-part_0, nodes_per_child, which_child+1):
            yield [part_0] + rest
