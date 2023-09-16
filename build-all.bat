@ echo off
echo compiling...
pyinstaller --noconfirm --onefile --windowed --icon "C:\Users\andre\Documents\GitHub\Cherry-Edit\Assets\icon.ico" --add-data "C:\Users\andre\Documents\GitHub\Cherry-Edit\key_bindings.py;." --add-data "C:\Users\andre\Documents\GitHub\Cherry-Edit\HELP.md;."  "C:\Users\andre\Documents\GitHub\Cherry-Edit\Cherry-Edit.py" "C:\Users\andre\Documents\GitHub\Cherry-Edit\theme_manager.py"
pyinstaller --noconfirm --onefile --console --icon "C:/Users/andre/Documents/GitHub/Cherry-Edit/icon.ico"  "C:/Users/andre/Documents/GitHub/Cherry-Edit/updater.py"
echo Done!