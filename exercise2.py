def email(text1):
    a=0
    b=0
    for i in text1:
        if i == "@":
            a += 1
        if i == ".":
            b += 1
    if a > 0 and b>0:
        print("that is an e-mail")
    else:
        print("that is not an e-mail")
text = str(input("enter your e-mail:"))
email(text)