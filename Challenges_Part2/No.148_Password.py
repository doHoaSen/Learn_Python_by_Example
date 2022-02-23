import csv

def get_data():
    f = list(csv.reader(open("passwords.csv")))
    tmp = []
    for x in f:
        tmp.append(x)
    return tmp



#Create User ID and PW (1)
def create_id(tmp):  
    #아이디 중복 확인하기
    again = True
    while again == True:
        userid = input("Enter a new ID: ")
        userid.lower()
        req = False
        for y in tmp:
            if userid in y[0]:
                print(userid, "has already been allocated. Try again.")
                req = True
        if req == False:
            again = False
    return userid


def create_pw():
    sclist = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "?"]
    nlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    tryagain = True
    while tryagain == True:
        score = 0
        uc = False  #대문자
        lc = False  #소문자
        sc = False  #특수기호
        n = False   #숫자
        pw = input("Enter Password: ")
        if len(pw) >= 8:
            score += 1
        for x in pw:
            if x.islower():
                lc = True
            if x.isupper():
                uc = True
            if x in sclist:
                sc = True
            if x in nlist:
                n = True
        if lc == True:
            score += 1
        if uc == True:
            score += 1
        if sc == True:
            score += 1
        if n == True:
            score += 1

        if score == 1 or score == 2:
            print("This is a weak password, try again")
        
        if score == 3 or score == 4:
            print("This password could be improved")
            again = input("Do you want to try for a stronger password? (y/n): ")
            again.lower()
            if again == "n":
                tryagain = False
        if score == 5:
            tryagain = False
    
    return pw


#Change PW (2)
def changepw(userid, tmp):
    if userid !="":
        new_pw = create_pw()
        ID = userid.index(userid)
        tmp[ID][1] = new_pw
        f = open("passwords.csv", "w")
        for row in tmp:
            newrecord = row[0] + ", " + row[1] + "\n"
            f.write(newrecord)
        f.close()



#Find UserID
def findid(tmp):
    again = True
    userid =""
    while again == True:
        searchid = input("Enter the userID you are looking for: ")
        searchid.lower()
        for y in tmp:
            if searchid in y[0]:
                req = True    
        if req == True:
            userid = searchid
            again = False
        else:
            print(searchid, "is NOT in the list")

    return userid

        

#Display all user IDs
def displaydata():
    tmp = get_data()
    for row in tmp:
        print(row[0])

#main
tmp = get_data()
again = True
while again == True:
    print("1) Create a new User ID \n2) Change a password \n3) Display all User IDs \n4) Quit")
    print()
    selection = int(input("Enter Selection: "))
    if selection == 1:
        userid = create_id(tmp)
        password = create_pw()
        f = open("passwords.csv", "a")
        newrecord = userid + ", " + password + "\n"
        f.write(str(newrecord))
        f.close()
    elif selection == 2:
        find_userid = findid(tmp)
        changepw(find_userid, tmp)
    elif selection == 3:
        displaydata()
    elif selection == 4:
        print("Finish the program. Thank you.")
        again = False
    else:
        print("Wrong selection. Try again. \n")