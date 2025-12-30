# mysql connector
import pymysql

# Trick Django into thinking PyMySQL is mysqlclient
pymysql.version_info = (2, 2, 7, "final", 0)  # Pretend it's mysqlclient >= 2.2.1
pymysql.install_as_MySQLdb()
