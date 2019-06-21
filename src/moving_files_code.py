import shutil
import os


def sourcePath():
    source = input("Enter source path by copying path as text\n")
    if not len(source) >= 3:
        print("Source path must have atleast 3 characters\neg: if the path is D drive, enter 'D:\\'\n:)\n")
        return sourcePath()
    if not os.path.exists(source):
        print("Invalid source path!!")
        return sourcePath()

    return source


def destPath():
    created = False
    dest = input("Enter destination path by copying path as text if the path exists, manually if not\n")
    if not len(dest) >= 3:
        print("Destination path must have atleast 3 characters\neg: if the path is D drive, enter 'D:\\'\n:)\n")
        return destPath()
    if not os.path.exists(dest[:3]):
        print("Invalid destination path!!")
        return destPath()
    if not os.path.exists(dest):
        os.makedirs(dest)
        created = True
    return (dest, created)


def fileExtension():
    ext = input("Enter file type (extension) of those files to be moved\n(include the dot also)\n")
    return ext


def srcDest():
    src = sourcePath()
    dC = destPath()
    dest = dC[0]
    destCreated = dC[1]
    if src + '\\' == dest or src == dest or src == dest + '\\':
        print("The source and destination cannot be the same\n")
        return srcDest()
    else:
        return (src, dest, destCreated)


def movingFiles():
    srcDestCreated = srcDest()
    source = srcDestCreated[0]
    destination = srcDestCreated[1]
    destCreated = srcDestCreated[2]
    extension = fileExtension()
    files_list = list(os.listdir(source))
    count = 0
    for _ in files_list:
        if _.endswith(extension):
            count += 1
            print("Moving ...\n")
            shutil.move(source + "/" + _, destination)
            print("Moved " + _ + " from " + source + " to " + destination + " \n")
    if count == 0:
        if destCreated:
            os.rmdir(destination)
        print("No files found with the given extension\nChoose an option\n1.Retry\n2.Exit")
        opt = int(input())
        if opt == 1:
            movingFiles()
        else:
            exit()
    else:
        print("The files have been moved successfully!!\n1.Move some other files\n2.Exit")
        opt = input()
        if opt == '1':
            movingFiles()
        else:
            exit()


movingFiles()