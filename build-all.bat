@ echo off
echo compiling...
pyinstaller --noconfirm --onefile --windowed --icon "C:\Users\andre\Documents\Coding Projects\Python\Cherry-Edit\Assets\icon.ico" --add-data "C:\Users\andre\Documents\Coding Projects\Python\Cherry-Edit\key_bindings.py;." --add-data "C:\Users\andre\Documents\Coding Projects\Python\Cherry-Edit\HELP.md;."  "C:\Users\andre\Documents\Coding Projects\Python\Cherry-Edit\Cherry-Edit.py" "C:\Users\andre\Documents\Coding Projects\Python\Cherry-Edit\theme_manager.py"
pyinstaller --noconfirm --onefile --console --icon "C:\Users\andre\Documents\Coding Projects\Python\Cherry-Edit\icon.ico"  "C:\Users\andre\Documents\Coding Projects\Python\Cherry-Edit\updater.py"

echo Done!
pause