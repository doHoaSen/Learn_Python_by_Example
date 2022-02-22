#색상 목록에서 네 가지 색상을 자동으로 지정, 무작위로 동일한 색상을 두 번 이상 선택 가능, 사용자에게 표시되지 않음
#사용자가 색상 목록에서 네 가지의 색상 선택
#올바른 위치에 올바른 색상이 몇 개이며, 색상은 맞지만 위치가 맞지 않은 것이 몇 개인지 표시
#올바른 위치에 올바른 색상 네 개 선택할 때까지 프로그램 계속되고, 
#프로그램 종료 시 적절한 메시지 표시하고 몇 번 시도했는지 알려주자

#variables: count (시도), wrong_place (색상은 맞지만 위치가 맞지 않음), bingo(올바른 위치에 올바른 색상)

import random

color_list = ["red", "yellow", "green", "blue", "white"]

#program makes choice
def programchoice():
    c1 = random.choice(color_list)
    c2 = random.choice(color_list)
    c3 = random.choice(color_list)
    c4 = random.choice(color_list)
    #print(c1, c2, c3, c4)
    program_data = (c1, c2, c3, c4)
    return program_data

#User makes choice
def userchoice():
    print("The Color List: ", color_list)
    again = True
    while again == True:
        u1 = input("Enter your choice for place 1: ").lower()
        if u1 != "red" and u1 != "yellow" and u1 != "green" and u1 != "blue" and u1 != "white":
            print("Incorrect Selection, Try again. \n")
        else:
            again = False

    again = True
    while again == True:
        u2 = input("Enter your choice for place 2: ").lower()
        if u2 != "red" and u2 != "yellow" and u2 != "green" and u2 != "blue" and u2 != "white":
            print("Incorrect Selection, Try again. \n")
        else:
            again = False
    
    again = True
    while again == True:
        u3 = input("Enter your choice for place 3: ").lower()
        if u3 != "red" and u3 != "yellow" and u3 != "green" and u3 != "blue" and u3 != "white":
            print("Incorrect Selection, Try again. \n")
        else:
            again = False

    again = True
    while again == True:
        u4 = input("Enter your choice for place 4: ").lower()
        if u4 != "red" and u4 != "yellow" and u4 != "green" and u4 != "blue" and u4 != "white":
            print("Incorrect Selection, Try again. \n")
        else:
            again = False

    user_data = (u1, u2, u3, u4)
    return user_data



def playgame(c1, c2, c3, c4, u1, u2, u3, u4):
    wrong_place = 0; bingo = 0
    if c1 == u1:
        bingo += 1
    elif u1 == c2 or u1 == c3 or u1 == c4:
        wrong_place += 1

    if c2 == u2:
        bingo += 1
    elif u2 == c1 or u2 == c3 or u2 == c4:
        wrong_place += 1

    if c3 == u3:
        bingo += 1
    elif u3 == c1 or u3 == c2 or u3 == c4:
        wrong_place += 1

    if c4 == u4:
        bingo += 1
    elif u4 == c1 or u4 == c2 or u4 == c3:
        wrong_place += 1

    print("Correct color in the correct place: ", bingo)
    print("Correct color but in the wrong place: ", wrong_place)
    print()
    return bingo



#main
c1, c2, c3, c4 = programchoice()
count = 0
play = True
while play == True:
    u1, u2, u3, u4 = userchoice()
    bingo = playgame(c1, c2, c3, c4, u1, u2, u3, u4)
    count += 1
    if bingo == 4:
        play = False
    
print("You Win!")
print("You took", count, "guesses")