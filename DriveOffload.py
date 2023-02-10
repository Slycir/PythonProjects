import os
import shutil
import tkinter as tk

# -------------- IMPORTANT STUFF --------------

# database_path = "C:\\Users\\timot\\python\\Scouting Stuff\\all_matches"
database_path = "C:\\Users\\theop\\OneDrive\\Desktop\\scouting_database"

# locates the path of flash drive
def get_drive_path() -> str:
    # gets all drives on device
    drives = os.popen("wmic logicaldisk get name").read().split()

    for drive in drives:
        if(os.path.isdir(f"{drive}\\Matches") == True):
            return f"{drive}\\Matches"

def check_directory(team_num: str) -> str:
    folder_path = database_path + "\\" + team_num
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def read_drive() -> None:
    drive_path = get_drive_path()
    drive_dir = os.listdir(drive_path)
    # loop through all files on drive
    for path in drive_dir:
        team_num = get_team_num(path)
        # get place to copy from and where to copy to
        copy_source = drive_path + "\\" + path
        copy_destination = check_directory(team_num) + "\\" + path

        if os.path.exists(copy_destination): continue

        shutil.copyfile(copy_source, copy_destination)

# finds the team number in file name and returns it
def get_team_num(file_name: str) -> str:
    start_id = file_name.find("T")
    end_id = file_name.find("-", start_id)
    team_num = file_name[start_id + 1:end_id]
    return team_num

# --------------- TKINTER STUFF --------------

root = tk.Tk()

def initialize_tk_window() -> None:
    root.title = "Drive Offloader"
    root.geometry("300x300")

    text = tk.Label(root, text="Do you have the drive plugged in?")
    text.pack()

    button = tk.Button(
                        root, text="YES", command=read_drive, 
                        height=10, width=30,
                        bg="#afb7c4"
                       )
    button.pack()

    root.mainloop()


def main(): 
    initialize_tk_window()

if __name__ == "__main__":
    main()