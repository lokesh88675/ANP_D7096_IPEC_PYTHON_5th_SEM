#to import mysql.connector module
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
#------------------------------------------------------------
# writing update query
sql_query = 'update student set standard = %s, age = %s where stdid = %s'
#------------------------------------------------------------
new_standard = '10th'
new_age = 16
stdid = 'std101'

#put the values to be updated inside a tuple
values = (new_standard, new_age, stdid)
#------------------------------------------------------------
#to execute the query
cursorobj.execute(sql_query, values)
#------------------------------------------------------------
#to commit changes
dataconnection.commit()
#------------------------------------------------------------
#to check data updated or not
if(cursorobj.rowcount > 0):
	print("Data updated successfully")
else:
	print("No record found with given stdid / no changes made")
#------------------------------------------------------------
#to close cursor object
cursorobj.close()
#to close connection object
dataconnection.close()
#------------------------------------------------------------