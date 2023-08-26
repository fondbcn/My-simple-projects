import mysql.connector

mydb = mysql.connector.connect(database='mysql',host="localhost",user='HP',password="2153")
mycursor = mydb.cursor()
mycursor.execute(" DROP TABLE IF EXISTS jobs;")
mycursor.execute("CREATE TABLE jobs ( JOB_ID integer NOT NULL UNIQUE PRIMARY KEY, JOB_TITLE varchar(35) NOT NULL DEFAULT 'unploy', MIN_SALARY int DEFAULT null, MAX_SALARY int DEFAULT NULL)")
mycursor.execute("INSERT INTO jobs VALUES(5001,'engee',3500,13000)")
mycursor.execute(" INSERT INTO jobs VALUES(5002,'admin',4000,7000)")
mycursor.execute(" INSERT INTO jobs VALUES(5003,'scientist',5000,15000)")
mycursor.execute(" INSERT INTO jobs VALUES(5004,'engee',2500,10000)")
mycursor.execute(" INSERT INTO jobs VALUES(5005,'avocat',4000,10000)")
mycursor.execute('''create procedure get()
                    begin
                      select * from jobs 
                      where MIN_SALARY<3000
                    end;''',multi=True)

#----------------------------------------------------------------------------------------------------
mydb.commit()
mycursor.execute("SELECT * FROM jobs")
r=mycursor.fetchall()
for i in r:
  print (i)
if mydb:
 mycursor.close()
 mydb.close()
 print("\nconnection is closed.")