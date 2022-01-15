# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 11:08:26 2022

@author: vikas
"""
import sys
import subprocess
try:
    import ctypes  # An included library with Python install. 
    import pandas as pd
    from tabulate import TableFormat, tabulate
    import numpy as np
    import pandas as pd
    import tkinter
    from tkinter import *
    from tkinter import ttk
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    print("Opps required dependencies not found Trying to install them please")
    listr=["lxml","pandas","numpy","tk","tabulate"]
    # implement pip as a subprocess to install the requirded dependenices
    for i in listr:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install',
        i])
# The webpage URL whose table we want to extract
url = "https://prsindia.org/covid-19/cases"

def view():
    try:
        table=pd.read_csv(r"hello.csv")
        df=pd.DataFrame(table)
    except:
        ctypes.windll.user32.MessageBoxW(0,"No Data found please Connec internet to download Case's Data", "Info", 0)
    finally:
        f=df.drop(['Unnamed: 0', '#'], axis = 1)
        f['Active Percentage']=(f['Active Cases']/f['Confirmed Cases'])*100
        f['Recovery Percentage']=(f['Cured/Discharged']/f['Confirmed Cases'])*100
        f['Death Percentage']=(f['Death']/f['Confirmed Cases'])*100
        xf=['State/UT','Total Cases','active','recovered','deaths','Active Percentage','Recovery Percentage','Death Percentage']
        f.at[7,'State/UT']='D and N Havel'
        f=f.round(2)
        f.to_csv('data.csv')
        #creating root window of gui pop up
        root=Tk()
        root.title("Covid-19 state Wise Data")
        root.geometry(f'{900}x{700}+{280}+{80}')

        #Frame for treeview
        mframe=Frame(root)
        mframe.pack(pady=(2,25))

        #creating a treeview which is used to create tabular data
        myt=ttk.Treeview(mframe,height=100)
        dft=pd.read_csv('data.csv', index_col=0)  #Reading the data file from a CSV

        #Adding the data of cloumns from CSV to Treeview frame
        myt["column"]=list(dft.columns)
        myt["show"]="headings"
        for column in myt["column"]:
            myt.heading(column,text=column)
            myt.column(column,minwidth=0, width=110, stretch=YES)

        #Adding the data of rows from CSV to Treeview frame
        dft_rows=dft.to_numpy().tolist()
        for row in dft_rows:
            myt.insert("","end",values=row)

        myt.pack(pady=15)
        # creating ok  button frame
        okf=Frame(root)
        okf.place(height=30,width=110,rely=.95,relx=.87)
        btn = Button(okf, text = '  ok  ', bd = '5', command = root.destroy)
        btn.place(rely=.62,relx=.3)
        btn.pack()
        
        root.mainloop()
        f=f.drop(f.index[36])
        x=f['State/UT']
        t=f['Confirmed Cases']/50
        a=f['Active Cases']
        r=f['Cured/Discharged']/50
        d=f['Death']
        ap=f['Active Percentage']
        rp=f['Recovery Percentage']
        dp=f['Death Percentage']
        y=[x,t,a,r,d]
        yx=[x,ap,rp,dp]
        zf=pd.DataFrame(y)
        y=zf.T
        zf=pd.DataFrame(yx)
        yx=zf.T
        graph=input("do you want Graphical Reprsentaion Y/N= ")
        if graph=='y' or graph=='Y':
              
            ctypes.windll.user32.MessageBoxW(0, """To better Display the Graph Confirmed 
and recovered cases are divided by 50""", "Info", 0)
            y.plot(x='State/UT',kind='bar',stacked=False,title='Total Cases V/S Deaths V/S Recovey V/S Active',color=['red','blue','green','black'],figsize=(15,8))
            plt.tight_layout()
            plt.show()
            yx.plot(x='State/UT',kind='bar',stacked=False,title='Active V\S Recovery V\S Death Percentage',color=['red','blue','green','black'],figsize=(15,8))
            plt.tight_layout()
            plt.show()
