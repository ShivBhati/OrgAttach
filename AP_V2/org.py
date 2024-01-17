import os
import shutil
import datetime

folder_path = r'B:\Python\org_attacch\Export'# this is the Export folder path
csvpath = r"B:\Python\org_attacch\CSV" #change this
errorfiletomove = r"B:\Python\org_attacch\Error" #change this
sucessfiletomove = r"B:\Python\org_attacch\Sucess"
permanenterror = r"B:\Python\org_attacch\Error\PermanentError"#change this

listerror = os.listdir(errorfiletomove)
for e in listerror:
    if e.endswith(".csv"):
        errorcsvname = r'B:\Invoices\Attachment_Demo\FileNotProcessed.txt'
        modtime = os.path.getmtime(errorcsvname)
        modetimeformated = datetime.datetime.fromtimestamp(modtime)
        current_time = datetime.datetime.now()
        timediff = current_time - modetimeformated
        timediff_minutes = timediff.total_seconds()/60
        if timediff_minutes > 60 and timediff_minutes < 4320 :
            shutil.move(errorcsvname,csvpath)
        elif timediff_minutes > 4320:
            shutil.move(errorcsvname,permanenterror)
    
    
list_dir = os.listdir(folder_path)

for f in list_dir:
    if len(f) > 1:
        commonfilepath = os.path.join(folder_path, f)
        if f == "FileNotProcessed.txt":
            with open(commonfilepath, 'r') as file:
                file_content = file.read()
            os.remove(commonfilepath)
            file_content_split = file_content.split()
            errorfilename_unpath = file_content_split[0] + '.csv'
            errorfilename = os.path.join(csvpath,errorfilename_unpath)
            errorfiletomovename =  os.path.join(errorfiletomove,errorfilename_unpath)
            shutil.move(errorfilename,errorfiletomovename)
        elif f == 'Unprocessed.txt':
            with open(commonfilepath, 'r') as file:
                file_content = file.read()
            os.remove(commonfilepath)
            file_content_split = file_content.split()
            errorfilename_unpath = file_content_split[0]
            errorfilename = os.path.join(csvpath,errorfilename_unpath)
            errorfiletomovename =  os.path.join(errorfiletomove,errorfilename_unpath)
            shutil.move(errorfilename,errorfiletomovename)
        elif f == 'Processed.txt' :
            with open(commonfilepath, 'r') as file:
                file_content = file.read()
            os.remove(commonfilepath)
            file_content_split = file_content.split()
            sucessfilename_unpath = file_content_split[0].replace("FileName","") + '.csv'
            sucessfilename = os.path.join(csvpath,sucessfilename_unpath)
            sucessfiletomovename =  os.path.join(sucessfiletomove,sucessfilename_unpath)
            shutil.move(sucessfilename, sucessfiletomovename)
        else:
            os.remove(commonfilepath)
    else:
        print("you do not have any csv file yet")
# shutil.rmtree(folder_path+"/*") 
    




