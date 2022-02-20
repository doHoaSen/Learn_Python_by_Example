#142
#141번 프로그램의 BookInfo 사용하고 저자와 그의 출생지 목록을 출력
#출생지 입력하라고 요청하고, 입력된 값에서 태어난 저자의 모든 책에 대한 제목과 출간일 그리고 저자의 이름을 표시하도록 하자
print("No.142")
import sqlite3
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("Select * from Authors")
for row in cursor.fetchall():
    print(row)

print()
location = input("Enter a place of birth: ")
print()

cursor.execute("""Select Books.Title, Books.Year, Books.Author From Books, Authors Where Authors.Name = Books.Author 
AND Authors.Place_of_Birth = ?""", [location])
for row in cursor.fetchall():
    print(row)

db.close()
print()
print("********************************************************************************")
#143
#BooksInfo 사용, 사용자에게 연도 입력하라고 요청
#입력한 연도 이후의 모든 책을 출간된 연도 순으로 정렬해 출력하라
print("No.143")
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

year = int(input("Enter a year: "))
print()

cursor.execute("Select Books.Title, Books.year, Books.Author From Books Where Year > ? Order By Year", [year])
for row in cursor.fetchall():
    print(row)

db.close()
print("********************************************************************************")
#144
#사용자에게 저자의 이름을 입력하라고 요청, 입력된 저자와 모든 책 정보를 텍스트 파일에 저장하라
#각 필드는 대시로 구분하기
print("No.144")
print()
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

f = open("Booklist.txt", "w")

cursor.execute("Select Name From Authors")
for row in cursor.fetchall():
    print(row)
print()

author = input("Enter a name: ")
cursor.execute("Select * From Books Where Author = ?", [author])
for x in cursor.fetchall():
    newrecord = str(x[0]) + "-" + x[1] + "-" + x[2] + "-" + str(x[3]) + "\n"
    f.write(newrecord)

f.close()
db.close()