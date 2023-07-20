import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='12345',
    database='your_database'
)

# Create a table
cursor = db.cursor()
cursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")

# Insert data into the table
sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
values = ("John", 20)
cursor.execute(sql, values)
db.commit()

# Delete data from the table
sql = "DELETE FROM students WHERE id = %s"
values = (1,)
cursor.execute(sql, values)
db.commit()

# Update data in the table
sql = "UPDATE students SET age = %s WHERE name = %s"
values = (25, "John")
cursor.execute(sql, values)
db.commit()

# Close the connection
cursor.close()
db.close()
