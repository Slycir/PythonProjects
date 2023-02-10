import os
import shutil
from time import sleep
from datetime import datetime
from tkinter import *
from pynput.keyboard import Key, Controller

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

    keyboard = Controller()
    
    # Find Excel 2016
    drives = os.popen("wmic logicaldisk get name").read().split()
    for drive in drives:
        if(os.path.isdir(f"{drive}\\Program Files\\Microsoft Office\\root\\Office16") == True):
            source = f"{drive}\\Program Files\\Microsoft Office\\root\\Office16"
            break
    else:
        print("Excel 2016 not found!")
        return
    
    # Focus Excel 2016
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt)
    sleep(.5)

    # Save file
    keyboard.press(Key.ctrl)
    keyboard.press('s')
    keyboard.release('s')
    keyboard.release(Key.ctrl)
    sleep(1.5)

    # Close Excel 2016
    keyboard.press(Key.alt)
    keyboard.press(Key.f4)
    keyboard.release(Key.f4)
    keyboard.release(Key.alt)

    # Open Save File window
    root = Tk()
    m=mainWindow(root)
    root.title("Save File")
    root.attributes("-topmost", True)
    root.mainloop()
    
    # Open Excel 2016
    os.system(f"\"{scouting}\\EDIT_Match_Scouting.xlsm\"")

def filesave(team,match):

    # Find removable matches drive
    drives = os.popen("wmic logicaldisk get name").read().split()
    for drive in drives:
        if(os.path.isdir(f"{drive}\\Matches") == True):
            matches = f"{drive}\\Matches"
            break
    else:
        print("Matches drive not found! Please insert the matches drive and try again. If the problem persists, please contact the Scouting Leads.")
        return

    shutil.copyfile(f"{scouting}\\EDIT_Match_Scouting.xlsm", f"{matches}\\M{match}-T{team}-({datetime.now().strftime('%m-%d-%y')}).xlsm")
    shutil.copyfile(f"{scouting}\\BLANK_Match_Scouting.xlsm", f"{scouting}\\EDIT_Match_Scouting.xlsm")

class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.lTeam=Label(master,text=("Enter your team number: "))
        self.lTeam.pack()
        self.eTeam=Entry(master)
        self.eTeam.pack()
        self.lMatch=Label(master,text=("Enter your match number: "))
        self.lMatch.pack()
        self.eMatch=Entry(master)
        self.eMatch.pack()
        self.b=Button(master,text="Save",state="normal",command=lambda: self.cleanup())
        self.b.pack()
    
    def cleanup(self):
        team = self.eTeam.get()
        match = self.eMatch.get()
        filesave(team,match)
        self.master.destroy()

if __name__ == "__main__":
    main()

