```markdown
# MySQL Basics

This repository provides a basic guide to essential MySQL concepts and commands. It covers the following topics:

1. **Creating a new MySQL user:**
   - Use the `CREATE USER` statement to create a new user with a specified username, host, and password.

   ```sql
   CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
   ```

2. **Managing privileges for a user:**
   - Grant privileges using the `GRANT` statement. Example for granting all privileges on a database:

   ```sql
   GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost';
   ```

3. **Primary Key:**
   - Understand the concept of a PRIMARY KEY, a unique identifier for each record in a table.

   ```sql
   CREATE TABLE example_table (
       id INT PRIMARY KEY,
       name VARCHAR(255)
   );
   ```

4. **Foreign Key:**
   - Learn about FOREIGN KEYs, which establish relationships between tables.

   ```sql
   CREATE TABLE orders (
       order_id INT PRIMARY KEY,
       product_id INT,
       FOREIGN KEY (product_id) REFERENCES products(product_id)
   );
   ```

5. **NOT NULL and UNIQUE constraints:**
   - Use constraints to enforce rules on column values.

   ```sql
   CREATE TABLE example_table (
       id INT PRIMARY KEY,
       name VARCHAR(255) NOT NULL,
       email VARCHAR(255) UNIQUE
   );
   ```

6. **Retrieving data from multiple tables:**
   - Use the `JOIN` clause to retrieve data from multiple tables based on related columns.

   ```sql
   SELECT * FROM orders
   JOIN products ON orders.product_id = products.product_id;
   ```

7. **Subqueries:**
   - Understand subqueries, which are nested queries used within other SQL statements.

   ```sql
   SELECT column_name
   FROM table_name
   WHERE column_name = (SELECT column_name FROM another_table WHERE condition);
   ```

8. **JOIN and UNION:**
   - Explore the use of JOINs to combine rows from multiple tables and UNION to combine result sets.

   ```sql
   -- JOIN example
   SELECT *
   FROM employees
   INNER JOIN departments ON employees.department_id = departments.department_id;

   -- UNION example
   SELECT column_name FROM table1
   UNION
   SELECT column_name FROM table2;
   ```

Feel free to explore each section and adapt the provided SQL examples to your specific use case.
```

This README.md file provides a brief overview of the MySQL basics covered in the repository and guides users on how to explore each topic.
