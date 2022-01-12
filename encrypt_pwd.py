import base64

def encrypt(pwd):
    ecy=base64.b64encode(pwd.encode("UTF-8"))
    print(ecy)

#def decrypt(ecy):
#   dcy=base64.b64decode(ecy.decode("UTF-8"))
#   print(dcy)
    
pwd=input("enter password :")
encrypt(pwd)
