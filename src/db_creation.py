from psycopg2 import *
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from src.environment import *

if __name__ == "__main__":
    con = connect(f"user={DATABASE_USER} password='{DATABASE_PASSWORD}' host={DATABASE_HOST}")
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = con.cursor()

    print(f"DROP DATABASE IF EXISTS {DATABASE_NAME};")

    cursor.execute(f"DROP DATABASE IF EXISTS {DATABASE_NAME};")
    con.commit()

    print(f"CREATE DATABASE  {DATABASE_NAME};")
    cursor.execute(f"CREATE DATABASE  {DATABASE_NAME};")
    con.commit()
    con.close()

    print(f"APPLY SCHEMA ...")

    conn = connect(f"dbname={DATABASE_NAME} user={DATABASE_USER} password='{DATABASE_PASSWORD}' host={DATABASE_HOST}")
    sql_file = open('sql/etl_accident_db_creation.sql', 'r')
    conn.cursor().execute(sql_file.read())
    conn.commit()
    conn.close()

    print(f"END ...")
