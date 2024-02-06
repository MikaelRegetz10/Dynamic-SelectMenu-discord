from mysql.connector import Error
import mysql.connector
import settings


try:
    db = mysql.connector.connect(
        host=settings.DB_HOST,
        user=settings.DB_USERNAME,
        password=settings.DB_PASSWORD,
        database=settings.DB_NAME
    )

except Error as e:
    print(e)