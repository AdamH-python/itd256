# Use the Index Luke: Case Insensitive Search Using UPPER and LOWER
Adam Hellinga

using UPPER() and LOWER() operations allows you to ignore the case of what you are looking for.

it ends up doing a full table scan if you ask for it to search with the UPPER or LOWER clauses as its not looking for something like last_name, but instead UPPER(last_name).

To actually query an index instead of a full table scan, you need to make an index with UPPER(last_name).
- an index like this that uses a function or expression is called a function-based index