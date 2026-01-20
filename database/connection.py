import mysql.connector as SQLC

# 1. login to database
database_config = SQLC.connect(
                        host = 'localhost',
                        user = 'root',
                        password = 'mysql', # your myswl workbench password
                        database='notes_management'
                    )

# 2. creating cursor object 
cursor = database_config.cursor(buffered=True)

# Create database if it does not exist and select it
cursor.execute("CREATE DATABASE IF NOT EXISTS notes_management")
cursor.execute("USE notes_management")


# print(database_config)
# print(cursor)

# # creating database
# create_database_query = "CREATE DATABASE IF NOT EXISTS ANIMALS;"
# # 3. execute() function is used to execute the sql queries
# cursor.execute(create_database_query)
# print("Database created successfully")

# # selecting database
# cursor.execute("USE ANIMALS;")

# # CREATING TABLE
# animal_table_query = """
#                     CREATE TABLE ANIMAL(
#                     NAME VARCHAR(30),
#                     AGE INT
#                     );"""
# cursor.execute(animal_table_query)
# print(cursor)
# print("Table created successfully")