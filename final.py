# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 09:05:34 2022

@author: vikas
"""
import sys
import subprocess
import ctypes 
def final():
    try:
        import matplotlib
        import tkinter
        import lxml
        from tabulate import tabulate
        import pandas as pd
    except ModuleNotFoundError: #this will check that all the dependcies are present if any dependciy is missing it will install it
        er="Opps required dependencies not found Trying to install them please connect to internet"
        ctypes.windll.user32.MessageBoxW(0,er,"error",0)
        listr=["lxml","pandas","numpy","tk","tabulate","matplotlib"]
        # implement pip as a subprocess to install the requirded dependenices
        for i in listr:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install',i])
        final()
    try:
        # Assign the table data to a Pandas dataframe
        url = "https://prsindia.org/covid-19/cases"
        table = pd.read_html(url)[0]      # Assign the url data to a Pandas dataframe 
        table.to_csv('hello.csv')
        import datetime
        now = datetime.datetime.now() #this will take todays date and store it in a txt file
        pr=now.strftime("%d %B %Y")
        file1 = open("date.txt", "w") 
        file1.write(pr)
        file1.close() 
    except:
        try:
            table=pd.read_csv(r"hello.csv")
            file1 = open("date.txt", "r") #this will open the txt file containing the date
            notc="""System not connected to internet using old Saved offline data:
    from Date :"""+file1.read() #this will read the contents from the txt file
            ctypes.windll.user32.MessageBoxW(0,notc , "Info", 0) #this will show a pop up with an information
            file1.close() 
        except:
            error="No Data found please Connect internet to download Case's Data"
            ctypes.windll.user32.MessageBoxW(0,error , "Error", 0) #this will show a pop up with an error
            exit()
    import ald,indi,summary
    a=int(input("""India covid-19 Cases Data:
    Enter One For Summary of Data:
    Two for state wise list:
    Three for Individual States:
    And press 0 for exit=  :"""))
    print('---------------------------------------------------------')
    while a in range(1,5):
        if a==2:
            ald.view()
            print('---------------------------------------------------------')
        if a==1:
            summary.view()
            print('---------------------------------------------------------')
        if a==3:
            indi.state()
            print('---------------------------------------------------------')
        
        a=int(input("""India covid-19 Cases Data:
    Enter One For Summary of Data:
    Two for state wise list:
    Three for Individual States:
    And press 0 for exit=  :"""))
        print('---------------------------------------------------------')
    if a==0:
        exit()
final()
