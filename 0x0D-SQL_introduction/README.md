# Database Basics and MySQL Usage

## What's a Database?

A database is a structured collection of data organized in a way that facilitates efficient retrieval and management of information. It serves as a centralized repository for storing, managing, and retrieving data.

## What's a Relational Database?

A relational database is a type of database that organizes data into tables with rows and columns. These tables are related to each other based on common attributes, establishing relationships between different pieces of information.

## What Does SQL Stand For?

SQL stands for Structured Query Language. It is a domain-specific language used to manage and manipulate relational databases. SQL allows users to interact with databases by querying, updating, and managing data.

## What's MySQL?

MySQL is an open-source relational database management system (RDBMS) that uses SQL. It is widely used for building scalable and secure database-driven applications. MySQL is known for its speed, reliability, and ease of use.

## How to Create a Database in MySQL

To create a database in MySQL, you can use the following SQL command:

```sql
CREATE DATABASE dbname;
```

Replace "dbname" with the desired name of your database.

## What Does DDL and DML Stand For?

- **DDL:** Data Definition Language. It deals with the structure of the database, including creating, altering, and deleting tables and schemas.
  
- **DML:** Data Manipulation Language. It deals with the manipulation of data stored in the database, such as inserting, updating, and deleting records.

## How to CREATE or ALTER a Table

To create a table, you can use the following SQL command:

```sql
CREATE TABLE tablename (
  column1 datatype,
  column2 datatype,
  ...
);
```

To alter a table, you can use the ALTER TABLE statement:

```sql
ALTER TABLE tablename
ADD COLUMN newcolumn datatype;
```

## How to SELECT Data from a Table

To retrieve data from a table, you can use the SELECT statement:

```sql
SELECT column1, column2
FROM tablename
WHERE condition;
```

## How to INSERT, UPDATE, or DELETE Data

- **INSERT:**
```sql
INSERT INTO tablename (column1, column2, ...)
VALUES (value1, value2, ...);
```

- **UPDATE:**
```sql
UPDATE tablename
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

- **DELETE:**
```sql
DELETE FROM tablename
WHERE condition;
```

## What Are Subqueries?

Subqueries are queries nested within other queries. They can be used to retrieve data that will be used in the main query as a condition.

Example:
```sql
SELECT column1
FROM tablename
WHERE column2 IN (SELECT column2 FROM anothertable WHERE condition);
```

## How to Use MySQL Functions

MySQL provides a variety of functions for tasks like mathematical operations, string manipulation, and date/time calculations. Example:

```sql
SELECT AVG(column1) AS average_value
FROM tablename;
```

This calculates the average value of 'column1' in the specified table.

Remember to refer to the [MySQL documentation](https://dev.mysql.com/doc/) for more in-depth information on MySQL and SQL syntax.
