# Import modules
import sqlite3
from sqlite3 import Error


# Connect to a database
conn = sqlite3.connect("buildings.db")
conn.row_factory = sqlite3.Row


# Run SQL queries
def sql_query(query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def sql_edit_insert(query, var):
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()
    
def sql_delete(query, var):
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()
    
def sql_query2(query, var):
    cur = conn.cursor()
    cur.execute(query, var)
    rows = cur.fetchall()
    return rows