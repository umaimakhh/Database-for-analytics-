createtblStudentTable  = """CREATE TABLE Studentd -- creating Employee Details table
(
  
  Name VARCHAR2(25),
  StudentID NUMBER(7),
  Address VARCHAR2(50),
  GradYear NUMERIC(4),
  
  CONSTRAINT Namepk
     PRIMARY KEY(StudentID)
);"""

createtblGradeTable  = """CREATE TABLE Graded -- creating Employee Job table
(
CName VARCHAR2(25),
  StudentID NUMBER(7),
  CGrade NUMBER(4),


     	FOREIGN KEY (CName)
		REFERENCES CourseD (CName),
     
     	FOREIGN KEY (StudentID)
		REFERENCES Studentd (StudentID)
);"""

createtblCourses  = """CREATE TABLE CourseD -- creating Employee Job table
(
CName VARCHAR2(25),
  Department VARCHAR2(7),
  Credits NUMBER(1),

  CONSTRAINT CName_pk
     PRIMARY KEY(CName)
);"""

import sqlite3
conn = sqlite3.connect('dsc450.db') # open the connection
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS Graded') 
cursor.execute('DROP TABLE IF EXISTS CourseD')  
cursor.execute('DROP TABLE IF EXISTS Studentd')  
 

cursor.execute(createtblStudentTable)
cursor.execute(createtblGradeTable)
cursor.execute(createtblCourses)


insertStudent = ["INSERT INTO Studentd VALUES ('James Muriel Last', 1, '350 StoneTX', 2020);",
"INSERT INTO Studentd VALUES ('Alin Murl Last', 2, 'Boston TX', 2016);",
"INSERT INTO Studentd VALUES ('James Murl Last', 3, 'Houston CA', 2015);",
"INSERT INTO Studentd VALUES ('James Muriel Last', 4, ' Greendale LA', 2014);",
"INSERT INTO Studentd VALUES ('Umaima KH Ahmad', 5, ' Houston TX', 2014);",
"INSERT INTO Graded VALUES ('Alebgra', 1, 89);",
"INSERT INTO Graded VALUES ('Maths', 2, 55);",
"INSERT INTO Graded VALUES ('Database', 3, 90);",
"INSERT INTO Graded VALUES ('DV', 4, 65);",
"INSERT INTO Graded VALUES ('Alebgra', 4, 89);",
"INSERT INTO Graded VALUES ('Maths', 3, 55);",
"INSERT INTO Graded VALUES ('Database', 2, 90);",
"INSERT INTO Graded VALUES ('DV', 1, 65);",
"INSERT INTO Graded VALUES ('Film', 4, 90);",
"INSERT INTO Graded VALUES ('BI', 2, 65);",
"INSERT INTO CourseD VALUES ('Alebgra', 'cdm', 4);",
"INSERT INTO CourseD VALUES ('Maths', 'cdc', 4);",
"INSERT INTO CourseD VALUES ('Database', 'cdm', 3);",
"INSERT INTO CourseD VALUES ('DV', 'cdm', 4);",
"INSERT INTO CourseD VALUES ('Film', 'MFA', 3);",
"INSERT INTO CourseD VALUES ('BI', 'Business', 4);",
"INSERT INTO CourseD VALUES ('Science', 'Bio', 4);"]

for ins in insertStudent:         # insert the Student rows
    cursor.execute(ins)


#part 4a
sqlInsert = """select SG.StudentID,SG.Name,SG.Address,SG.GradYear,coursed.Cname,Coursed.Department,Coursed.credits from
(select Studentd.StudentID ,Studentd.Name,Studentd.Address,Studentd.GradYear,Graded.Cname,Graded.CGrade
from Studentd  LEFT OUTER JOIN Graded  ON Studentd.StudentID = Graded.StudentID) 
SG Left outer join Coursed ON SG.cname = coursed.cname
union
select CG.StudentID,studentd.Name,studentd.Address,studentd.GradYear,CG.Cname,CG.Department,CG.credits from
(select c.cname,c.department,c.credits,g.studentID from Coursed c left outer join Graded g on c.cname=g.cname) CG left outer join
Studentd on CG.StudentID = studentd.StudentID;"""

executeQuery  = cursor.execute(sqlInsert)

print("\nFetching data from query -- \n")
Result = executeQuery.fetchall()
conn.commit()


outfile= open("E:\DPU\winter 2020\\output.txt","w+")
count = 0
print("\nStroing data in output file -- \n")

for x in Result:
    revisedString = str(Result[count]).replace("(","")
    revisedString2 = revisedString.replace(")","")
    revisedString3 = revisedString2.replace("'","")
    outfile.write(revisedString3+'\n')
    print(revisedString3)
    count = count +1

#part 4E PART 1

createView = """ CREATE VIEW queryData AS
select SG.StudentID,SG.Name,SG.Address,SG.GradYear,coursed.Cname,Coursed.Department,Coursed.credits from
(select Studentd.StudentID ,Studentd.Name,Studentd.Address,Studentd.GradYear,Graded.Cname,Graded.CGrade
from Studentd  LEFT OUTER JOIN Graded  ON Studentd.StudentID = Graded.StudentID) 
SG Left outer join Coursed ON SG.cname = coursed.cname
union
select CG.StudentID,studentd.Name,studentd.Address,studentd.GradYear,CG.Cname,CG.Department,CG.credits from
(select c.cname,c.department,c.credits,g.studentID from Coursed c left outer join Graded g on c.cname=g.cname) CG left outer join
Studentd on CG.StudentID = studentd.StudentID;"""
executeView  = cursor.execute(createView)

newQueryDepartment = '''Select department , AVG(GradYear) from queryData where department group by department;'''

print("\nFetching data from query - For every department, display the first graduation year -- \n")
executeQueryDepartment  = cursor.execute(newQueryDepartment)
Result = executeQueryDepartment.fetchall()
print(Result)
conn.commit()