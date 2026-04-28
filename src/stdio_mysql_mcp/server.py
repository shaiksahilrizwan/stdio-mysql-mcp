from fastmcp import FastMCP
import os 
from urllib.parse import urlparse
import mysql.connector
import sys

app=FastMCP("stdio-mysql-mcp")

try:
    url=urlparse(os.environ.get("MYSQL_URL"))
    if not url:
        print("Error: MYSQL_URL environment variable is missing.", file=sys.stderr)
        sys.exit(1)
    db_host = url.hostname
    db_user = url.username
    db_password = url.password
    db_port = url.port or 3306
    db_local=mysql.connector.connect(host=db_host,user=db_user,passwd=db_password,port=db_port)
    local_cursor=db_local.cursor(buffered=True)
except Exception as e:
    print({"status":"failed","message":f"Error {e}"})
    sys.exit(1)
@app.tool
def get_databases():
    """Retrieve a list of all available databases on the MySQL server."""
    try:
        local_cursor.execute("SHOW DATABASES")
        db_list=[]
        for db in local_cursor:
            db_list.append(db[0])
        return db_list
    except Exception as e:
        return {"status": "failed", "message": f"Error {e}"}

@app.tool
def get_tables_in_db(database:str):
    """Retrieve a list of all tables within a specified database."""
    try:
        local_cursor.execute(f"USE {database}")
        local_cursor.execute("SHOW TABLES")
        table_list=[]
        for table in local_cursor:
            table_list.append(table[0])
        return table_list
    except Exception as e:
        return {"status": "failed", "message": f"Error {e}"}

@app.tool
def get_records(database:str,table:str):
    """Retrieve all records and column names from a specific table in a given database."""
    try:
        local_cursor.execute(f"USE {database}")
        local_cursor.execute(f"SELECT * from {table}")
        records=[]
        for record in local_cursor:
            records.append(record)
        return {"column_names":local_cursor.column_names,"rows":records}
    except Exception as e:
        return {"status": "failed", "message": f"Error {e}"}

@app.tool
def get_specific_column_records(columns:list[str],table:str,database:str="student_tracker"):
    """Retrieve records for specific columns from a given table and from given database."""
    try:
        local_cursor.execute(f"USE {database}")
        cols_list=''
        if len(columns)==1:
             cols_list+=columns[-1]
        else:
            for i in range(len(columns)):
                if i==len(columns)-1:
                    cols_list+=columns[i]
                else:
                    cols_list+=columns[i]+","
        local_cursor.execute(f"SELECT {cols_list} FROM {table}")
        records=[]
        for record in local_cursor:
            records.append(record)
        return {"column_names":local_cursor.column_names,"rows":records}
    except Exception as e:
        return {"status": "failed", "message": f"Error {e}"}

@app.tool
def custom_sql_query(sql:str):
    """Execute a custom SQL query and return the resulting rows and column names."""
    try:
        local_cursor.execute(sql)
        records=[]
        for record in local_cursor:
            records.append(record)
        return {"column_names":local_cursor.column_names,"rows":records}
    except Exception as e:
        return {"status": "failed", "message": f"Error {e}"}
   

if __name__ == "__main__":
    app.run() 