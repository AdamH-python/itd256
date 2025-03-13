# Use the Index Luke: Loops
Joining combines fragments of data to suit a specific processing purpose.
Using the right index relies on which join algorithm you use.
All join algorithms can only process 2 tables at a time
To add more, it joins two and then joins another
The computer tries to find the fastest order.

## Nested Loops
The fundamental join algorithm

Like nested queries, there's an outer query that fetches results from one table and a secondary query for each row from the outer query.

Can be slower than just a big join, due to latencies.

Really easy to implement accidentally.

ORMs don't generate SQL joins but instead query one table with nested selects, known as the N+1 problem.

Even if a nested select performs the same index lookups it may still be slower due to increased network communication.

Generally, nested loops joins are easy and are good for small result sets but otherwise you should use a different join algorithm.