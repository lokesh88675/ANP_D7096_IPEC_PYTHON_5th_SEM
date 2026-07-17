#to import mysql.connector modulestd
import mysql.connector
#------------------------------------------------------------
#to establish connection with mysql
dataconnection = mysql.connector.connect(host = 'localhost',
	user = 'root',
	password = 'Lokesh21@.',
	database = 'studentmanagement'
	)
#------------------------------------------------------------
# to create a cursor object
cursorobj = dataconnection.cursor()
#------------------------------------------
stdid = input("enter the user id")
sql_query = 'delete from student where stdid = %s'

#put the values to be  delete into a tuple

#------------------------------------------------------------
#to execute the query
cursorobj.execute(sql_query,(stdid,))
#------------------------------------------------------------
#to commit changes
dataconnection.commit()
#------------------------------------------------------------
#to check data inserted or not
if(cursorobj.rowcount  > 0):
	print("Data deletedsuccessfully")
else:
	print(" data")
#------------------------------------------------------------
#to close cursur object
cursorobj.close()
#to close connection object
dataconnection.close()
#------------------------------------------------------------
 