''' 
    Author: Vladimir Heredia
    Class: CS521
    Date: 06/18/2018
    Assignment: Final Project
    Description: This class is used to create a connection to the DB
'''

import sqlite3

class DatabaseConnection:
    ''' Used to create db and manipulate data '''
    def __init__(self, file_name):
        self.__file_name = file_name

    def connect(self):
        ''' Create database connection
            and return connection & cursor '''
        conn = sqlite3.connect(self.__file_name)

        # return both
        return conn

    def close(self, conn):
        ''' Close connection '''
        conn.close()

    def create_table(self):
        ''' Creates table if it doesn't exist'''
        conn = self.connect()
        conn.execute('create table if not exists \
            glucose(reading integer, date text, event text, notes text)')
        
