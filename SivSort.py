import os
from tkinter import Tk, filedialog
import datetime
import pathlib
from pathlib import Path
import shutil

print("By Wojtekb30, 03.10.2022, program version 1.0")
print("This program was created as a gift for Siv. It sorts jpg, png, mp4 and zip files to folders depending on first word of filename. The separator is '-'.")
input("First let's choose the folder files to sort are in. \nPress ENTER/RETURN to continue. ")
root = Tk() 
root.withdraw() 

root.attributes('-topmost', True)
# folder path
dir_path = filedialog.askdirectory()
print("Chosen: "+str(dir_path))

input("\nNow let's choose the destination folder (folder in which subfolders to sort to are or should be). \nPress ENTER/RETURN to continue. ")
dir_path_destination = filedialog.askdirectory()
print("Chosen: "+str(dir_path_destination))

print("\nType '1' to create new folders if necessary. Type anything else if not:")
rodzajsort = input()
print("Are you sure to start?")
input("Press ENTER/RETURN to start. ")

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
        

n=0
while n<len(res):
    rozszerzenie = pathlib.Path(dir_path+"/"+res[n]).suffix
    #print(str(res[n]))
    print("-------")
    print("Now processing "+str(dir_path+'/'+res[n])+"\n")
    if (("-" in str(res[n])) and (str(rozszerzenie).lower()==".jpg" or str(rozszerzenie).lower()==".png" or str(rozszerzenie).lower()==".mp4" or str(rozszerzenie).lower()==".zip")):
        sciezka = Path(dir_path_destination+"/"+str(res[n]).partition("-")[0])
        #print(sciezka)
        
        if str(rodzajsort)=="1":
            os.makedirs(sciezka, exist_ok = True)
        if sciezka.is_dir():
            try:
                shutil.move(dir_path+"/"+res[n], sciezka)
                print("File moved.")
            except:
                print("Error! File of such name already exists there (probably).\n")
    else:
        print("File skipped.\n")
    print("The iteration number "+str(n+1)+" of "+str(len(res))+" done.\n")
    n=n+1
print("Done")
input("Press ENTER/RETURN to end. ")
