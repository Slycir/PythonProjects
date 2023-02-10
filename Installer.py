import os
import shutil

def main():
    print("Installing Scouting Sheets...")
    # Find user's home directory
    home = os.path.expanduser("~")
    # Find user's desktop directory
    if os.path.isdir(f"{home}\\OneDrive\\Desktop") == True:
        desktop = f"{home}\\OneDrive\\Desktop"
    else:
        desktop = f"{home}\\Desktop"

    # Find removable install drive
    print("Finding install drive...")
    drives = os.popen("wmic logicaldisk get name").read().split()
    for drive in drives:
        if(os.path.isdir(f"{drive}\\Install") == True):
            source = f"{drive}\\Install"
            print(f"Install drive found: {drive}")
            break
    else:
        print("Install drive not found!")
        return



    # Create a directory in Desktop called "Scouting"
    if(os.path.isdir(f"{desktop}\\Scouting") == False):
        print("Creating directory...")
        os.mkdir(f"{desktop}\\Scouting")
        print("Directory created!")

    print("Copying files...")
    shutil.copyfile(f"{source}\\EDIT_Match_Scouting.xlsm", f"{desktop}\\Scouting\\EDIT_Match_Scouting.xlsm")
    shutil.copyfile(f"{source}\\BLANK_Match_Scouting.xlsm", f"{desktop}\\Scouting\\BLANK_Match_Scouting.xlsm")
    print("Files copied!")

    print("Copying executable...")
    shutil.copyfile(f"{source}\\SheetSave.exe", f"{desktop}\\SheetSave.exe")
    print("Executable copied!")

    print("Installation complete!")

if __name__ == "__main__":
    main()

