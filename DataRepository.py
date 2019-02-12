''' 
    Author: Vladimir Heredia
    Class: CS521
    Date: 06/19/2018
    Assignment: 
    Description:
'''
import datetime as dt
from datetime import datetime, date

class DataRepository:
    ''' This class will access and store the data to the DB '''
    def __init__(self, conn):
        self.__conn = conn

    def getAllReadings(self):
        ''' Gets all of the readings from the DB '''
        with self.__conn:
            data = self.__conn.execute('select * from glucose')
            return data.fetchall()

    def getLastSevenDays(self):
        ''' Gets the last 7 days of data '''
            seven_days_ago =datetime.now() + dt.timedelta(-7)
            cmd = "select * from glucose where date between '{}' and '{}'"
                  .format(seven_days_ago.date(), datetime.now().date())
            data = self.__conn.execute(cmd )
            return data.fetchall()

    def getLastFourteenDays(self):
        ''' Gets the last 14 days of data '''
            fourteen_days_ago =datetime.now() + dt.timedelta(-14)
            cmd = "select * from glucose where date between '{}' and '{}'"
            .format(fourteen_days_ago.date(), datetime.now().date())
            data = self.__conn.execute(cmd )
            return data.fetchall()

    def getLastThirtyDays(self):
        ''' Gets the last 30 days of data '''
            thirty_days_ago =datetime.now() + dt.timedelta(-30)
            cmd = "select * from glucose where date between '{}' and '{}'"
            .format(thirty_days_ago.date(), datetime.now().date())
            data = self.__conn.execute(cmd )
            return data.fetchall()

    def getLastNinetyDays(self):
        ''' Gets the last 30 days of data '''
            ninety_days_ago =datetime.now() + dt.timedelta(-90)
            cmd = "select * from glucose where date between '{}' and '{}'"
            .format(ninety_days_ago.date(), datetime.now().date())
            data = self.__conn.execute(cmd )
            return data.fetchall()


    def saveGlucose(self, glucose):
        ''' Save Glucose object to database '''
        with self.__conn:
            self.__conn.execute('''insert into glucose 
                                (reading,date,event,notes)
                                values(?, ?, ?, ?)''', 
                                (glucose.getReading(),
                                glucose.getReadingDate(),
                                glucose.getEvent(),
                                glucose.getNotes()))
            self.__conn.commit()

    


    def seedDatabase(self):
        ''' Adds initial data to glucose table '''
        # add initial data
        readings = [
            (87, str(7 - datetime.now()), 'Before Meal', 'I feel ok today' ),
            (165, str(7 - datetime.now()), 'After Meal', 'Had a big meal' ),
            (135, str(7 - datetime.now()), 'After Meal', 'Had less food today' ),
            (230, str(datetime.now()), 'After Meal', 'Ate too much food today' ),
            (75, str(datetime.now()), 'Before Meal', 'I feel shaky' )
            ]
        with self.__conn:
            self.__conn.executemany(
                    'insert into Glucose(reading, date, event, notes) \
                     values (?, ?, ?, ?)', readings)
          
       