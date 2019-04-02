import psycopg2
from config import config

class Database:
    def __init__(self, section=None):
        self.section = section
        self.conn = None

        if self.section is not None:
            try:
                # read connection parameters
                params = config(self.section)

                # connect to the PostgreSQL server
                #print('Connecting to the PostgreSQL database...')
                self.conn = psycopg2.connect(**params)
                self.curr = self.conn.cursor()

            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

    def __del__(self):
        if self.conn is not None:
            self.conn.close()
            #print('Database connection closed')

    def fetch_all_db_data(self, sql_stmt):
        self.curr.execute(sql_stmt)
        rows = self.curr.fetchall()

        return rows

    def execute_query(self, sql_stmt):
       self.curr.execute(sql_stmt)

    def delete_from_table(self, table, condition=None):
        if condition is None:
            sql_stmt = f"delete from {table}"
        else:
            sql_stmt = f"delete from {table} where {condition}"

        self.execute_query(sql_stmt)
        self.conn.commit()

    def count_records(self, table):
        sql_stmt = f"select count(*) from {table}"
        self.execute_query(sql_stmt)
        row = self.curr.fetchone()

        return row[0]

