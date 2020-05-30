
# --------Reverse Cypher Program by UmerAftab For Reverse Encryption/Decryption-------
while True:
    Ask = input(
        "press 1 for Encryption or decrption of your message or press 2 to leave : ")
    if Ask == "1":
        Message = input("print message here :")
        translated = " "
        i = len(Message)-1
        while i >= 0:
            translated = translated + Message[i]
            i = i-1
        print(translated)
    elif Ask == "2":
        break
