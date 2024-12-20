from MySql import Connection
import mysql.connector
import xlsxwriter


def insertDataInDB(urls, keyword):
		try:
			print(keyword)
			connection = Connection.MySQLConnection()
			cursor= connection.cursor()
			
			webhockey = xlsxwriter.Workbook(f'{keyword}.xlsx')
			worksheet = webhockey.add_worksheet()

			worksheet.write(0,0, 'Keyword')
			worksheet.write(0,1, 'URL')

			

			for row_num, url in enumerate (urls, start=1):
				insert_stm= (
						"INSERT INTO search_results (keyword, url)"
						"VALUES (%s, %s)"
						)
				data = (keyword, url)
				cursor.execute(insert_stm, data)
				connection.commit()

				worksheet.write(row_num, 0, keyword)
				worksheet.write(row_num, 1, url)
			print("URLs saved successfully in the database and Excel!")
		except Exception as e:
			print(f"Error saving URLs to the database: {e}")
		finally:
			if connection.is_connected():
				cursor.close()
				connection.close()
			webhockey.close()