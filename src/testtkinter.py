from src import oraganise
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import *


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
        oraganise.move_files(dir_list)
    else:
        messagebox.showinfo("Warning!", "Select From and To Paths")
    # oraganise.print_names()

r = tk.Tk()
dir_list=[]
r.title('Fire Organizer')
r.geometry("1200x400")

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
# print_paths=tk.Button(r, text='Display', width=25, command=display_path).place(x=1000,y=200)
move_button=tk.Button(r, text='Move!', width=25, command=move_files_func).place(x=1000,y=200)
exit_button=tk.Button(r, text='Exit', width=25, command=r.destroy).place(x=1000,y=250)

#Fixed labels
ini_lbl = Label(master=r,textvariable=initial_path_label).place(x=10,y=100)
finail_lbl = Label(master=r,textvariable=final_path_label).place(x=10,y=150)

#Path Labels
ini_path_lbl = Label(master=r,textvariable=initial_path).place(x=100,y=100)
finail_path_lbl = Label(master=r,textvariable=final_path).place(x=100,y=150)

r.mainloop()
