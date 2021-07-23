from socket import *
import time
from modules import Querry,Messaging,sql_connect,list_to_json

def main():
    serverIP = "192.168.1.88"  # You can use gethostbyname(gethostname())
    appPort = 1033 # Port you want for the application.
    serverSocket = socket(AF_INET, SOCK_STREAM)  # Create the socket object
    serverSocket.bind((serverIP, appPort))  # Bind the socket to ip & port
    serverSocket.listen(5)  # Listen to incoming connections, 5 at a time.
    print("Listening to incoming connections..........\n")

    while True:
        connectionSocket, clientAddr = serverSocket.accept()
        #print("connectionSocket printout: ", connectionSocket)
        print("=======================================================")
        print("New connection: ", clientAddr)
        print("TIME : ", time.strftime("%a,%d %b %Y %H:%M:%S"))
        msgRecv = connectionSocket.recv(1024)

        #Decode message recieved ===================================
        in_msg = msgRecv.decode("utf-8")
        print("Request received: " + in_msg )

        #Make decision based on incoming string =====================
        if in_msg == "all":
            query = "select * from cmdb"
            print("DB Query : ", query)

        elif "SELECT" in in_msg:
            tupl = (
                    in_msg.split(":")[1],
                    in_msg.split(":")[2]
                    )
            try:
                result = Querry(sql_connect(),tupl).select()
                out_str = list_to_json(result)
            except UnboundLocalError:
                print("UnboundLocalError: local variable 'dict' referenced\
                      before assignment")
                out_str = "ERROR!! DB Search failed"
        
        elif "UPDATE" in in_msg:
            tupl = (
                    in_msg.split(":")[1],
                    in_msg.split(":")[2],
                    in_msg.split(":")[3],
                    in_msg.split(":")[4]
                    )
            Querry(sql_connect(),tupl).update()
            out_str = in_msg.split(":")[4] + " : successfully updated"
            # To include error catching here.
            
        elif "INSERT" in in_msg:
            tupl = (
                    in_msg.split(":")[1],
                    in_msg.split(":")[2],
                    in_msg.split(":")[3],
                    in_msg.split(":")[4],
                    in_msg.split(":")[5],
                    in_msg.split(":")[6],
                    )
            Querry(sql_connect(),tupl).insert()
            out_str = in_msg.split(":")[1] + " : successfully inserted"
            # To include error catching here.
            
        elif "DELETE" in in_msg:
            tupl = (in_msg.split(":")[1],)
            Querry(sql_connect(),tupl).delete()
            out_str = in_msg.split(":")[1] + " : successfully deleted"
            # To include error catching here.
            
        else:
            out_str = "ERROR! Process failure"

        Messaging(out_str,connectionSocket).process()
        connectionSocket.close()
        print("Connection with client closed\n")

if __name__ == "__main__":
    main()
