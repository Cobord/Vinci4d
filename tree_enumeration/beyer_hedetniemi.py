"""
Beyer-Hedetniemi Algorithm
"""

from copy import copy
from typing import Callable, List, Optional

def last_not_level_one(level_sequence: List[int]) -> Optional[int]:
    """
    Look for index with value which is not 1
    because this is a level sequence by assumption level_sequence[0] = 0
    """
    p = len(level_sequence) - 1
    while level_sequence[p] == 1:
        if p == 0:
            break
        p -= 1
    if p == 0:
        return None
    return p

def next_rooted_tree(previous_level_sequence: List[int]):
    """
    One iteration to produce the next level sequence
    of another canonical tree with the same node count
    """

    p = last_not_level_one(previous_level_sequence)
    if p is None:
        return None

    q = p - 1
    while previous_level_sequence[q] != previous_level_sequence[p] - 1:
        q -= 1
    next_level_sequence = copy(previous_level_sequence)
    for i in range(p, len(next_level_sequence)):
        next_level_sequence[i] = next_level_sequence[i - p + q]
    return next_level_sequence

def beyer_hedetniemi(how_many_vertices: int,
                     level_sequence_filter: Optional[Callable[[List[int]],bool]] = None):
    """
    unlabelled unordered trees with `how_many_vertices`
    """
    if how_many_vertices == 0:
        return
    current_level_sequence = list(range(how_many_vertices))
    to_continue = True
    while to_continue:
        if level_sequence_filter is None or level_sequence_filter(current_level_sequence):
            yield current_level_sequence
        current_level_sequence = next_rooted_tree(current_level_sequence)
        if current_level_sequence is None:
            to_continue = False
