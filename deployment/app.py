# Module Imports
import mariadb
import sys

def execute(conn, sql):
   cursor= conn.cursor()
   cursor.execute(sql)

   row_headers = [value[1] for value in cursor]

   return row_headers

def create_(conn, sql):
   cursor= conn.cursor()
   cursor.execute(sql)
   conn.commit()

def update_(conn, sql):
   create_(conn, sql)


# Instantiate Connection
try:
   conn = mariadb.connect(
      user="root",
      password="password",
      host="localhost",
      ssl_ca="skysql_chain.pem",
      port=5009)

   # create database
   #create_(conn, "CREATE DATABASE sensor")

   print("inserting value")
   #create_(conn, "insert into sensor.temperature (value) values (41);")

   print("select operations")
   temperatures = execute(conn, "SELECT * FROM sensor.temperature;")
   print([int(t) for t in temperatures])

   print("update operations")
   update_(conn, "UPDATE sensor.temperature SET value={} where id={};".format(75, 5))


   print("select operations")
   temperatures = execute(conn, "SELECT * FROM sensor.temperature;")
   print([int(t) for t in temperatures])

except mariadb.Error as e:
   print(f"Error connecting to MariaDB Enterprise: {e}")
   sys.exit(1)