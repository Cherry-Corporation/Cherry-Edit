@ echo off
echo compiling...
pyinstaller --noconfirm --onefile --windowed --icon "C:\Users\andre\Documents\GitHub\Cherry-Edit\Assets\icon.ico" --add-data "C:\Users\andre\Documents\GitHub\Cherry-Edit\key_bindings.py;." --add-data "C:\Users\andre\Documents\GitHub\Cherry-Edit\HELP.md;."  "C:\Users\andre\Documents\GitHub\Cherry-Edit\Cherry-Edit.py"
echo Done!