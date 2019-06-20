import os
import shutil
# current_dir=os.path.dirname(os.path.realpath(__file__))
# print(current_dir)
files_dir=r'D:\File Oragniser\File-Organiser\unordered Files'
dest_dir=r'D:\File Oragniser\File-Organiser\Ordered Files'
dir_files=os.listdir(files_dir)
given_file_extensions=['.py','.txt','.docx']
files_naming={}
files_naming[".py"]="python files"
files_naming[".txt"]="text Document"
files_naming["Pdf"]="PDF Files"

for file in dir_files:
    try:
        filename, file_extension = os.path.splitext(file)
        if(file_extension in given_file_extensions):
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
        print(file)


