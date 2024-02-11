import os
import sys
import time
import subprocess
from colorama import Fore, Back, Style,init

init()


y = """

             options:
             
             h/help > help
             1 > ip netstat
             2 > ping to my network
             3 > arp all
             4 > delete my file 

"""

time.sleep(0.2)
x = """
 ______    _    ______
 \    /  /   \  \    /
  \  /  |     |  \  /   
   \/    \ _ /    \/

# Please Enter help 
# This is a network health check tool!
# :)
"""
print(Fore.RED + x)
time.sleep(0.2)
print(Fore.GREEN + "\/\n")


while 1:
    Enter = input("X >> ")


    def netstat():
        time.sleep(0.3)
        os.system('netstat /a')
        
        
    def network():
        ipconfig = subprocess.check_output("ipconfig").decode('utf-8')
        listm = ipconfig.split(":")
        item = ' \r\n\r\nWireless LAN adapter Wi-Fi'

        if item:
            index = listm.index(item)
            del listm[0:index]
            val = listm[9]
            remove = '\r\n   Subnet Mask . . . . . . . . . . . '
            myip = val.replace(remove,"")

        ipL = myip.split(".")
        ipL[3] = 0 

        for ipL[3] in range(256):
            str3 = str(ipL[3])
            x = str(ipL[0]+"."+ipL[1]+".")
            y = str(ipL[2]+"."+str3)
            z = x+y
            os.system(f'ping {z}')
            

        
    def arp():
        time.sleep(0.3)
        os.system('arp /a')


    def delete():
        time.sleep(0.3)
        name = input("Enter your system name:")
        time.sleep(0.4) 
        os.chdir("C:\\")
        os.system("cd /")
        os.system("cd Users")
        os.system(f"cd {name}")
        os.system("cd AppData")
        os.system("cd Local")
        os.system("del Temp")
        
        

    try:
        if Enter == "help":
            print(y)
        elif Enter == "h":
            print(y)
        elif Enter == "1":
            netstat()
        elif Enter == "2":
            network()
        elif Enter == "3":
            arp()
        elif Enter == "4":
            delete()        
        else:
            print("Error...please Enter help!")


    except:
        "Error ... try agian :)"

    





