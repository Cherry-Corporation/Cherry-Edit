import wget
#define update url
url='https://github.com/Andre-cmd-rgb/Py-Edit/releases/download/1.1/main.exe'
#define Updater
def Updater():
    filename = wget.download(url)
    os.remove("main.exe")
    os.rename('main (1).exe', 'main.exe')
    os.system(exit)
    
