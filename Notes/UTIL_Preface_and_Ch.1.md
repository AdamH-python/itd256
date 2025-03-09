# Use the Index Luke: Preface and Chapter 1 Notes
Adam Hellinga
## Preface
SQL seperates the where and the how, making it easier to find data, but its not perfect.

## Chapter 1
### Index Leaf Nodes
Insert statements screw up the indexes and are slow, so find a way to order them that isn't impacted by insert statements.

The logical order is a double linked list
- every node, or entry, has a link to the entry before and after it.
- It can be easily added to by just updating two of the links to reference the new entry.
### The B-Tree
Index leaf nodes are in an arbitrary order, like a shuffled phone book.

To find an entry among this shuffled phone book, it needs a secondary structure, a balanced search tree or B-Tree.

Like a lead node that reffers to a bunch of leaf nodes.
- Each value in a branch node corresponds to the largest value in the leaf node section it reffers to.
### Slow Indexes, pt. 1
Many people think that these indexes can be slower than the standard select, which can be true in some scenarios.
- If you have a long tree of references between nodes, it will be slow.

It takes three steps which can each be slow
1. The tree traversal (finding the nodes with the right data)
2. Following the leaf node chain (in case the referenced node in the tree doesn't cover all the possibilities)
3. Fetching data from the table

There are a few ways that a database may follow this path.

#### Index Unique Scan
If the constraint only appears once, they only have to look down the branches and not down the links.

#### Index Range Scan
If there might be multiple that may fall under the constraint, it will look down the tree and the chain.

#### Table Access by Index ROWID

Retrieves the data from the table, and is often performed after an Index Scan.

Index Range Scans are common and can often take a long time, as often times 100's of pieces can follow a constraint.