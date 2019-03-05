# moonfrog labs:
- line increase and then decrease, find the point at which it decreases 
    solution: modified binary search
- chocolate bars. cost of merging = sum(height_bar_1 + height_bar_2).
    find the minimum cost of merging all chocolate bars into a single bar.
    solution: at each stage find smallest two chocolates using min-heap and merge them

# myntra:
- identify minimum number of swaps to get to the original sorted order
- given a lattice represented in the form of matrix where 0: does not conduct, 1: conducts
    Lattice 1                   Lattice 2
    0 0 1 0 <- top              0 1 0 0 0 <- top
    0 1 1 0                     0 1 1 1 0
    0 0 0 1                     0 0 0 1 0
    0 0 1 0 <- bottom           0 0 0 1 0 <- bottom
    (Does not conduct)          (Conducts)
    Find whether the lattice conducts electricity from top to bottom layer (only up, left, down and right are connected neighbors. diagonal neighbors are not connected)
    solution: disjoint set
- given emp_id, rating, mgr_id (hierarchy) find the x% of employees at each level for  
    distributing bonuses. x is changeable again and again.
- print all nodes at `d` distance from the given node in a binary tree
    solution: stack
- for a stream of numbers return the first unique number with every update
    solution: deque + hash_map