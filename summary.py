try:
    import pandas as pd
    from tabulate import TableFormat, tabulate
    import matplotlib.pyplot as plt
    import ctypes
    import tkinter
    from tkinter import *
    from tkinter import ttk
except ModuleNotFoundError:
    import sys
    import subprocess
    print("Opps required dependencies not found Trying to install them please")
    listr=["lxml","pandas","numpy","tk","tabulate"]
    # implement pip as a subprocess to install the requirded dependenices
    for i in listr:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install',
        i])

def view():
    try:
        table=pd.read_csv(r"hello.csv")
        df=pd.DataFrame(table)
    except:
        print("No Data found please Connect internet to download Case's Data")
        exit()
    finally:
        f=df.drop(['Unnamed: 0', '#'], axis = 1)
        f['Active Percentage']=((f['Active Cases']/f['Confirmed Cases'])*100).round(2)
        f['Recovery Rate']=((f['Cured/Discharged']/f['Confirmed Cases'])*100).round(2)
        f['Death Percentage']=((f['Death']/f['Confirmed Cases'])*100).round(2)
        g=f[f['State/UT']=='India']
        g.round(2)
        sd=g.T
        sd=sd.rename(columns={36:"Cases/Rate"})
        sd["Data"]=sd.index
        sd=sd.drop(index='State/UT')
        sd=sd[["Data","Cases/Rate"]]
        f.at[7,'State/UT']='D and N Havel'
        xl=["State/UT","Active Case's","Confirmed Case's","Recovery","Death","Active Percentage","Recovery Rate","Death Rate"]
        fd=f.drop(['State/UT'], axis = 1)
        fd=fd.drop(f.index[36])
        mi = fd.idxmin()
        ma = fd.idxmax()
        lcs=f.iat[mi[0],0]  #Confirmed state
        lcc=f.iat[mi[0],1]  #Confirmed
        las=f.iat[mi[1],0]  #Active state
        lac=f.iat[mi[1],2]  #Active
        lds=f.iat[mi[3],0]  #Death state
        ldc=f.iat[mi[3],4]  #Death
        laps=f.iat[mi[4],0] #active Percntage state
        lapc=f.iat[mi[4],5] #Active percentage case's
        lrrs=f.iat[mi[5],0] #recovery rate state
        lrrc=f.iat[mi[5],6] #recovery rate case's
        ldrs=f.iat[mi[6],0] #death Rate state
        ldrc=f.iat[mi[6],7] #death rate case's
        #Highest case start from here
        hcs=f.iat[ma[0],0]  #Confirmed
        hcc=f.iat[ma[0],1]  #Confirmed
        has=f.iat[ma[1],0]  #Active
        hac=f.iat[ma[1],2]  #Active
        hds=f.iat[ma[3],0]  #Deatt
        hdc=f.iat[ma[3],4]  #Deatt
        haps=f.iat[ma[4],0] #active Percntage
        hapc=f.iat[ma[4],5] #
        hrrs=f.iat[ma[5],0]
        hrrc=f.iat[ma[5],6]
        hdrs=f.iat[ma[6],0]
        hdrc=f.iat[ma[6],7]
        lowest={"Lowest":["Active Case's","Confirmed Case's","Death","Active Percentage","Recovery Rate","Death Rate"],
            "State":[las,lcs,lds,laps,lrrs,ldrs],
            "Case's":[lac,lcc,ldc,lapc,lrrc,ldrc],
            }
        highest={"Higest":["Active Case's","Confirmed Case's","Death","Active Percentage","Recovery Rate","Death Rate"],
            "State":[has,hcs,hds,haps,hrrs,hdrs],
            "Case's":[hac,hcc,hdc,hapc,hrrc,hdrc],
            }
        highest=pd.DataFrame(highest)
        lowest=pd.DataFrame(lowest)
        def pop(popd,popt):
            #creating root window of gui pop up
            root=Tk()
            root.title(popt)
            root.geometry(f'{350}x{250}+{280}+{80}')

            #Frame for treeview
            mframe=Frame(root)
            mframe.pack(pady=(2,25))

            #creating a treeview which is used to create tabular data
            myt=ttk.Treeview(mframe,height=100)
            # popd=pd.read_csv('data.csv', index_col=0)  #Reading the data file from a CSV
            roh=ttk.Style()
            roh.configure('Treeview', rowheight=25)
            #Adding the data of cloumns from CSV to Treeview frame
            myt["column"]=list(popd.columns)
            myt["show"]="headings"
            for column in myt["column"]:
                myt.heading(column,text=column)
                myt.column(column,minwidth=0, width=110, stretch=NO)

            #Adding the data of rows from CSV to Treeview frame
            popd_rows=popd.to_numpy().tolist()
            for row in popd_rows:
                myt.insert("","end",values=row)

            myt.pack(pady=15)
            # creating ok  button frame
            okf=Frame(root)
            okf.place(height=30,width=110,rely=.85,relx=.7)
            btn = Button(okf, text = '  ok  ', bd = '5', command = root.destroy)
            btn.place(rely=.62,relx=.3)
            btn.pack()
            
            root.mainloop()
        
        # print(tabulate(sd,tablefmt='grid'))
        pop(sd,"India Covid-19 Case's Summary")
        xf=["Lowest","State","Case's"]
        pop(lowest.round(2),"Lowest case's")
        highestp=tabulate(highest,xf,tablefmt='grid')
        pop(highest.round(2),"Higest Case's")
        
