# Module Imports
import mariadb
import sys

def create_(conn, sql):
   cursor= conn.cursor()
   cursor.execute(sql)
   conn.commit()




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

   print("creating table")
   create_(conn, "CREATE TABLE IF NOT EXISTS sensor.temperature (id int auto_increment, value decimal(15,2), primary key(id));")


except mariadb.Error as e:
   print(f"Error connecting to MariaDB Enterprise: {e}")
   sys.exit(1)