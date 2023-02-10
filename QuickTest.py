import os

def main():
    # Find Microsoft Office directory
    drives = os.popen("wmic logicaldisk get name").read().split()
    for drive in drives:
        if(os.path.isdir(f"""{drive}\\Program Files\\Microsoft Office\\root\\Office16""") == True):
            source = f"""{drive}\\Program Files\\Microsoft Office\\root\\Office16"""
            break
    else:
        print("Microsoft Office not found!")
        return
    
    # Open Excel 2016
    os.startfile(f"{source}\\EXCEL.EXE")

if __name__ == "__main__":
    main()
