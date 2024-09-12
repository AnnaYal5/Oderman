import sqlite3


def create_table_if_not_exists():
    try:
        # Підключення до бази даних SQLite
        sqlite_connection = sqlite3.connect("menu_db.db")
        cursor = sqlite_connection.cursor()
        print("Database connected")

        # SQL-запит для створення таблиці, якщо вона не існує
        create_table_query = """
        CREATE TABLE IF NOT EXISTS test_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            category TEXT
        );
        """
        cursor.execute(create_table_query)
        sqlite_connection.commit()
        print("Table created successfully or already exists")

    except sqlite3.Error as error:
        print(f"Error while creating table: {error}")
        return f"Error while creating table: {error}"

    finally:
        if cursor:
            cursor.close()
        if sqlite_connection:
            sqlite_connection.close()
            print("Connection closed")


def insert_into_table(name, description, price, category):
    try:
        # Підключення до бази даних SQLite
        sqlite_connection = sqlite3.connect("menu_db.db")
        cursor = sqlite_connection.cursor()
        print("Database connected")

        # SQL-запит для вставки даних у таблицю
        insert_query = """
        INSERT INTO test_table (name, description, price, category)
        VALUES (?, ?, ?, ?);
        """

        # Кортеж із даними для вставки
        data_tuple = (name, description, price, category)

        # Виконання запиту
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


def get_data_from_table():
    try:
        # Підключення до бази даних SQLite
        sqlite_connection = sqlite3.connect("menu_db.db")
        cursor = sqlite_connection.cursor()
        print("Database connected")

        # SQL-запит для вибірки всіх даних із таблиці
        select_query = "SELECT * FROM test_table;"
        cursor.execute(select_query)

        # Отримання всіх результатів
        records = cursor.fetchall()
        print("Data retrieved successfully")
        return records

    except sqlite3.Error as error:
        print(f"Error while fetching data: {error}")
        return f"Error while fetching data: {error}"

    finally:
        if cursor:
            cursor.close()
        if sqlite_connection:
            sqlite_connection.close()
            print("Connection closed")


# Спочатку створюємо таблицю, якщо вона не існує
create_table_if_not_exists()


# Витягуємо дані
data = get_data_from_table()
for row in data:
    print(row)