import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import *
import os
import shutil


def move_files(list_paths):
    files_dir=list_paths[0]
    dest_dir=list_paths[1]
    dir_files = os.listdir(files_dir)
    if dir_files!=[]:
        for file in dir_files:
            try:
                filename, file_extension = os.path.splitext(file)
                if file_extension in files_naming:
                    dirName=dest_dir+"\\"+files_naming[file_extension]
                    if not os.path.exists(dirName):
                        os.mkdir(dirName)
                else:
                    dirName = dest_dir + "\\" + "Other Files"
                    if not os.path.exists(dirName):
                        os.mkdir(dirName)
                if not os.path.exists(dirName+"\\"+file):
                    shutil.move(files_dir +"\\"+file, dirName)
                else:
                    print("File Already exists")
            except:
                messagebox.showinfo("ERROR!","Error in the File Named :: "+file)
        messagebox.showinfo("Success!", "Files moved succesfully")
    else:
        messagebox.showinfo("Alert!","No files to move")

def browse_i_button():
    filename = filedialog.askdirectory()
    initial_path.set(filename)
    if(len(dir_list)>0 and filename!=''):
        dir_list[0]=filename
    elif(len(dir_list)==0):
        dir_list.append(filename)

def browse_f_button():
    filename = filedialog.askdirectory()
    final_path.set(filename)
    if(len(dir_list)==2 and filename!=''):
        dir_list[1]=filename
    elif(len(dir_list)==1):
        dir_list.append(filename)
    elif(len(dir_list)==0):
        dir_list.append('')
        dir_list.append(filename)

def display_path():
    print(dir_list)

def move_files_func():
    if(len(dir_list)>1 and dir_list[0]!=''):
        move_files(dir_list)
    else:
        messagebox.showinfo("Warning!", "Select From and To Paths")

r = tk.Tk()
dir_list=[]
r.title('Fire Organizer')
r.geometry("1200x400")


files_naming={}
files_naming[".py"]="python files"
files_naming[".txt"]="text Document"
files_naming[".pdf"]="PDF Files"
files_naming[".docx"]="Word Documents"
given_file_extensions = ['.py', '.txt', '.docx','.pdf']


initial_path_label=StringVar()
initial_path_label.set('From : ')
initial_path=StringVar()
initial_path.set("Not Yet Selected")
final_path_label=StringVar()
final_path_label.set('To : ')
final_path=StringVar()
final_path.set("Not Yet Selected")


#Buttons
initial_dir_button = tk.Button(r, text='Browse Intital Directory', width=25, command=browse_i_button).place(x=1000,y=100)
final_dir_button = tk.Button(r, text='Browse Final Directory', width=25, command=browse_f_button).place(x=1000,y=150)
move_button=tk.Button(r, text='Move!', width=25, command=move_files_func).place(x=1000,y=200)
exit_button=tk.Button(r, text='Exit', width=25, command=r.destroy).place(x=1000,y=250)

#Fixed labels
ini_lbl = Label(master=r,textvariable=initial_path_label).place(x=10,y=100)
finail_lbl = Label(master=r,textvariable=final_path_label).place(x=10,y=150)

#Path Labels
ini_path_lbl = Label(master=r,textvariable=initial_path).place(x=100,y=100)
finail_path_lbl = Label(master=r,textvariable=final_path).place(x=100,y=150)

r.mainloop()
