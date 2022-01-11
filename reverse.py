def rev(string):
    reverse=string[::-1]
    print(reverse)

def rev1(string):
      for i in range(len(string)-1,-1,-1):
          print(string[i],sep=" ",end=" ")
    

string=input("enter a string : ")
print("\nchoose :\n1. method1 \n2. method2")
c=int(input("choice :"))
if(c==1):
    rev(string)
else:
    rev1(string)

