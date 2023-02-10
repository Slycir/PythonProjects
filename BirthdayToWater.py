from datetime import datetime
from tkinter import *
import webbrowser
import math

millnames = ['',' thousand',' million',' billion',' trillion']

def millify(n):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

def main():
    root=Tk()
    m=mainWindow(root)
    root.mainloop()
    
class popupWindow(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.master=master
        self.lMonth=Label(top,text="Enter your month of birth (Jan=1, Feb=2...)")
        self.lMonth.pack()
        self.eMonth=Entry(top)
        self.eMonth.insert(0, "12")
        self.eMonth.pack()
        self.lDay=Label(top,text="Enter your day of birth")
        self.lDay.pack()
        self.eDay=Entry(top)
        self.eDay.insert(0, "31")
        self.eDay.pack()
        self.lYear=Label(top,text="Enter your year of birth")
        self.lYear.pack()
        self.eYear=Entry(top)
        self.eYear.insert(0, "1999")
        self.eYear.pack()
        self.b2=Button(top,text="Calculate",state="normal",command=lambda: self.cleanup())
        self.b2.pack()
    def cleanup(self):
        self.eYearValue=self.eYear.get()
        self.eMonthValue=self.eMonth.get()
        self.eDayValue=self.eDay.get()
        self.top.destroy()

class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.lLived=Label(master,text=("2 quadrillion gallons of water are used annually for agriculture."))
        self.lLived.pack()
        self.lGallons=Label(master,text=("Let's put that into perspective."))
        self.lGallons.pack()
        self.lYear=Label(master,text="")
        self.lYear.pack()
        self.b=Button(master,text="Let's go!",state="normal",command=lambda: self.popup())
        self.b.pack()
        self.bLearn=Button(master,text="Learn more",state="disabled",command=lambda: webbrowser.open("https://www.wired.com/2006/03/farms-waste-much-of-worlds-water/"))
        self.bLearn.pack()

    def popup(self):
        self.w=popupWindow(self.master)
        self.b["state"] = "disabled" 
        self.master.wait_window(self.w.top)
        self.update()
        self.b["state"] = "normal"

    def update(self):
        gallons = 2 * 10**15
        year = int(self.w.eYearValue)
        month = int(self.w.eMonthValue)
        day = int(self.w.eDayValue)
        birthday = datetime(year, month, day)
        now = datetime.now()
        age = now - birthday
        
        years = year + int(gallons / 60 / 60 / 24 / 365)
        months = month + (int((gallons / 60 / 60 / 24 / 365) * 12) % 12)
        days = day + int((gallons / 60 / 60 / 24) % 30)

        if days > 30:
            days = days - 30
            months = months + 1

        if months > 12:
            months = months - 12
            years = years + 1

        self.lLived.config(text=(f"You have lived for about {millify(age.total_seconds())} seconds.") )
        self.lGallons.config(text=(f"Drinking a gallon of water a second, you would have to live {millify(gallons / age.total_seconds())} times as long to drink the water used in agriculture annually.") )
        self.lYear.config(text=(f"In other words, you would have to live until {months}/{days}, {millify(years)} years in the future."))
        self.b.config(text="Try again")
        self.bLearn.config(state="normal")

main()