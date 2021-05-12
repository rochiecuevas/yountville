# import modules
import sqlite3
from sqlite3 import Error

# create a function that creates a connection to a sqlite3 database

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    
    return conn
            
# create functions that creates tables using SQL statements

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print ("Table created successfully.")
    except Error as e:
        print(e)
        
def main():
    database = r"/Users/rochiecuevas/Documents/Data_side_projects/Yountville2/buildings.db"
    
    sql_create_equipment_table = """CREATE TABLE IF NOT EXISTS equipment (
                                  id integer PRIMARY KEY,
                                  Equipment_ID integer NOT NULL,
                                  Equipment_Name text NOT NULL,
                                  Part text,
                                  Make text,
                                  Make_Date text,
                                  Catalogue_No text,
                                  Frame text,
                                  Model_No text,
                                  Serial_No text,
                                  ID_No text,
                                  Power_hp integer,
                                  Voltage_V text,
                                  Current_amp text,
                                  RPM integer,
                                  Frequency_hz integer,
                                  PH integer,
                                  HD_FT text,
                                  CAP_GPM text,
                                  Date_installed text,
                                  Remarks text,
                                  FOREIGN KEY (Building_ID) REFERENCES buildings(Building_ID)
                                  );"""
    
    sql_create_staff_table = """CREATE TABLE IF NOT EXISTS staff (
                            id integer PRIMARY KEY,
                            Staff_ID integer,
                            Last_Name text NOT NULL,
                            Initials text,
                            Position text
                            );"""
    
    sql_create_buildings_table = """CREATE TABLE IF NOT EXISTS buildings (
                                 id integer PRIMARY KEY,
                                 Building_ID integer NOT NULL,
                                 Building_Name text,
                                 Section text,
                                 Room text
                                 );"""
    
    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        print ("Opened database successfully.")

        # (1) create stationary engineers table
        create_table(conn, sql_create_staff_table)

        # (2) create buildings table
        create_table(conn, sql_create_buildings_table)

        # (3) create equipment table
        create_table(conn, sql_create_equipment_table)

    else:
        print("Error! Cannot create the database connection.")


if __name__ == "__main__":
    main()