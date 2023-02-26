import os
import shutil
from time import sleep
from datetime import datetime
from tkinter import *
from pandas import read_excel

# Find user's home directory
home = os.path.expanduser("~")
# Find user's desktop directory OneDrive or Desktop
if os.path.isdir(f"{home}\\OneDrive\\Desktop") == True:
    desktop = f"{home}\\OneDrive\\Desktop"
else:
    desktop = f"{home}\\Desktop"
# Find Scouting directory or quit if it doesn't exist
if os.path.isdir(f"{desktop}\\Scouting") == False:
    print("Scouting directory not found! Please run the installer and try again. If the problem persists, please contact the Scouting Leads.")
    exit()
scouting = f"{desktop}\\Scouting"


def main():

    # Open Save File window
    root = Tk()
    r=runningWindow(root)
    root.title("Saving...")
    root.attributes("-topmost", True)
    root.mainloop()


    # Find Excel 2016
    drives = os.popen("wmic logicaldisk get name").read().split()
    for drive in drives:
        if(os.path.isdir(f"{drive}\\Program Files\\Microsoft Office\\root\\Office16") == True):
            source = f"{drive}\\Program Files\\Microsoft Office\\root\\Office16"
            break
        elif(os.path.isdir(f"{drive}\\Program Files (x86)\\Microsoft Office\\Office16") == True):
            source = f"{drive}\\Program Files (x86)\\Microsoft Office\\Office16"
            break
    else:
        print("Excel 2016 not found!")
        return

    # Close Excel 2016
    os.system("taskkill /im EXCEL.EXE")

    # Open Save File window
    root = Tk()
    rtp=mainWindow(root)
    root.title("Save File")
    root.attributes("-topmost", True)
    root.mainloop()


def filesave(team):

    # Find removable matches drive
    drives = os.popen("wmic logicaldisk get name").read().split()
    for drive in drives:
        if(os.path.isdir(f"{drive}\\Pits") == True):
            matches = f"{drive}\\Pits"
            break
    else:
        root = Tk()
        nf=notFoundWindow(root)
        root.title("Error")
        root.attributes("-topmost", True)
        root.mainloop()
        return

    shutil.copyfile(f"{scouting}\\EDIT_Pit_Scouting.xlsm", f"{matches}\\PIT-T{team}-({datetime.now().strftime('%m-%d-%y')}).xlsm")
    shutil.copyfile(f"{scouting}\\BLANK_Pit_Scouting.xlsm", f"{scouting}\\EDIT_Pit_Scouting.xlsm")

class mainWindow(object):
    def __init__(self,master):

        # Find Team # and Match # w/ Pandas
        while True:
            try:
                df = read_excel(f"{scouting}\\EDIT_Pit_Scouting.xlsm", header=None)
                break
            except:
                sleep(.5)
        team = df.iloc[2,1]
        # Close Pandas
        del df

        self.master=master
        self.lTeam=Label(master,text=("Enter your team number: "))
        self.lTeam.pack()
        self.eTeam=Entry(master)
        self.eTeam.insert(0,team)
        self.eTeam.pack()
        self.b=Button(master,text="Save",state="normal",command=lambda: self.cleanup())
        self.b.pack()
    
    def cleanup(self):
        team = self.eTeam.get()
        filesave(team)
        self.master.destroy()

class runningWindow(object):
    def __init__(self,master):
        self.master=master
        self.l=Label(master,text="Saving...")
        self.l.pack()
        self.lRemembers=Label(master,text="Ensure that the file is saved and that the matches drive is inserted. \nIf the matches drive is not inserted, the file will not be saved.")
        self.lRemembers.pack()
        self.b=Button(master,text="Ready",command=lambda: self.cleanup())
        self.b.pack()
        self.bCancel=Button(master,text="Cancel",command=lambda: self.cancel())
        self.bCancel.pack()

    def cleanup(self):
        self.master.destroy()
    
    def cancel(self):
        os.system("taskkill /f /im python.exe")
        self.master.destroy()

class notFoundWindow(object):
    def __init__(self,master):
        self.master=master
        self.l=Label(master,text="Error: Matches drive not found! Please insert the matches drive and try again. \nIf the problem persists, please contact the Scouting Leads.")
        self.l.pack()
        self.b=Button(master,text="Close",command=lambda: self.cleanup())

    def cleanup(self):
        self.master.destroy()

if __name__ == "__main__":
    main()

