
#Q1. What is a database? Differentiate between SQL and NoSQL databases.
Ans:A database is a collection of data that is organized in a way that allows for efficient storage, retrieval, and management of that data. There are two main types of databases: SQL and NoSQL.
SQL databases, also known as relational databases, store data in tables that are related to one another through a common key. SQL databases use a structured query language (SQL) to interact with the data. Examples of SQL databases include MySQL, PostgreSQL, and Oracle.
NoSQL databases, on the other hand, do not use tables to store data. Instead, they use a variety of data models, such as key-value, document, or graph. NoSQL databases are often used for storing and processing large amounts of unstructured data. Examples of NoSQL databases include MongoDB, Cassandra, and Couchbase.

#Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.
Ans:DDL stands for Data Definition Language. It is used to define the structure of a database, including the creation, modification, and deletion of tables and other database objects. Here are some examples of DDL commands:
CREATE: Used to create a new table or other database object. For example, the following SQL command creates a new table called "students" with three columns: id, name, and age.
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  age INT
);
DROP: Used to delete an existing table or other database object. For example, the following SQL command deletes the "students" table:
DROP TABLE students;
ALTER: Used to modify the structure of an existing table. For example, the following SQL command adds a new column called "email" to the "students" table:
ALTER TABLE students ADD COLUMN email VARCHAR(50);
TRUNCATE: Used to delete all data from a table. For example, the following SQL command removes all data from the "students" table:
TRUNCATE TABLE students;

#Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.
Ans:DML stands for Data Manipulation Language. It is used to manipulate the data in a database, including adding, modifying, and deleting data. Here are some examples of DML commands:
INSERT: Used to add new data to a table. For example, the following SQL command adds a new row to the "students" table:
INSERT INTO students (id, name, age) VALUES (1, 'John Doe', 20);
UPDATE: Used to modify existing data in a table. For example, the following SQL command changes the age of the student with id 1 to 21:
UPDATE students SET age = 21 WHERE id = 1;
DELETE: Used to remove data from a table. For example, the following SQL command removes the row from the "students" table where id is 1:
DELETE FROM students WHERE id = 1;

#Q4. What is DQL? Explain SELECT with an example.
Ans:DQL stands for Data Query Language. It is used to retrieve data from a database. The most commonly used DQL command is SELECT, which is used to retrieve data from one or more tables. Here is an example of the SELECT command:
SELECT name, age FROM students WHERE age > 20;
This command selects the name and age columns from the "students" table where the age is greater than 20.

#Q5. Explain Primary Key and Foreign Key.
Ans:In relational databases, a primary key is a column or a set of columns that uniquely identifies each row in a table. A primary key is used to ensure that each row in the table can be uniquely identified, and it is used as a reference point for other tables. In most cases, a primary key is a single column, and it is typically an auto-incrementing integer that is assigned to each new row.
A foreign key, on the other hand, is a column or a set of columns in one table that references the primary key of another table. The purpose of a foreign key is to create a relationship between two tables by linking a column in one table to a column in another table. This ensures data consistency and integrity between the two tables. When a foreign key is defined, it ensures that the value in the referencing column must match a value in the referenced primary key column.

#Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.
Ans:Here is an example Python code to connect to MySQL and execute a SELECT statement using the cursor() and execute() methods:
python

import mysql.connector

# connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="database_name"
)

# create a cursor object
mycursor = mydb.cursor()

# execute a SELECT statement
mycursor.execute("SELECT * FROM customers")

# fetch the results
myresult = mycursor.fetchall()

# print the results
for x in myresult:
  print(x)


The cursor() method creates a new cursor object that is used to execute SQL statements. 
The execute() method is used to execute a SQL statement on the database.
 In this example, the execute() method is used to execute a SELECT statement that retrieves
all rows from the "customers" table. The fetchall() method is 
 then used to fetch all the rows from the result set, and the for loop is used to print each row.

#Q7. Give the order of execution of SQL clauses in an SQL query.

In general, the order of execution of SQL clauses in a SQL query is as follows:

FROM - specifies the table or tables from which to retrieve data
WHERE - specifies the conditions that the data must meet to be included in the result set
GROUP BY - groups the data based on one or more columns
HAVING - filters the data based on the groups created by the GROUP BY clause
SELECT - selects the columns to include in the result set
ORDER BY - specifies the order in which to sort the result set
LIMIT - limits the number of rows returned by the query (optional)
However, the specific order can vary depending on the complexity of the query and the requirements of the database.



