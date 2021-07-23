# Modules for client side
from socket import *
import json

def display(in_str):
    """
    Convert the incoming json string to a dictionary.
    """
    print("\n===============DEVICE DETAILS=======================\n")
    #print(in_str)
    dictx = json.loads(in_str)
   
    print("hostname : ", dictx["hostname"])
    print("mgt_ip : ", dictx["mgt_ip"])
    print("region: ", dictx["region"])
    print("vendor : ", dictx["vendor"])
    print("serial_num : ", dictx["serial_num"])
    print("Sw_version : ", dictx["sw_version"])
    print("\n===============================================\n")

def messaging(c_soc,msg_out):
    # Function to do the messaging with server
    #STEP 1 : To server ========================================
    print("Message to server : ",msg_out)
    c_soc.send(msg_out.encode("utf-8")) #Send encoded message.
    print("\nQuerry sent to server.......\n")

    #STEP 2: From server ========================================
    msg_in = c_soc.recv(1024)
    #print("Message from server :",msg_in.decode("utf-8"))
    return msg_in.decode("utf-8") #Comes in as a string 
    
def menu():
    # Menu function
    print("\n-------MAIN MENU----------\n")
    print("0 = Exit the program")
    print("1 = Search for a specific device details using hostname or Management IP")
    print("2 = Update existing device records[Hint: Use option 1 to check current stored information]")
    print("3 = Add new device")
    print("4 = Delete device from records")
    print("\n-------------------------\n")