import mysql.connector
from mysql.connector import Error

class DBHelper:

    def __init__(self, user, password, database, host='localhost'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def getConnection(self):
        conn = None
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database)

            if conn.is_connected():
                print('Connection is successfull')

        except Error as e:
            print(e)

        return conn


    def create(self, connection):
        cursor = connection.cursor()
        query = """
                CREATE TABLE IF NOT EXISTS `share`.`tempdb` (
                  `ShareCode` INT NOT NULL,
                  `ShareQuantity` FLOAT NULL,
                  `ShareAverage` FLOAT NULL,
                  PRIMARY KEY (`ShareCode`));
                """

        try:
            cursor.execute(query)
            connection.commit()
            cursor.close()
        except Error as e:
            print('Error : ' + e.msg)


    def query(self, connection):
        cursor = connection.cursor()
        SQL = "SELECT ShareCode, ShareQuantity, ShareAverage FROM myshares"
        try:
            cursor.execute(SQL)
            results = cursor.fetchall()
            return results

            cursor.close()
        except Error as e:
            print('Error : ' + e.msg)


    def insert(self, connection, ShareCode, ShareQuantity, ShareAverage):
        cursor = connection.cursor()
        SQL = "INSERT INTO myshares (ShareCode, ShareQuantity, ShareAverage) VALUES (%s, %s, %s)"
        values = (ShareCode, ShareQuantity, ShareAverage)

        try:
            cursor.execute(SQL, values)
            connection.commit()
            cursor.close()
            print("Insert was successful")
        except Error as e:
            print(e)


    def where(self, connection, population):
        cursor = connection.cursor()
        SQL = "SELECT * FROM city WHERE Population > %s"
        val = (population, )
        cursor.execute(SQL, val)
        results = cursor.fetchall()

        for result in results:
            print(result)

        cursor.close()


    def orderby(self, connection):
        cursor = connection.cursor()
        SQL = "SELECT * FROM city ORDER BY Population"
        cursor.execute(SQL)

        results = cursor.fetchall()
        for result in results:
            print(result)

        cursor.close()


    def delete(self, connection, shareCode):
        cursor = connection.cursor()
        SQL = "DELETE FROM myshares WHERE ShareCode = %s"
        code = (shareCode, )

        try:
            cursor.execute(SQL, code)
            connection.commit()
            print("record(s) deleted")
        except Error as e:
            print(e)
        finally:
            cursor.close()


    def update(self, connection, share_code, share_quantity, share_average):
        cursor = connection.cursor()
        SQL = "UPDATE myshares SET ShareQuantity = %s, ShareAverage = %s WHERE ShareCode = %s"
        val = (share_quantity, share_average, share_code)

        try:
            cursor.execute(SQL, val)
            connection.commit()
            print("record updated")
        except Error as e:
            print(e)
        finally:
            cursor.close()


"""
CREATE TABLE IF NOT EXISTS `share`.`myshares` (
  `ShareCode` INT NOT NULL,
  `ShareQuantity` FLOAT NULL,
  `ShareAverage` FLOAT NULL,
  PRIMARY KEY (`ShareCode`));
"""