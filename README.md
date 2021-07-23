Overview
---------
Code for interacting with Network management MySQL database.
Instead of having clients querrying the DB remotely independently, the DB is only querried by server.
Server script recieves incoming requests from client and based on string identifier, perfoms the querrying and returns results.

1)On the client machines :
- Querry CMDB for device details based on Ip address or Hostname
- Update device details in CMDB
- Add new device in CMDB
- Delete current device in CMDB

2)On the server:
- A script that interracts with CMBD.
- Script uses keywords from incoming client sockets to choose method.
- Script returns feedback to through the created tcp socket.

3) MySQL server has a table called cmdb under MyDB database.

mysql> select * from cmdb;
+------+-----------+----------+------------+----------+------------+--------+
| id   | hostname  | mgt_ip   | serial_num | vendor   | sw_version | region |
+------+-----------+----------+------------+----------+------------+--------+
|    1 | z-nsw-r01 | 10.1.1.1 | sn232323   | cisco    | 16.09.1b   | nsw    |
|    2 | z-vic-r01 | 10.2.2.2 | sn121212   | aruba    | 7.04.1b    | vic    |
|    3 | z-wa-r01  | 10.3.3.3 | sn454545   | fortinet | 19.07.4c   | wa     |
|    5 | z-sa-r01  | 10.4.4.4 | sn333333   | f5       | 17.45.6c   | sa     |
+------+-----------+----------+------------+----------+------------+--------+
4 rows in set (0.00 sec)

Functions/Methods
-----------------
For the client<> server connection :
  - socket() module has been used on both server and client side to create a TCP socket.
  - bind() and listen() methods used in server side and connect() method used on client side.

For the server <>MySQL server connection:
  - https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
  - https://pynative.com/python-mysql-database-connection/ 
  - MySQL connector python API module has been used.
  - connect() method of mysql.connector() class used to create Mysql DB Server <> main server connection.
  - connection.cursor() method to create a cursor object which creates a new MySQLCursor object.
  - cursor.execute() method to execute the SQL changes.
  - cursor.commit() to make DB changes persistent.
  - cursor.close() & connection.close() methods to close open connections.

Issues
-----------
- MySQLCursorDic creates a cursor that returns rows as dictionaries not as tuples.It's invoked with 
  (dictionary=True). Default is (dictionary=False)
- For select() and update() methods, Prepared statement object,cursor= connection.cursor(prepare=True),
  was return errors for update() and empty string for select().
- Seems like the ' ' were not being added to the variables in the end sql command.
- I chose to create the comple sql query statement earlier before parsing it into the cursor.execute() method.

Further improvements
--------------------
- Building of unittest code for both client end and server end.
- Introduce multithreading on server side to accomodate more than 1 parallel client querries.
- Introduce GUI on client side and remove terminal.

Author
------
A.M