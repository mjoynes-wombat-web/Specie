lsimport MySQLdb
import MySQLdb.cursors

def connection():
    conn = MySQLdb.connect(host='localhost',
                           user='ssmith',
                           passwd='------------------',
                           db='Specie',
                           cursorclass=MySQLdb.cursors.DictCursor)
    c = conn.cursor()

    return c, conn
