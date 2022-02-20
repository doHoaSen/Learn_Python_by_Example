#저자의 목록과 그들이 쓴 저서를 저장할 BookInfo라는 새 SQL DB 생성
#Authors 라는 테이블과 Books라는 테이블 만들기

import sqlite3
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

#Create "Authors" Table
cursor.execute("""Create Table if not exists Authors(Name text Primary key, 
Place_of_Birth text)""")

cursor.execute("""Insert into Authors(Name, Place_of_Birth) Values("Agatha Christie", "Torquay")""")
db.commit()

cursor.execute("""Insert into Authors(Name, Place_of_Birth) Values("Cecelia Ahern", "Dublin")""")
db.commit()

cursor.execute("""Insert into Authors(Name, Place_of_Birth) Values("J.K. Rowling", "Bristol")""")
db.commit()

cursor.execute("""Insert into Authors(Name, Place_of_Birth) Values("Oscar Wilde", "Dublin")""")
db.commit()

cursor.execute("select * from Authors")
for row in cursor.fetchall():
    print(row)

print("*****************************************************************************")

#Create "Books" Table
cursor.execute("Create Table if not exists Books(ID integer primary Key, Title text, Author text, Year integer)")

cursor.execute("""Insert into Books(ID, Title, Author, Year) VALUES("1", "De Profundis", "Oscar Wilde", "1905")""")
db.commit()

cursor.execute("""Insert into Books(ID, Title, Author, Year) VALUES("2", "Harry Potter and the chamber of secrets", "J.K. Rowling", "1998")""")
db.commit()

cursor.execute("""Insert into Books(ID, Title, Author, Year) VALUES("3", "Harry Potter and the prisoner of Azkaban", "J.K. Rowling", "1999")""")
db.commit()

cursor.execute("""Insert into Books(ID, Title, Author, Year) VALUES("4", "Lyrebird", "Cecelia Ahern", "2017")""")
db.commit()

cursor.execute("""Insert into Books(ID, Title, Author, Year) VALUES("5", "Murder on the Orient Express", "Agatha Christie", "1934")""")
db.commit()

cursor.execute("""Insert into Books(ID, Title, Author, Year) VALUES("6", "Perfect", "Cecelia Ahern", "2016")""")
db.commit()

cursor.execute("""Insert into Books(ID, Title, Author, Year) VALUES("7", "The marble collector", "Cecelia Ahern", "2016")""")
db.commit()

cursor.execute("""Insert into Books(ID, Title, Author, Year) VALUES("8", "The murder on the links", "Agatha Christie", "1923")""")
db.commit()

cursor.execute("""Insert into Books(ID, Title, Author, Year) VALUES("9", "The picture of Dorian Gray", "Oscar Wilde", "1890")""")
db.commit()

cursor.execute("""Insert into Books(ID, Title, Author, Year) VALUES("10", "The secret adversary", "Agatha Christie", "1921")""")
db.commit()

cursor.execute("""Insert into Books(ID, Title, Author, Year) VALUES("11", "The seven dials mystery", "Agatha Christie", "1929")""")
db.commit()

cursor.execute("""Insert into Books(ID, Title, Author, Year) VALUES("12", "The year I met you", "Cecelia Ahern", "2014")""")
db.commit()

cursor.execute("Select * from Books")
for row in cursor.fetchall():
    print(row)