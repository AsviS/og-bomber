import bombOg as b
import getpass
import os
banner="""

    ██████╗  ██████╗       ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗
    ██╔═══██╗██╔════╝       ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
    ██║   ██║██║  ███╗█████╗██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
    ██║   ██║██║   ██║╚════╝██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
    ╚██████╔╝╚██████╔╝      ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
    ╚═════╝  ╚═════╝       ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                    ---------text & call bomber-spoofing---------
                            -----author : Samartha-----
                                 ---build v1.0---
"""
os.system('cls')
print(banner)
un=getpass.getuser()
pn=input("Enter number : ")
n=int(input("Enter limit : "))
cc=input("Country Code :")
if b.checkConnectivity():
    if b.ifExists(un):
        if b.checkQuota(b.getUserDetails(un)):
            if b.blackList(pn):
                b.startBombing(pn,cc,n,un)
            else:
                print("This number has been blacklisted")
                exit()
        else:
            print("You have exhausted your daily quota\nSubscribe premium to get unlimited msg")
    else:
        print("You have not registered for the service\nRun setup.py to register")
else:
    print("Check your internet Connection")
