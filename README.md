# part-ll-avl-morphing-dict
Python module implementing a partitioned linked-list/AVL-tree morphing dictionary, i.e. a data structure that manages
key-value  pairs where the keys are integers partitioned into a fixed number of blocks, each one associated with a
linked list or an AVL tree depending on its size.
First essay paper of Algorithm Engineering course.

## Requirements

Given the following parameters in the set of integers $\mathbb{Z}$:

- $min$ and $max$ such that $max > min$
- $r = 6$
- $b > r$ such that $\left( max - min \right)$ is a multiple of $b$

Let's define $d = \left| \frac{max - min}{b} \right|$ and the set
$B_i = \left\\{ n \in \mathbb{Z} : min + i \cdot b \leq n < min + \left( i + 1 \right) \cdot b \right\\}$
with $i \in \left\\{0, \ldots, d - 1 \right\\}$, $B_d = \left\\{ n \in \mathbb{Z} : n < min \right\\}$
and $B_{d + 1} = \left\\{ n \in \mathbb{Z} : n \geq max \right\\}$.

From the previous definitions it can be seen that
$\bigcup\nolimits_{i=0}^{d+1} B_i = \mathbb{Z}$ and
$B_i \cap B_j = \emptyset \quad \forall i,j \in \left\\{1, \ldots, d + 1\right\\}$ with $i \ne j$,
therefore $\left\\{ B_i \right\\}_{i = 0}^{d + 1}$ forms a partition of $\mathbb{Z}$.

Implement a data structure that manages pairs of type $\left(key, value\right)$
(for simplicity $key \in \mathbb{Z}$) with the following characteristics:
- an array $v$ of size $d + 2$ where each cell is indexed by $i \in \left\\{ 0, \ldots, d + 1\right\\}$
and points to a known data structure (linked list or AVL tree) with $n_i$ elements
  - $v\left[ i \right]$ points to a linked list $\Leftrightarrow n_i < r$
  - $v\left[ i \right]$ points to an AVL tree $\Leftrightarrow n_i \ge r$
- implements the `insert(key, value)`, `delete(key)`, `search(key)` methods of the `Dictionary` abstract 
class
  - operations are performed on the data structure pointed to by
$v\left[ i \right] \Leftrightarrow key \in B_i$ with $i \in \left\\{ 0, \ldots, d + 1 \right\\}$

**N.B.**: the `insert` and `delete` operations modify the number $n_i$ of elements present in the data
structure pointed by $v\left[ i \right]$.
The data structure, where necessary, must be changed accordingly.
For example, if in the linked list pointed by $v\left[ 1 \right]$ there are $5$ elements ($n_1 < r$)
and one more is added, $n_1$ is then greater than or equal to $r$ and the list is transformed into an
AVL tree with the same elements.
Now $v\left[ 1 \right]$ will point to the tree and no longer to the linked list.
If instead from the tree of $v\left[ 1 \right]$ we remove an element we arrive at $n_1 = 5$ and the tree
is transformed into a linked list.

Finally, experimentally compare the average execution time of the methods `search` and `delete` of the
previously described data structure and of the Python `dictionary` with respect to the number $n$ of
elements.
