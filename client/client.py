from socket import *
from modules import menu,messaging
def main():
    server_ip = "192.168.1.88"
    server_port = 1033

    while True:
        #Create an IPV4(using AF_INET) TCP socket.If UDP socket use SOCK_DGRAM
        c_soc = socket(AF_INET,SOCK_STREAM)
        c_soc.connect((server_ip,server_port)) # Takes in a tuple. Set up connection with server.

        menu()
        choice = input("Key in choice as per options above: ")
        if choice == "0":
            print("Program exiting..")
            break
        elif choice == "1":
            select(c_soc)
        elif choice == "2":
            update(c_soc)
        elif choice == "3":
            insert(c_soc)
        elif choice == "4":
            delete(c_soc)
        else:
            print("ERROR!! Choose the right option as per the menu")

        c_soc.close()

def select(c_soc):
    print("\nChoose from the menu below\n")
    print("1=Search by hostname\n2=Search by management IP\n")
    num = input("Enter number from menu: ")
    
    if num == "1":
        hn = input("hostname: ")
        out_str = "SELECT:hostname:"+hn
    elif num == "2":
        ip = input("Management IP: ")
        out_str = "SELECT:mgt_ip:"+ip
        
    print(messaging(c_soc,out_str)) 

def update(c_soc):
    print("\nChoose what to update from below\n")
    print("1=Hostname\n2=Mngt IP\n3=Serial Num\n4=vendor\n5=Software version\n6=Region/State\n")
    choice = input("Key in the choice : ")
    if choice == "1":
        ip = input("Current management ip address : ")
        hn = input("Updated hostname:")
        out_str = "UPDATE:hostname:"+hn+":mgt_ip:"+ip
    else:
        hn = input("Device hostname:")
        if choice == "2":
            v1 = ":mgt_ip:"
            v2 = input("Updated management ip:")
        elif choice == "3":
            v1 = ":serial_num:"
            v2 = input("Updated serial number:")
        elif choice == "4":
            v1 = ":vendor:"
            v2 = input("Updated vendor:")
        elif choice == "5":
            v1 = ":sw_version:"
            v2 = input("Updated software version:")
        elif choice == "6":
            v1 = "region:"
            v2 = input("Updated region/state:")
        out_str = "UPDATE"+ v1 + v2 + ":hostname:"+hn
    
    #in_str = messaging(c_soc,out_str)
    print(messaging(c_soc,out_str)) 


def insert(c_soc):
    # Collect and send values as a string
    #(hostname,mgt_ip,serial_num,vendor,sw_version,region)
    
    x = ":"
    hn = input("Hostname : ")
    ip= input("Management IP : ")
    sn= input("Serial number : ")
    ven = input("Vendor : ")
    sw = input("Software version : ")
    rg = input("State/region : ")
    
    """
    x = ":"
    hn = 'z-tas-r01'
    ip= '10.5.1.1'
    sn= 'sn555555'
    ven = 'viptela'
    sw = '1.04.1b'
    rg = 'tas'
    """
    
    out_str = "INSERT:" + hn + x + ip + x + sn + x + ven + x + sw + x + rg
    print(messaging(c_soc,out_str))

def delete(c_soc):
    out_str = "DELETE:" + input("Hostname to delete:")
    print(messaging(c_soc,out_str))

if __name__ == "__main__":
    main()

        