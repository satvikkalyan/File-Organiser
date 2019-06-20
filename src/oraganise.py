import os

current_dir=os.getcwd()
dir_files=os.listdir(current_dir)[1:]
given_file_extensions=['.py','.txt','.docx']
files_naming={}
files_naming[".py"]="python files"
files_naming[".txt"]="text Document"
files_naming["Pdf"]="PDF Files"
for file in dir_files:

    filename, file_extension = os.path.splitext(file)
    print("File Name :: "+filename+"\nFile Extension :: "+file_extension)



