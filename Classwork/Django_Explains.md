# Using Django to create different types of querys
Adam Hellinga

Here is the django documentation, sql queries that it runs, and the diagram of how it is executed.
## Sequential Scan
Django Documentation:
```
Inventory.objects.all.count()
```
SQL Documentation:
```
SELECT COUNT(*) AS "__count" FROM "db_inventory"
```
Diagram:

<img src="/Users/1010947/Desktop/itd256/Other/Sequential_Scan.png" alt="The image did not load">

Reflection:
- I believe that this query used a sequential scan, as the index does not provide information that would make this query any faster.

## Index Scan
Django Documentation:
```
Order.objects.filter(id=15).values_list("customer_id")
```
SQL Documentation:
```
SELECT "db_order"."customer_id" FROM "db_order" WHERE "db_order"."id" = 15 LIMIT 21
```
Diagram:

<img src="/Users/1010947/Desktop/itd256/Other/Index_Scan.png" alt="The image did not load">

Reflection:
- I believe that this used an index query because the index helps idenify which rows follow the constraint, but does not provide information on what to return, so it must access the table.

## Index Only Scan
Django Documentation:
```
Order.objects.filter(id = 14).count()
```
SQL Documentation:
```
SELECT COUNT(*) AS "__count" FROM "db_order" WHERE "db_order"."id" = 14
```
Diagram:

<img src="/Users/1010947/Desktop/itd256/Other/Index_Only_Scan.png" alt="The image did not load">

Reflection:
- I believe that this query used an index only scan because the constraints can be filtered using the index, and all the information requested can be found with just the index, so accessing the table is not needed.