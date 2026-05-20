from db import connect

conn = connect()
cur = conn.cursor()
conn.autocommit = True

cur.execute(
    # "CREATE DATABASE library"
    # """CREATE TABLE authors(
    # id SERIAL PRIMARY KEY,
    # name VARCHAR(140)
    # )"""
    # """CREATE TABLE books(
    # id SERIAL PRIMARY KEY,
    # title VARCHAR(100),
    # page INT
    # )"""
    # "INSERT INTO authors(name) VALUES('Shekspir'),('A.Navoiy'),('X.Toxtaboyev'),('A.Qahhor')"
    # "INSERT INTO books(title,page) VALUES('Qirol RIL',80),('Farhod va shirin',320),('Sariq devni minib',200)"
    "SELECT authors.name , books.title,books.page FROM authors LEFT JOIN books ON authors.id = books.id"
)

rows = cur.fetchall()
for row in rows:
    print(row)