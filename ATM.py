from os import system
import time
import random
from typing import Text, TextIO, Type

# ATM Siytem
def plus(Mny_set, Add_mny):
    plus=float(Mny_set) + float(Add_mny)
    return plus

def minus(Mny_set, Rmv_mny):
    minus=float(Mny_set) - float(Rmv_mny)
    return minus


print("Starting...")
time.sleep(10)
print(100*"\n")
print("|=============================|")
print("|===========Welcome===========|")
print("|=============================|\n")
Rd_code=random.randint(1,100000)

print("By: DimDev#5240\n")
print("|=============Fake ATM=============|\n")
Mny_plyr=input("Set Your Money: ")
lgin_atm_plyr=random.randint(1, 100)
print("Making Login Fake ATM...")
time.sleep(5)

lgin_atm=lgin_atm_plyr

print("Confirm Money...")
time.sleep(5)
print("Your Login Fake Atm:", lgin_atm_plyr)
time.sleep(5)
print("Done!!")
time.sleep(1)

while True:
    print("\n\n\n\n\n\n|===========Fake ATM Menu===========|")
    print("1. Cheak Money")
    print("2. Money Tube")
    print("3. Withdraw Money")
    Atm_awl=int(input("Select Option: "))
    
    Mny_set=Mny_plyr
    
    if Atm_awl==1:
        lgin_atm1=int(input("Login ATM: "))
        if lgin_atm1==lgin_atm:
            print("Your Money:", Mny_plyr)
            time.sleep(3)
        else:
            print("Infalid Login Fake ATM", +lgin_atm1)

    elif Atm_awl==2:
        lgin_atm2=int(input("Login ATM: "))
        if lgin_atm2==lgin_atm:
            print("Your Money", Mny_plyr)
            Add_mny=input("Add Money: ")
            print("Done!, Now Your Fake Money:", plus(Mny_set, Add_mny))
            time.sleep(3)
        else:
            print("Infalid Login ATM", +lgin_atm2)

    elif Atm_awl==3:
        lgin_atm3=int(input("Login ATM: "))
        if lgin_atm3==lgin_atm:
            print("Your Money:", Mny_plyr)
            Rmv_mny=input("Withdraw Money: ")
            print("Done!, Now Your Fake Money", minus(Mny_set, Rmv_mny))
            time.sleep(3)
        else:
            print("Infalid Login ATM", +lgin_atm3)