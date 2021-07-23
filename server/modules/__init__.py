import mysql.connector
from mysql.connector import Error
import json

def sql_connect():
    """
    - Creates SQL Connection
    - Trying to look cool using the ** (unpacking) operator
    config = config = {
            'host':'localhost',
            'user':'<user_name>',
            'passwd':'<password>',
            'database': '<database name>'
        }
    """
    try: 
        from modules.secret import config
        conx = mysql.connector.connect(**config)

        if conx.is_connected():
            """
            The is_connected() is the method of the MySQLConnection class 
            through which we can verify is our Python application 
            connected to MySQL.
            """
            db_Info = conx.get_server_info()
            print("Connected to MySQL Server version" , db_Info)
            #cursor = connection.cursor()
            return conx
                
    except Error as err:
            print("Error while connecting to MySQL", err)


class Querry():
    """Class that has methods perfoming the CRUD.More details in README"""
    
    def __init__(self,connection,tupl):
        self.connection = connection
        self.tupl = tupl
        
    def select(self):
        """Method to select.More info in README"""
        
        sql_query = "select * from cmdb where %s='%s'"% self.tupl
        print("SQL Query: ",sql_query)
        
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(sql_query)
            output = cursor.fetchall()
            #print(output)
            cursor.close()
            print("Cursor instance closed")
            return output
        
        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                #cursor.close()
                print("MySQL connection is closed")
    
    def insert(self):
        """Method to insert.More info in README"""
        
        sql_query = """INSERT INTO cmdb (hostname,mgt_ip,serial_num,vendor,
        sw_version,region) VALUES (%s,%s,%s,%s,%s,%s)"""
        
        try:
            #print(sql_query)
            cursor = self.connection.cursor(prepared=True)
            cursor.execute(sql_query,self.tupl)
            self.connection.commit()
            #row_num = cursor.rowcount()
            cursor.close()
            print("Cursor instance closed")
            #return row_num
            print("SUCCESS : INSERT operation successful")
        
        except mysql.connector.Error as error:
            print("ERROR : {}".format(error))

        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("MySQL connection is closed")
    
    def update(self):
        """Method to update.More info in README"""
        
        sql_q= "UPDATE cmdb set %s = '%s' where %s = '%s'"% self.tupl
        print("SQL Query: ",sql_q)
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_q)
            self.connection.commit()
            #row_num = cursor.rowcount()
            cursor.close()
            print("Cursor instance closed")
            #return row_num
            print("SUCCESS : UPDATE operation successful")
        
        except mysql.connector.Error as error:
            print("ERROR : {}".format(error))

        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("MySQL connection is closed")
                
    def delete(self):
        """Method to delete.More info in README"""
        
        sql_query = """DELETE from cmdb where hostname = %s"""
        
        try:
            #print(sql_query)
            cursor = self.connection.cursor(prepared=True)
            cursor.execute(sql_query,self.tupl)
            self.connection.commit()
            #row_num = cursor.rowcount()
            cursor.close()
            print("Cursor instance closed")
            #return row_num
            print("SUCCESS : DELETE operation successful")
        
        except mysql.connector.Error as error:
            print("ERROR : {}".format(error))

        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("MySQL connection is closed")        
    
        
        
class Messaging():
    def __init__(self,in_str,conSoc):
        self.in_str = in_str
        self.conSoc = conSoc

    def process(self):
        self.conSoc.send(self.in_str.encode("utf-8"))
        print("\nMessage returned to client")
        

def list_to_json(in_list):
    """
    - Python mysql querry returns 1 list made up of tuples as values.
    - Tuple is converted to dictionary.
    - The dictionary is converted to json object.
    - Return json object for sending through client socket.
    """
    print("\n****List[(tuple)] query result*******\n")
    print(in_list)
    
    try:
        for dict in in_list:
            json_str = json.dumps(dict,indent = 4)
        print("\n****json string query result*******\n")
        print(json_str)
        return json_str
        
    except UnboundLocalError:
        #Catch errors when then list is empty
        print("\n****json string query result*******\n")
        print("ERROR!!Empty results returned")
        json_str = "{ERROR in querry}"
        return json_str
        

    