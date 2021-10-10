import shutil
import os
from zipfile import ZipFile


path = "C:/Users/RUDRA/Downloads/Brave Download/"
dest = "C:/Users/RUDRA/Desktop/instagram/post/"
files = os.listdir(path)
filename = "C:/Users/RUDRA/Desktop/instagram/post/Files_airmore_20210503_114454.zip"
for a in files:
    if a.endswith(".zip") and a.startswith("Files_airmore"):
        shutil.move(os.path.join(path, a), os.path.join(dest, a))
        filename = os.path.join(dest, a)


print(filename)
with ZipFile(filename, "r") as zipObj:
    print(zipObj)
    # Extract all the contents of zip file in current directory
    zipObj.extractall(dest)

for imgs in os.listdir(dest):
    if imgs.startswith("Instander"):
        instander = os.path.join(dest, "Instander")
        for i in os.listdir(instander):
            shutil.move(os.path.join(instander, i), os.path.join(dest, i))

for a in os.listdir(dest):
    if a.endswith(".zip") and a.startswith("Files_airmore"):
        os.remove(os.path.join(dest, a))
        os.rmdir(instander)
