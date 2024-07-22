
import psycopg2
import sqlite3

# PostgreSQL connection
pg_conn = psycopg2.connect(
     dbname="portfolio",
    user="portfolio_User",
    password="password",
    host="localhost",
    port="5432"
)
pg_cur = pg_conn.cursor()

# SQLite connection
sqlite_conn = sqlite3.connect('db.sqlite3')
sqlite_cur = sqlite_conn.cursor()

# Get list of tables
pg_cur.execute("""
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema='public' 
    AND table_type='BASE TABLE'
""")
tables = pg_cur.fetchall()

for table in tables:
    table_name = table[0]
    print(f"Processing table: {table_name}")

    # Get table schema
    pg_cur.execute("""
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_name = %s
    """, (table_name,))
    columns = pg_cur.fetchall()

    # Create table in SQLite
    sqlite_cur.execute(f"DROP TABLE IF EXISTS \"{table_name}\"")
    
    column_defs = []
    for col in columns:
        column_defs.append(f"\"{col[0]}\" {col[1]}")
    create_table_sql = f"CREATE TABLE \"{table_name}\" ({', '.join(column_defs)})"
    
    print(f"Creating table with SQL: {create_table_sql}")
    sqlite_cur.execute(create_table_sql)

    # Copy data
    pg_cur.execute(f'SELECT * FROM "{table_name}"')
    rows = pg_cur.fetchall()
    for row in rows:
        placeholders = ','.join(['?' for _ in row])
        sqlite_cur.execute(f'INSERT INTO "{table_name}" VALUES ({placeholders})', row)

    sqlite_conn.commit()

pg_conn.close()
sqlite_conn.close()

print("Data migration completed successfully.")