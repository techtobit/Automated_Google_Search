import mysql.connector

def MySQLConnection():
	try:
			connection=mysql.connector.connect(
				host= 'sql.freedb.tech',
				port= '3306',
				username= 'freedb_ashrafuddin27',
				password= 'D5%%mbk8rk%D2u9',
				database= 'freedb_ags_db',
			)

			cursor=connection.cursor()
			create_table_query = """
        CREATE TABLE IF NOT EXISTS search_results (
            id INT AUTO_INCREMENT PRIMARY KEY,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
						keyword TEXT NOT NULL,
            url TEXT NOT NULL
        );
        """
			cursor.execute(create_table_query)
			print('database connected')
			return connection
	except mysql.connector.Error as e:
		print(f'Error to connect database ${e}')
		raise
