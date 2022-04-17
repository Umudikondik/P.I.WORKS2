import mysql.connector

# First, a database connection is established. Then two different sql queries are prepared, one creates a list that
# stores Device_Type, one creates a list that stores Stats_Access_Link. With the second query LIKE operator,
# it is customized to get the desired string part. Then, with the while loop, the results are written sequentially.
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT Stats_Access_Link FROM database WHERE Stats_Access_Link LIKE <url>https://%<url>")

myresult = mycursor.fetchall()

mycursor2 = mydb.cursor()

mycursor2.execute("SELECT Device_Type FROM database")

myresult2 = mycursor2.fetchall()

i = 0
while i < len(myresult):
    result = myresult[i]
    print(myresult2[i] + " --> " + myresult[i])
