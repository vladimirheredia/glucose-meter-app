''' 
    Author: Vladimir Heredia
    Class: CS521
    Date: 06/18/2018
    Assignment: Final Project
    Description: Meter Class
'''

from Glucose import Glucose
from datetime import datetime, date
from DatabaseConnection import DatabaseConnection
from DataRepository import DataRepository
import math
from tkinter import *
from tkinter import messagebox

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')


def graph_data(conn):
    ''' Graphing data '''
    c = conn.connect()

    repo = DataRepository(c)
    #repo.seedDatabase()
    #repo.saveGlucose(glucose)

    readings = repo.getAllReadings()
    dates = []
    values = []
    for row in readings:
        dates.append(datetime.strptime(row[1],  "%Y-%m-%d %H:%M:%S.%f"))
        values.append(row[0])

    plt.plot_date(dates, values, '-')
    # beautify the x-labels
    plt.gcf().autofmt_xdate()
    myFmt = mdates.DateFormatter('%x')
    plt.gca().xaxis.set_major_formatter(myFmt)
    plt.show()


if __name__ == '__main__':

   
    
    # Ask user for glucose reading
    int_read = 0

    # Create the database connection
    conn = DatabaseConnection('glucosedb.sqlite')
    c = conn.connect()

    # Instantiage DataRepository object
    repo = DataRepository(c)

    # To create UI
    window = Tk()
    window.configure(background = '#319997')
    window.title('Glucose Monitor App')
    window.wm_iconbitmap('images/glucose.ico')

    # main image
    img_title = tk.PhotoImage(file='images/main_img.png')
    w = Label(window, image=img_title).grid(row=0, columnspan=20)

    # img to add to button
    img = tk.PhotoImage(file='images/glucometer.png')
  
    # create form
    txtReading = StringVar()
    lblReading = Label(window, text = 'Glucose reading:')
    entReading = Entry(window, textvariable=txtReading, width=7)

    lblReading.grid(row = 1, column = 0,sticky=W)
    entReading.grid(row = 1, column = 1, sticky=W, padx=2)
    lblReading.configure(background = '#319997', 
                         font=('Century Gothic',12),
                         foreground = 'white')

    # add combobox
    tkvar = StringVar()
    choices = {'Before meal', 'After Meal', 'Before Excercise', 'After Excercise'}
    tkvar.set('Before Meal')

    lblEvent = Label(window, text = 'Choose event:')
    lblEvent.grid(row = 2, column = 0, sticky=W)
    lblEvent.configure(background = '#319997', 
                       font=('Century Gothic',12),
                       foreground='white')

    evtdropDown = OptionMenu(window, tkvar, *choices)
    evtdropDown.grid(row =2, column =1, pady=5)
    evtdropDown.configure(width=13)

    def eventDropDown(*args):
        global strEvent
        strEvent = tkvar.get()


    tkvar.trace('w', eventDropDown)

    # label for comments property
    lblNotes = Label(window, text='Comments:')
    lblNotes.grid(row = 3, column = 0, sticky=W)
    lblNotes.configure(background = '#319997', 
                       font=('Century Gothic',12),
                       foreground='white')

    # Textbox for comments
    txtNotes = Text(window)
    txtNotes.grid(row=3, column=1,pady=5)
    txtNotes.configure(width=14, height=3, padx=5)

    ttk.Separator(orient='horizontal').grid(column = 0, 
                                            row =4, 
                                            columnspan=20, 
                                            sticky="ew")

    cmbChoice = StringVar()
    intChoices = {1:'Today', 2:'7 Days', 3:'14 Days', 4:'30 Days', 5:'3 Months'}
    cmbChoice.set('Today')

    # label for intervals property
    lblInterval = Label(window, text='Choose interval:')
    lblInterval.grid(row = 5, column = 0, sticky=W)
    lblInterval.configure(background = '#319997', 
                       font=('Century Gothic',12),
                       foreground='white')

    intdropDown = OptionMenu(window, cmbChoice, *intChoices.values())
    intdropDown.grid(row =5, column =1, pady=5)
    intdropDown.configure(width=13)

    # label for comments property
    lblRange = Label(window, text='Range (70 - 150):')
    lblRange.grid(row = 6, column = 0, sticky=W)
    lblRange.configure(background = '#319997', 
                       font=('Century Gothic',12),
                       foreground='white')

    # label for comments property
    lblRangeResult = Label(window, text='0')
    lblRangeResult.grid(row = 6, column = 1, sticky=W)
    lblRangeResult.configure(background = '#319997', 
                       font=('Century Gothic',12),
                       foreground='white')

    # label for range property
    lblA1c = Label(window, text='A1c (4.0% - 6.0%):')
    lblA1c.grid(row = 7, column = 0, sticky=W)
    lblA1c.configure(background = '#319997', 
                       font=('Century Gothic',12),
                       foreground='white')

    # label for range result property
    lblA1cResult = Label(window, text='0')
    lblA1cResult.grid(row = 7, column = 1, sticky=W)
    lblA1cResult.configure(background = '#319997', 
                       font=('Century Gothic',12),
                       foreground='white')


    # label for range result img property
    lblA1cResultImg = Label(window, text='')
    lblA1cResultImg.grid(row = 7, column = 2, sticky=W)
    lblA1cResultImg.configure(background = '#319997',)

    def intervalDropDown(*args):
        ''' Event triggered on interval dropdown '''
        # Formula: A1c = (46.7 + average_blood_glucose) / 28.7
        #print('Reading Avg. for the day is: ', math.floor(sum(row[0] for row in readings) / len(readings)))
        global cmbInterval
        cmbInterval = cmbChoice.get()
        if cmbInterval == 'Today':
            '''something'''
        elif cmbInterval == '7 Days':
            '''something'''
        elif cmbInterval == '14 Days':
            '''something'''
        elif cmbInterval == '30 Days':
            '''something'''
        elif cmbInterval == '3 Months':
            '''something'''

    cmbChoice.trace('w', intervalDropDown)

    def saveGlucose():
        ''' This method runs on the button click event'''
        print('button was clicked!')
        try:
            int_read = int(txtReading.get())
            entReading.configure(background = '#FFFFFF')

            # Create glucose object
            glucose = Glucose(int_read, datetime.now(), strEvent, txtNotes.get("1.0","end-1c"))

            # Save to DB
            repo.saveGlucose(glucose)

        except:
            entReading.configure(background = '#FFB2B2')
            messagebox.showwarning('Warning', 
                'Reading must be an integer. Please try again!')
       
        

        entReading.delete(0, END)
        txtNotes.delete("1.0","end-1c")

        
        
       

    # Button to submit the glucose reading to the DB
    btn = Button(window, text='Save', command=saveGlucose, image = img)
    btn.grid(row= 3, column = 19, padx=5, pady=5)

    # Chart button info
    def getChart():
        '''Get's chart information'''
        graph_data(conn)

    chart_img = tk.PhotoImage(file='images/chart.png')
    btnChart = Button(window, text='Chart', command=getChart, image=chart_img)
    btnChart.grid(row=8, column=18)
    # Exit application
    def exitApp():
        exit()

    exit_img = tk.PhotoImage(file='images/exit.png')
    btnExit = Button(window, text='Exit', command=exitApp, image=exit_img)
    btnExit.grid(row=8, column=19, padx=5, pady=5)

    window.mainloop()

    
    
    

