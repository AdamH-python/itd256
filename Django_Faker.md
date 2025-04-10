# Using Django and Faker
We used Faker and Django to convert our ite140 final project into an orm through Django, and used Faker to fill it with fake data.

## Creating Tables
In Django, tables are made similarly to objects in Python

[here is the file where all the tables are created](https://github.com/AdamH-python/orm/blob/main/db/models.py)
## ER Diagrams

### Manually Created ER Diagram
<img src="/Users/1010947/Desktop/itd256/Other/COSTCO.png" alt="The image did not load">

### pgAdmin Generated ER Diagram
<img src="/Users/1010947/Desktop/itd256/Other/Django_ER_Diagram.png" alt="The image did not load">

## Comparison
While the core tables of both diagrams are the same, there are some differences.

The differences I found include that the automatically generated diagram includes the schema with each table, while the manual one does not, this is due to the generated diagram including all tables in the database, while the manually created ER diagram only shows one schema.

The two tables are extremely similar, both use almost the same crows foot notation, the only difference is that the manually generated ER diagram specifies whether a value has to have at least one, or if there can be no connection.

If I were to do a similar project in the future, I would use django, as I find it more intuitive. It is also easier to fill with data, as you can use for loops easier than the fake data for postgresql.
