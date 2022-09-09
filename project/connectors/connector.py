import mysql.connector
from format import *

def dbconnect (  ) :
    '''
    establish a connection with remote  MySQL database (of e-commerce website)
    uses mysql.connector module
    :return: connection instance (  mysql.connector.connect() )
    '''

    hostname = '----'
    username = '----'
    password = '-----'
    database = '-----'


    try:
        myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
        printf2("connected successfully ")
        return myConnection

    except Exception as accesserror:
        printf2("Error while connecting to MySQL", accesserror)
        raise ValueError('No Mysql')





