sudo apt install wurl
curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | sudo bash -s -- --mariadb-server-version="mariadb-10.3"
sudo apt install mariadb-server mariadb-client

# Configure APT package repositories
# https://mariadb.com/products/skysql/docs/clients/mariadb-connectors/connector-c/#install-mariadb-connector-c
sudo apt install wget
wget https://downloads.mariadb.com/MariaDB/mariadb_repo_setup
echo "fd3f41eefff54ce144c932100f9e0f9b1d181e0edd86a6f6b8f2a0212100c32c mariadb_repo_setup" | sha256sum -c -
chmod +x mariadb_repo_setup
sudo ./mariadb_repo_setup --mariadb-server-version="mariadb-10.5"
sudo apt update

# install mariaDB connector
sudo apt install libmariadb3 libmariadb-dev