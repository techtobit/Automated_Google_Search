from MySql import Connection
import mysql.connector


def insertDataInDB(urls, keyword):
		try:
			print(keyword)
			connection = Connection.MySQLConnection()
			cursor= connection.cursor()

			for url in urls:
				insert_stm= (
						"INSERT INTO search_results (keyword, url)"
						"VALUES (%s, %s)"
						)
				data = (keyword, url)
				cursor.execute(insert_stm, data)
				connection.commit()
				print("URLs saved successfully!")
		except Exception as e:
			print(f"Error saving URLs to the database: {e}")
		finally:
			if connection.is_connected():
				cursor.close()
				connection.close()