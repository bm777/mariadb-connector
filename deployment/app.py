# Module Imports
import mariadb
import sys

# Instantiate Connection
try:
   conn = mariadb.connect(
      user="root",
      password="password",
      host="localhost",
      ssl_ca="skysql_chain.pem",
      port=5009)

except mariadb.Error as e:
   print(f"Error connecting to MariaDB Enterprise: {e}")
   sys.exit(1)