```markdown
# Python and MySQL

## Why Python Programming is Awesome

Python is a high-level, interpreted programming language known for its readability and versatility. It has a simple syntax that emphasizes readability and reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse.

```python
print("Hello, World!")
```

## Connecting to a MySQL Database from a Python Script

You can use the `mysql-connector-python` module to connect to a MySQL database:

```python
import mysql.connector

cnx = mysql.connector.connect(user='<username>', password='<password>',
                              host='<hostname>',
                              database='<database>')
cnx.close()
```

## SELECT Rows in a MySQL Table from a Python Script

You can execute a `SELECT` statement and fetch the results:

```python
cursor = cnx.cursor()
query = ("SELECT * FROM employees")
cursor.execute(query)

for row in cursor:
  print(row)

cursor.close()
```

## INSERT Rows in a MySQL Table from a Python Script

You can execute an `INSERT` statement to add data:

```python
cursor = cnx.cursor()
query = ("INSERT INTO employees (first_name, last_name) VALUES (%s, %s)")
data = ('John', 'Doe')
cursor.execute(query, data)

cnx.commit()
cursor.close()
```

## What ORM Means

ORM stands for Object-Relational Mapping. It's a technique that lets you interact with your database, like you would with SQL. In other words, it's a way to create, retrieve, update, and delete from your database using an object-oriented paradigm.

## Mapping a Python Class to a MySQL Table

With an ORM like SQLAlchemy, you can map a Python class to a MySQL table:

```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

engine = create_engine('mysql+mysqlconnector://<username>:<password>@<hostname>/<database>', echo=True)

Base.metadata.create_all(engine)
```

## Creating a Python Virtual Environment

A virtual environment is a way to keep the dependencies required by different projects separate:

```bash
python3 -m venv myenv
source myenv/bin/activate
```

## What is MySQLdb

MySQLdb is an interface for connecting to a MySQL database server from Python. It implements the Python Database API v2.0 and is built on top of the MySQL C API.

## What is SQLAlchemy

SQLAlchemy is a SQL toolkit and ORM that gives application developers the full power and flexibility of SQL. It provides a full suite of well known enterprise-level persistence patterns.
```
