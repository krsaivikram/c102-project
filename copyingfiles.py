import os
import shutil
source = input("type the source folder file")
destination = input("type the destination folder file")
source = source+"/"
destination = destination+"/"
createlist = os.listdir(source)
for i in createlist:
    shutil.copy((source+i),destination)

