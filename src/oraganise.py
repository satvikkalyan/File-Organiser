import os
import shutil

files_naming={}
files_naming[".py"]="python files"
files_naming[".txt"]="text Document"
files_naming[".pdf"]="PDF Files"
files_naming[".docx"]="Word Documents"
given_file_extensions = ['.py', '.txt', '.docx','.pdf']

def print_names():
    print(files_naming)

def move_files(list_paths):
    files_dir=list_paths[0]
    dest_dir=list_paths[1]
    dir_files = os.listdir(files_dir)
    for file in dir_files:
        try:
            filename, file_extension = os.path.splitext(file)
            if(file_extension in files_naming):
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
            print("Error in the File Named :: "+file)


