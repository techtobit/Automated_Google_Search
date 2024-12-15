from MySql import Connection
import mysql.connector


def insertDataInDB(self, urls):
		try:
			connection = Connection.MySQLConnection()
			cursor= connection.cursor()

			for url in urls:
				cursor.execute("INSERT INTO search_results (url) VALUES (%s)", (url,))
				connection.commit()
				print("URLs saved successfully!")
		except Exception as e:
			print(f"Error saving URLs to the database: {e}")
		finally:
			if connection.is_connected():
				cursor.close()
				connection.close()