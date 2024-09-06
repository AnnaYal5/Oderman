import sqlite3


def insert_into_table(name, description, price, category):
    try:
        # Connect to the SQLite database
        sqlite_connection = sqlite3.connect("menu_db.db")
        cursor = sqlite_connection.cursor()
        print("Database connected")

        # SQL query to insert data into the table (without id)
        insert_query = """
        INSERT INTO test_table 
        (name, description, price, category)
        VALUES (?, ?, ?, ?);
        """

        # Tuple containing the data to be inserted
        data_tuple = (name, description, price, category)

        # Execute the query and commit the transaction
        cursor.execute(insert_query, data_tuple)
        sqlite_connection.commit()
        print("Data inserted successfully")


    except sqlite3.Error as error:

        print(f"Error while adding item: {error}")

        return f"Error while adding item: {error}"

    finally:
        if cursor:
            cursor.close()
        if sqlite_connection:
            sqlite_connection.close()
            print("Connection closed")


