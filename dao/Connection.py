import psycopg2
from .config import config

class Connection():
    def getConnection():
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)

            return conn

        except (Exception, psycopg2.DatabaseError) as error:
            print("* Connection.py ERROR!")
            print(error)

    def testConnection():
        conn = None
        try:
            conn = Connection.getConnection()
            # create a cursor
            cur = conn.cursor()
            
            # execute a statement
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            print(db_version)
            
            # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')

#if __name__ == '__main__':
#    Connection.testConnection()