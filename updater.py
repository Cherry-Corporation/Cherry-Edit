import wget
import os
#define update url
url='https://github.com/Cherry-Corporation/Cherry-Edit/releases/download/0.9/Cherry-Edit.exe'
#define Updater
def Updater():
    os.remove("Cherry-Edit.exe")
    filename = wget.download(url)
    os.system(exit)
Updater()
