import random
def algo(cc,uc):
    if cc == uc:
        print(f"Draw!\n You chose: {uc} Computer chose: {cc}")
    elif uc=="s" and cc== "w" or uc=="w" and cc== "g" or uc=="g" and cc== "s":
        print(f"You win!!\n You chose: {uc} Computer chose: {cc}")
    elif uc=="s" and cc=="g" or uc=="w" and cc=="s" or uc=="g" and cc=="w":
        print(f"Computer win!\n You chose: {uc} Computer chose: {cc}")

def cc ():
    n=random.randint(1, 3)
    cc = 0
    if n == 1:
        cc ="s"
    elif n==2:
        cc= "w"
    elif n ==3:
        cc= "g"
    return cc
print("Wellcome to Snake4, Water or Gun Game")
uc = input("Select s,w or g: ")
cc=(cc())
result = algo(cc,uc)
print(result)







