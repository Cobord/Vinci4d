# Enumeration of Trees

# Vocabulary

- Free: no root is chosen. It is just as an undirected graph with the restrictions that it has no cycles and is connected
- Rooted: A tree as normally presented with a root at top and children branching down
- Ordered: A rooted tree where the children are ordered
- Labelled: If the tree has `n` nodes, then the nodes are uniquely labelled with `0` through `n-1` labels
- Level sequence: Let `T` be an unlabelled ordered rooted tree. Give it labels using the pre-order traversal. The level sequence is the list `L` such that `L[i]` is the depth of the node labelled `i`.
- Parent sequence: Let `T` be an unlabelled ordered rooted tree. Give it labels using the pre-order traversal. The parent sequence is the list `P` such that `P[i]` is the label of the parent of the node labelled `i` with the parent of the root being `None`.

Given an unordered tree we can forget the ordering and get an unordered tree. Call this map `f`. Given an unordered tree we have many such ordered representatives which forget to that unordered tree. The preimage of any given unordered tree `f^{-1}(u)` is a set of multiple ordered trees related by repeatedly re-ordering children or children of a descendent.

When we have a system for choosing one representative from among these pre-images in a systematic way, that is called a canonical tree.


# Free Labelled Trees

This is the version with the oldest history going back to Cayley. There are `(n+1)^(n-1)` such trees if there are `n+1` vertices.
These are in explicit bijection functions with Prufer sequences, parking functions (see algebraic combinatorics and representation theory literature) among many others.

# Beyer-Hedetniemi Algorithm

This generates level sequences for canonical trees each representing a single distinct unordered unlabelled rooted tree with a prescribed number of nodes. Translating from level sequences back to canonical trees (`from_level_sequence` in `OrderedTree`) is straightforward if necessary. Forgetting the ordering of the children/grandchildren among their siblings is also immediate though an ordered representative is better for displaying.

## Problem

The restiction of leaves means we are exploring many possibilities that have too many leaves. It is constant amortized time for generation of trees without this restriction. But if the leaf restriction is drastic such as `N=30` `M=3` there are far too many operations spent on the trees which have more than `3` leaves. Therefore it is not constant amortized when dividing by the number of trees which are actually yielded. Those trees need to fullfill the condition on leaves as compared to considering all unordered unlabelled rooted trees. Without this restriction it is producing the `30`th entry of `OEIS A000081` which is far greater than the sum of the `30`th entry of `OEIS A055278` which accounts for exactly `3` leaves and the counts for exactly `1` and `2` leaves.

# Top Down Approach

Instead we proceed by dividing up the prescribed number of nodes and range of leaves among an arbitrary number of children. For example if we are told `N=30` nodes and `M=3`, then we have `29` non-root nodes to divide up into some number of children and each child gets some nonzero amount of those `3` leaves. The generator which accomplishes this task is a combination of an iterator over [Integer Partitions](https://en.wikipedia.org/wiki/Integer_partition) and ordered partitions using some constraints in each. Suppose the division was into 3 children using `lambda = [14,13,2]` for the node counts on each child tree and `1` leaf each. Then on the recursive call we are producing all canonical trees with exactly those node counts and leaf counts in order to place them as each of the three children. Again they are produced with generators so the trees are all emitted as soon as they are constructed.

There is repeated work with enumerating the trees on the same constraints at different places for example if we there were two children with `40` nodes and `17` leaves and `60` nodes and `23` leaves on the other. Then some descendant of the later examined the same case of `40` nodes and `17` leaves with the remaining `20` and `6` among the ancestors, siblings, cousins etc. This list of trees is recomputed which indicates area for performance left on the table.

## Concerns

This works better than the previous algorithm when we are constraining the number of leaves to be small and growing much slower than `n`. However, if we consider a different regime where we scale the number of leaves slightly faster, there is a crossover to where this mechanism does not become effective as doing Beyer-Hedetniemi with a filter. At some point the faster production of trees accomplished by this algorithm and the filtering only removing a few cases rather than the overwhelming majority, means that Beyer-Hedetniemi is more effective in that regime. The examples given in the specification indicate that is not the regime of interest.

Consider the extreme examples.

If `M=1` is fixed and `N` grows then we prefer the approach that has the leaf restriction built in because we immediately yield the straight line path tree and nothing else. This contrasts with filtering all but `1` out if we produced all the trees and then checked for only `1` leaf.

If `M=N` as `N` grows then we are putting no extra restriction on the number of leaves beyond what is implied by the node count. In that case the filter does not remove anything and the constant amortized time per tree of Beyer-Hedetniemi holds up.

We could make an ansatz of `M=N^\alpha` with `\alpha` in between these above `0` and `1` extremes to look for a crossover.

# How to Use

## Small Leaf Constraints

In this regime use `tree_gen` with `3` arguments. The first is the value of `N` for the number of nodes. The second is `1` for the lower bound on the number of leaves. The third is `M` for the upper bound on the number of leaves.

## Minimal Constraints on Leaves

In this regime when you aren't constraining how many leaves beyond much more than what is constrained by the number of nodes, use `beyer_hedetniemi` with `2` arguments. The first is the value of `N` for the number of nodes. The second is a filter function which takes the level sequence and returns whether or not to filter out the associated tree. This latter argument is optional and defaults to doing no such filtering.