import os
import puremagic
import ffmpeg



icon = """
____ _  _ ___  ____ ____    ____ _ _  _ ___  _    ____    ____ ____ _  _ _  _ ____ ____ ___ ____ ____ 
[__  |  | |__] |___ |__/    [__  | |\/| |__] |    |___    |    |  | |\ | |  | |___ |__/  |  |___ |__/ 
___] |__| |    |___ |  \    ___] | |  | |    |___ |___    |___ |__| | \|  \/  |___ |  \  |  |___ |  \ 
                                                                                                      """










def refresher():
    try:
        os.system("cls");
    except:
        os.system("clear");

print(icon)

extension = [];
fileList = [];
for file in os.listdir():
    try:
        ext = puremagic.magic_file(f"{os.getcwd()}\{file}");
        fileExten = ext[0][2]
        if("video" in ext[0][3] or "audio" in ext[0][3]):
            extension.append(fileExten);
            fileList.append(file)
        else:
            continue;
    except:
        continue

mainAsk = input("\tWhat would you like to convert?\n\n1. Convert all files of the same type\n2. Convert specific files\n\nEnter:");
if(mainAsk == "1"):
    refresher()
    #
    print("\n\tNOTE:\tA file can sometimes end in a different file-extension than it actually is. The files listed below have correct extensions.")
    #
    for exten in list(set(extension)):
        print(f"\nFiles of type: {exten}:");
        for file in fileList:
            if(puremagic.magic_file(f"{os.getcwd()}\\{file}")[0][2]) == exten:
                print(f"\t{file}")
            else:
                continue;
        print("\n")
    counter = 1;
    print(f"{'_'*50}\n")
    for ex in list(set(extension)):
        print(f"{counter}{ex}")
        counter +=1;




      ##
elif(mainAsk == "2"):
    refresher()
    counter = 1;
    print("List of all video & audio files:");
    for file in fileList:
        print(f"\t{counter}. {file}\n");
        counter +=1;
    selectionOfFiles = input("\nEnter the number associated with the file(s) you wish to convert.\n(Seperate by commas if you wish to convert more than one.)\nEnter:\t")
    if(selectionOfFiles):
        selectionOfFilesIndexes = selectionOfFiles.split(",");
        selectionOfFilesFinal = [];
        for index in selectionOfFilesIndexes:
            try:
                item_index = int(index.strip());
                selectionOfFilesFinal.append(fileList[item_index-1]);
            except(ValueError, IndexError):
                break;
        refresher()
        print("You've selected the following file(s):")
        counter = 1;
        for item in selectionOfFilesFinal:
            print(f"{counter}. {item}")
            counter +=1;
        ##
    changeType = input("What format would you like these files to be converted to?\n(ex, mp4, mp3, mkv, avi)\nEnter:\t");
    for selection in selectionOfFilesFinal:
        newFile = selection.rfind(".");
        if(newFile != -1):
            newerFile = selection[:newFile];
        else:
            newerFile = selection;
        ffmpeg.input(f"{os.getcwd()}\\{selection}").output(f"{newerFile}.{changeType}", speed=8).run();








secondAsk = int(input("\n\tWhich numbered options above?\nEnter:\t"));
if(secondAsk <= len(extension)-1):
    refresher();
    print(f"You entered {secondAsk}, which means you've selected the files with the type of {extension[secondAsk - 1]}\n");
    changeType = input("What format would you like these files to be converted to?\n\t(ex, mp4, mp3, mkv, avi)\nEnter:\t");
    for file in fileList:
        newFile = file.rfind(".");
        if(newFile != -1):
            newerFile = file[:newFile];
        else:
            newerFile = file;
        if(puremagic.magic_file(f"{os.getcwd()}\\{file}")[0][2]) == (extension[secondAsk -1]):
           ffmpeg.input(f"{os.getcwd()}\\{file}").output(f"{newerFile}.{changeType}", speed=8).run();

        