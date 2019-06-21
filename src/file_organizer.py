import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import *
import os
import shutil
import pickle

def move_files(list_paths):
    files_dir=list_paths[0]
    dest_dir=list_paths[1]
    dir_files = os.listdir(files_dir)
    files_naming=read_from_file()
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


def write_to_file(temp_dict):
    with open('file_name.txt', 'wb') as file_data_dictionary_file:
        pickle.dump(temp_dict, file_data_dictionary_file)

def show_frame(cont):
    cont.tkraise()


def move_files_func():
    if(len(dir_list)>1 and dir_list[0]!=''):
        move_files(dir_list)
    else:
        messagebox.showinfo("Warning!", "Select From and To Paths")


def read_from_file():
    try:
        with open('file_name.txt', 'rb') as file_data_dictionary_file:
            temp_dict = pickle.load(file_data_dictionary_file)
            index=0
            for field in temp_dict:
                mylist.insert(index,str(field+"         "+temp_dict[field]))
                index=index+1
            return temp_dict
    except:
        file = open('file_name.txt', 'w')
        file.close()
        return {}

def add_exts():
    temp_dict=read_from_file()
    ext=e1.get()
    folder_name=e2.get()
    if(ext==""):
        messagebox.showinfo("Alert!", "Provide an extension")
    elif(folder_name==""):
        messagebox.showinfo("Alert!", "No folder name provided")
    elif(folder_name=="" and ext==""):
        messagebox.showinfo("Alert!", "Fields cannot be empty")
    elif(ext in temp_dict and folder_name==temp_dict[ext]):
        messagebox.showinfo("Alert!", "Extension already Exists give a different folder name to rename it")
    else:
        temp_dict[ext] = folder_name
        write_to_file(temp_dict)
    clean_and_populate(mylist, temp_dict)

def delete_ext():
    temp_dict=read_from_file()
    selected_index=mylist.curselection()
    if(len(selected_index)>0):
        temp_dict.pop(mylist.get(selected_index,None).split(" ")[0],None)
    else:
        pass
    write_to_file(temp_dict)
    clean_and_populate(mylist, temp_dict)

def clean_and_populate(mylist,temp_dict):
    index=0
    mylist.delete(0, 'end')
    for field in temp_dict:
        mylist.insert(index, str(field + "         " + temp_dict[field]))
        index = index + 1


r = tk.Tk()
dir_list=[]
r.title('Fire Organizer')
r.geometry("1200x400")
files_naming = {}

MainFrame=Frame(r,width=1200, height =400)
MainFrame.place(x=1,y=1)
AddextFrame=Frame(r,width=1200, height =400)
AddextFrame.place(x=1,y=1)


scrollbar = Scrollbar(AddextFrame)
scrollbar.place(  x=300,y=100)
mylist = Listbox(AddextFrame, yscrollcommand = scrollbar.set )
mylist.place(x=300,y=100,height=200,width=200)
scrollbar.config( command = mylist.yview )

clean_and_populate(mylist,read_from_file())


initial_path_label=StringVar()
initial_path_label.set('From : ')
initial_path=StringVar()
initial_path.set("Not Yet Selected")
final_path_label=StringVar()
final_path_label.set('To : ')
final_path=StringVar()
final_path.set("Not Yet Selected")

#Main Frame Buttons
initial_dir_button = tk.Button(MainFrame, text='Browse Intital Directory', width=25, command=browse_i_button).place(x=800,y=100)
final_dir_button = tk.Button(MainFrame, text='Browse Final Directory', width=25, command=browse_f_button).place(x=800,y=150)
move_button=tk.Button(MainFrame, text='Move!', width=25, command=move_files_func).place(x=800,y=200)
add_ext_button=tk.Button(MainFrame, text='Add Extensions', width=25, command=lambda: show_frame(AddextFrame)).place(x=800,y=250)
exit_button=tk.Button(MainFrame, text='Exit', width=25, command=r.destroy).place(x=800,y=300)

#Main Frame Fixed labels
ini_lbl = Label(master=MainFrame,textvariable=initial_path_label).place(x=10,y=100)
finail_lbl = Label(master=MainFrame,textvariable=final_path_label).place(x=10,y=150)

#Main Frame Path Labels
ini_path_lbl = Label(master=MainFrame,textvariable=initial_path).place(x=100,y=100)
finail_path_lbl = Label(master=MainFrame,textvariable=final_path).place(x=100,y=150)

#AddextFrame Frame Buttons
add_button=tk.Button(AddextFrame, text='Add ', width=25, command=add_exts).place(x=800,y=150)
delete_button=tk.Button(AddextFrame, text='Delete ', width=25, command=delete_ext).place(x=800,y=200)
back_button=tk.Button(AddextFrame, text='Back ', width=25, command=lambda: show_frame(MainFrame)).place(x=800,y=250)

#AddextFrame Frame Fixed Labels
Label(master=AddextFrame,text="Extension :").place(x=500,y=150)
Label(master=AddextFrame,text="Folder Name :").place(x=500,y=200)


#Entry Field
e1 = tk.Entry(AddextFrame)
e2 = tk.Entry(AddextFrame)
e1.place(x=580,y=150)
e2.place(x=580,y=200)


show_frame(MainFrame)
r.mainloop()
