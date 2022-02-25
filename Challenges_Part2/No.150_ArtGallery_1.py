#SQL Database로 그림 추적, GUI 사용하기
#새로운 작가와 작품 추가할 수 있어야
#작품이 판매되면 그 작품에 대한 데이터를 SQL 데이터베이스에서 삭제하고 별도의 텍스트 파일에 저장해야
#사용자는 작가, 제작 재료 또는 가격으로 검색할 수 있어야 함
from tkinter import *
import sqlite3
from turtle import width

def add_artist():
    newname = artist_name.get()
    newadd = artist_add.get()
    newtown = artist_town.get()
    newcounty = artist_county.get()
    newpostcode = artist_postcode.get()
    cursor.execute("INSERT INTO Artists (name, address, town, county, postcode) \
        VALUES (?, ?, ?, ?, ?)", (newname, newadd, newtown, newcounty, newpostcode))
    db.commit()
    artist_name.delete(0, END)
    artist_add.delete(0, END)
    artist_town.delete(0, END)
    artist_county.delete(0, END)
    artist_postcode.delete(0, END)
    artist_name.focus()


def clear_artist():
    artist_name.delete(0, END)
    artist_add.delete(0, END)
    artist_town.delete(0, END)
    artist_county.delete(0, END)
    artist_postcode.delete(0, END)
    artist_name.focus()


def add_art():
    newartname = artname.get()
    newarttitle = arttitle.get()
    newartmedium = artmedium.get()
    newartprice = artprice.get()
    cursor.execute("INSERT INTO Art (aritistid, title, medium, price) \
        VALUES (?, ?, ?, ?, ?)", (newartname, newarttitle, newartmedium, newartprice))
    db.commit()
    artname.delete(0, END)
    arttitle.delete(0, END)
    artmedium.delete(0, END)
    artprice.delete(0, END)
    artist_name.focus()




def clear_art():
    pass


#main
with sqlite3.connect("Art.db") as db:
    cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Artists(artistid integer PRIMARY KEY, name text, address text, town text, \
    county text, postcode text);")
cursor.execute("CREATE TABLE IF NOT EXISTS Art (pieceid integer PRIMARY KEY, title text, medium text, price integer);")

   
window = Tk()
window.title("Art Gallery System")
window.geometry("1300x600")

#add new art
title1 = Label(text= "Enter new details: ")
title1.place(x=10, y=10, width= 150, height= 25)

artist_name_lbl = Label(text= "Name: ")
artist_name_lbl.place(x=30, y=40, width= 80, height= 25)
artist_name = Entry(text="")
artist_name.place(x= 110, y=40, width=200, height=25)
artist_name.focus()

artist_add_lbl = Label(text= "Address: ")
artist_add_lbl.place(x=310, y=40, width= 80, height= 25)
artist_add = Entry(text= "")
artist_add.place(x= 390, y= 40, width= 200, height= 25)

artist_town_lbl = Label(text= "Town: ")
artist_town_lbl.place(x=590, y=40, width= 80, height= 25)
artist_town = Entry(text="")
artist_town.place(x=670, y=40, width=200, height=25)

artist_county_lbl = Label(text= "County: ")
artist_county_lbl.place(x=770, y=40, width= 80, height= 25)
artist_county = Entry(text="")
artist_county.place(x=850, y=40, width=200, height=25)

artist_postcode_lbl = Label(text= "Postcode: ")
artist_postcode_lbl.place(x=950, y=40, width= 80, height= 25)
artist_postcode = Entry(text="")
artist_postcode.place(x=1030, y=40, width=200, height=25)

#Create addBtn, clearBtn
addbtn = Button(text= "Add Artist", command= add_artist)
addbtn.place(x=110, y=80, width=130, height=25)

clearbtn = Button(text="Clear Artist", command= clear_artist)
clearbtn.place(x=250, y=80, width=130, height=25)



#Art Info
artname_lbl = Label(text="Artist ID: ")
artname_lbl.place(x=30, y=120, width=80, height=25)
artname = Entry(text="")
artname.place(x=110, y=120, width=50, height=25)

arttitle_lbl = Label(text= "Title: ")
arttitle_lbl.place(x=200, y=120, width=50, height=25)
arttitle = Entry(text="")
arttitle.place(x=280, y=120, width= 280, height=25)

artmedium_lbl = Label(text= "Medium: ")
artmedium_lbl.place(x=590, y=120, width=80, height=25)
artmedium = Entry(text="")
artmedium.place(x=670, y=120, width=100, height=25)

artprice_lbl = Label(text= "Price: ")
artprice_lbl.place(x=770, y=120, width=80, height=25)
artprice = Entry(text="")
artprice.place(x=850, y=120, width=80, height=25)

addartbtn = Button(text="Add Piece: ", command = add_art)
addartbtn.place(x=110, y=150, width=130, height=25)

clearartbtn = Button(text="Add Piece: ", command = clear_art)
clearartbtn.place(x=250, y=150, width=130, height=25)
window.mainloop()