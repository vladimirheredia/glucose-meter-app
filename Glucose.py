''' 
    Author: Vladimir Heredia
    Class: CS521
    Date: 06/18/2018
    Assignment: Final Project
    Description: Glocose class
'''

class Glucose:
    ''' Creates Glucose Objects '''
    def __init__(self, glucoseReading, readingDate, event, notes ):
        self.__glucoseReading = glucoseReading
        self.__readingDate = readingDate
        self.__event = event
        self.__notes = notes


    def setReading(self, reading):
        ''' Sets the glucose reading '''
        self.__glucoseReading = reading

    def getReading(self):
        ''' Gets the glucose reading '''
        return self.__glucoseReading

    def setReadingDate(self, readingDate):
        ''' Sets glucose reading date '''
        self.__readingDate = readingDate

    def getReadingDate(self):
        ''' Gets glucose reading date'''
        return self.__readingDate

    def setEvent(self, event):
        ''' Sets the event property '''
        self.__event = event
    
    def getEvent(self):
        ''' Gets the event property '''
        return self.__event

    def setNotes(self, notes):
        ''' Sets the notes property '''
        self.__notes = notes

    def getNotes(self):
        ''' Gets the notes property '''
        return self.__notes