#메시지의 각 문자는 정해진 만큼 알파벳을 이동해 새로운 문자를 나타냄
#예: 1만큼 이동; abc --> bcd

#issue1: 대소문자 모두 허용할 것인지, 하나로 통일할 것인지 --> lower로 통일시키기
#issue2: 구두점 허용할 것인지
#issue3: 시프트로 인해 문자가 알파벳의 끝을 넘어가게 된다면 처음으로 다시 돌아가야 함

alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",\
"l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
#len(alphabets) == 27


#Make a code
#공백을 포함한 메시지 만들 수 있으며, 숫자를 입력할 수 있어야 함
#입력된 숫자만큼 시프트 코드가 적용된 후 인코딩된 메시지 출력
def getdata():
    message = input("Enter a message: ")
    message = message.lower()
    num = int(input("Enter a number: "))
    if num <= 0 or num > 26:
        while num <= 0 or num > 26:
            num = int(input("You entered wrong number. Please enter a number again between 1-26: "))
    data = (message, num)
    return data


def encoding(message, num):
    new_message = ""
    for letter in message:
        y = alphabets.index(letter)
        y = y + num
        if y > 26:
            y = y - 27
        char = alphabets[y]
        new_message = new_message + char
    print(new_message)
    print()




#Decode a message
#인코딩된 메시지와 올바른 숫자를 입력해야 디코딩된 메시지가 출력됨
#즉, 각 문자를 입력한 숫자만큼 뒤로 이동하여 원래의 문자를 찾도록 함
def decoding(message, num):
    new_message = ""
    for letter in message: 
        y = alphabets.index(letter)
        y = y - num
        if y < 0:
            y += 27
        char = alphabets[y]
        new_message += char
    print(new_message)
    print()



#main
again = True
while again:
    print("""1) Make a code \n2) Decode a message \n3) Quit \n""")
    selection = int(input("Enter your selection: "))
    if selection == 1:
        (message, num) = getdata()
        encoding(message, num)
    elif selection == 2:
        (message, num) = getdata()
        decoding(message, num)
    elif selection == 3:
        again = False
    else:
        print("Wrong selection.\nTry again.\n")