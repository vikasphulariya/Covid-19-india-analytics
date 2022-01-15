try:
    import pandas as pd
    from tabulate import TableFormat, tabulate
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    import sys
    import subprocess
    print("Opps required dependencies not found Trying to install them please")
    listr=["lxml","pandas","numpy","tk","tabulate"]
    # implement pip as a subprocess to install the requirded dependenices
    for i in listr:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install',
        i])

def state():
    try:
        table=pd.read_csv(r"hello.csv")
        df=pd.DataFrame(table)
    except:
        print("No Data found please Connect internet to download Case's Data")
    finally:
        f=df.drop(['Unnamed: 0', '#'], axis = 1)
        f=f.drop(f.index[36])
        state=input('State name:')
        g=f[f['State/UT']==state]
        f=g.T
        xf=['Total Cases','active','recovered','deaths']
        x=g.iat[0,0]
        print(tabulate(f,tablefmt='grid'))
        t=g.iat[0,1]
        a=g.iat[0,2]
        r=g.iat[0,3]
        d=g.iat[0,4]
        y=[t,a,r,d]
        graph=input("do you want Graphical Reprsentaion Y/N= ")
        if graph=='y' or graph=='Y':
            plt.bar(xf,y,color=['red','blue','green','black'])
            plt.title(state)
            plt.show()