import os
import datetime 

errorcsvname = r'B:\Invoices\Attachment_Demo\FileNotProcessed.txt'
modtime = os.path.getmtime(errorcsvname)
modetimeformated = datetime.datetime.fromtimestamp(modtime)
current_time = datetime.datetime.now()
timediff = current_time - modetimeformated

# Convert timediff to minutes
timediff_minutes = timediff.total_seconds()/60

print(modetimeformated)
print(current_time)
print(timediff_minutes)