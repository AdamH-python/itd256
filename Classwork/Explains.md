# Using Explain to find query plans in Postgresql
Adam Hellinga

## Sequential Scan
EXPLAIN SELECT * FROM employees LIMIT 5;

                                QUERY PLAN                                 
---------------------------------------------------------------------------
 Limit  (cost=0.00..0.76 rows=5 width=1029)
   ->  Seq Scan on employees  (cost=0.00..15286.00 rows=100000 width=1029)
(2 rows)

I believe that this query used a Sequential Scan because the index does not contain information that would make this faster, so it just scanned all the data.

## Index Scan
EXPLAIN SELECT * FROM employees WHERE employee_id = 99435;

                                   QUERY PLAN                                    
---------------------------------------------------------------------------------
 Index Scan using employees_pk on employees  (cost=0.29..8.31 rows=1 width=1029)
   Index Cond: (employee_id = '99435'::numeric)
(2 rows)

I believe that this query used Index Scan because it used a unique constraint so it didnt have to look sequentially, and it had to find information from the table other than the primary key so it was not an index only scan.

## Index Only Scan
EXPLAIN SELECT count(*) FROM employees WHERE (employee_id % 2) = 0;

                                          QUERY PLAN                                          
----------------------------------------------------------------------------------------------
 Aggregate  (cost=3110.54..3110.55 rows=1 width=8)
   ->  Index Only Scan using employees_pk on employees  (cost=0.29..3109.29 rows=500 width=0)
         Filter: ((employee_id % '2'::numeric) = '0'::numeric)

I believe that this query used an Index Only Scan because the information being found is in the index so it does not need to look at the table.