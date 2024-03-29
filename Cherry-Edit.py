from tkinter import *
from tkinter import Menu
from tkinter import colorchooser
from tkinter.messagebox import askokcancel
from tkinter.filedialog import askopenfilename, asksaveasfilename
from pathlib import Path
from key_bindings import show_bindings
import os
import subprocess
from functools import cache
from theme_manager import list_available_themes, load_theme_from_file, apply_theme


import re


def highlight_syntax(event=None):
    content = textarea.get("1.0", "end")
    
    # Define syntax keywords
    keywords = ['def', 'if', 'else', 'elif', 'for', 'while', 'import', 'from', 'as', 'return']

    # Highlight keywords
    for keyword in keywords:
        start_index = "1.0"
        while True:
            start_index = textarea.search(keyword, start_index, stopindex=END, nocase=1, regexp=True)
            if not start_index:
                break
            end_index = f"{start_index}+{len(keyword)}c"
            textarea.tag_add('keyword', start_index, end_index)
            start_index = end_index

    # Define syntax patterns for strings and comments
    patterns = [
        (r'(\'\'\'[\s\S]*?\'\'\'|\"\"\"[\s\S]*?\"\"\")|(\"[^\"]*\")|(\'[^\']*\')', 'string'),  # Strings
        (r'#.*', 'comment'),  # Comments
    ]

    # Apply syntax highlighting for strings and comments
    for pattern, tag in patterns:
        for match in re.finditer(pattern, content):
            start_index = "1.0" + str(match.start())
            end_index = "1.0" + str(match.end())
            textarea.tag_add(tag, start_index, end_index)




def on_text_change(event):
    textarea.after(50, highlight_syntax)  # Delay the syntax highlighting to allow the text to update first


@cache
def new():
    # New File Function
    global file
    file = None
    root.title("Untitled - Py Edit")
    textarea.delete(1.0, END)

@cache
def new_shortcut(event):
    # New File Function
    global file
    file = None
    root.title("Untitled - PyEdit")
    textarea.delete(1.0, END)

@cache
def openfile():
    # Open File Function
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[
                           ("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = None

    else:
        textarea.delete(1.0, END)
        root.title(Path(file).name + "- Editor")
        with open(file, 'r') as f:
            textarea.insert(1.0, f.read())

@cache
def openfile_shortcut(event):
    # Open File Function
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[
                           ("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = None

    else:
        textarea.delete(1.0, END)
        root.title(Path(file).name + "- Editor")
        with open(file, 'r') as f:
            textarea.insert(1.0, f.read())

@cache
def savefile():
    # File Save Function
    global file
    if file is None:
        file = asksaveasfilename(defaultextension=".txt", initialfile="Untitled.txt",
                                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None

        else:
            with open(file, 'w') as f:
                f.write(textarea.get(1.0, END))
                root.title(Path(file).name + "- Editor")
    else:
        with open(file, 'w') as f:
            f.write(textarea.get(1.0, END))
            root.title(Path(file).name + "- Editor")

@cache
def savefile_shortcut(event):
    # File Save Function
    global file
    if file is None:
        file = asksaveasfilename(defaultextension=".txt", initialfile="Untitled.txt",
                                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None

        else:
            with open(file, 'w') as f:
                f.write(textarea.get(1.0, END))
                root.title(Path(file).name + "- Editor")
    else:
        with open(file, 'w') as f:
            f.write(textarea.get(1.0, END))
            root.title(Path(file).name + "- Editor")

@cache
def engaged(event):
    # textarea active status change function
    sbar['text'] = "Status : Writing..."

@cache
def free(event):
    # textarea inactive status change function
    sbar['text'] = "Status : Ready..."

@cache
def fullscreen(event):
    root.attributes('-fullscreen', True)

@cache
def reset_win(event):
    root.attributes('-fullscreen', False)

@cache
def dark_theme():
    textarea['bg'] = 'black'
    textarea['fg'] = 'white'
    textarea['insertbackground'] = 'red'
    textarea['cursor'] = 'arrow'
    sbar['bg'] = 'black'
    sbar['fg'] = 'white'

@cache
def light_theme():
    textarea['bg'] = 'white'
    textarea['fg'] = 'black'
    textarea['insertbackground'] = 'white'
    textarea['font'] = f"{font} {size} bold"
    textarea['cursor'] = 'arrow'
    sbar['bg'] = "white"
    sbar['fg'] = "black"

@cache
def cut():
    textarea.event_generate('<<Cut>>')
    sbar['text'] = 'Status : Cut Text Successfully!'

@cache
def copy():
    textarea.event_generate('<<Copy>>')
    sbar['text'] = 'Status : Copied Text Successfully!'

@cache
def paste():
    textarea.event_generate('<<Paste>>')
    sbar['text'] = 'Status : Pasted Text Successfully!'

@cache
def key_cut(event):
    sbar['text'] = 'Status : Cut Text Successfully!'
    textarea.event_generate('<<Cut>>')

@cache
def key_copy(event):
    sbar['text'] = 'Status : Copied Text Successfully!'
    textarea.event_generate('<<Copy>>')

@cache
def key_paste(event):
    sbar['text'] = 'Status : Pasted Text Successfully!'
    textarea.event_generate('<<Paste>>')

@cache
def font_color():
    textarea['fg'] = colorchooser.askcolor(title="Pick Font Color")[1]

@cache
def background():
    textarea['bg'] = colorchooser.askcolor(title="Pick Background Color")[1]

@cache
def cursor_color():
    textarea['insertbackground'] = colorchooser.askcolor(
        title="Pick Cursor Color")[1]

@cache
def sbar_color():
    sbar['bg'] = colorchooser.askcolor(title="Pick Status Bar Color")[1]

@cache
def window_color():
    color = colorchooser.askcolor(title="Pick Window Color")[1]
    root.config(bg=color)

@cache
def about():
    askokcancel("About Editor", "Editor Version: 1.0,\n"
                                "Developer: Andre-Cmd-Rgb.")

@cache
def get_help():
    with open('HELP.md', 'r') as info:
        askokcancel("Information By Editor", info.read())


# Shows all key_bindings from key_bindings module.
@cache
def keybindings():
    show_bindings()


# increases font size from menu.
@cache
def increase_font():
    global size, font
    size += 2
    textarea['font'] = f"{font} {size}"

# Decreases font size from menu.

@cache
def decrease_font():
    global size, font
    size -= 2
    textarea['font'] = f"{font} {size}"

# Increases font size with shortcut.

@cache
def font_inc(event):
    global size, font
    size += 2
    textarea['font'] = f"{font} {size}"

# Decreases font size with shortcut.

@cache
def font_dec(event):
    global size, font
    size -= 2
    textarea['font'] = f"{font} {size}"


# Function makes text bold in textarea.
@cache
def bold(event):
    textarea['font'] += " bold"


# Function makes text italic in textarea.
@cache
def italic(event):
    textarea['font'] += " italic"


# Function underlines text in textarea.
@cache
def underline(event):
    textarea['font'] += " underline"

@cache
def Updater():
    subprocess.Popen("updater.exe")
#def Custom_theme():
#    textarea['bg'] = ins[1]
#    textarea['fg'] = ins[2]
#    textarea['insertbackground'] = ins[3]
#    textarea['font'] = f"{font} {size} bold"
#    textarea['cursor'] = ins[5]
#    sbar['bg'] = ins[6]
#    sbar['fg'] = ins[7]

# Initialization and Customizations...
root = Tk()
size = 18
font = "Helvetica"
file = None
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
root.geometry(f"{width}x{height}")
# You can add any icon that you want!
root.iconbitmap('icon.ico')
root.title("Cherry Edit")

# Tool bar or Menubar...
menubar = Menu(root, bg="black")
filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label='New (Ctrl + N)', command=new)
filemenu.add_command(label='Open (Ctrl + O)', command=openfile)
filemenu.add_separator()
filemenu.add_command(label='Save (Ctrl + S )', command=savefile)
menubar.add_cascade(label='File', menu=filemenu)

editmenu = Menu(menubar, tearoff=False)
editmenu.add_command(label='Cut (Ctrl + X)', command=cut)
editmenu.add_command(label='Copy (Ctrl + C)', command=copy)
editmenu.add_command(label='Paste (Ctrl + V)', command=paste)
editmenu.add_command(label='Increase Font Size ▲', command=increase_font)
editmenu.add_command(label='Decrease Font Size ▼', command=decrease_font)
menubar.add_cascade(label="Edit", menu=editmenu)

colormenu = Menu(menubar, tearoff=False)

# Call the list_available_themes function to get the list of themes
available_themes = list_available_themes()

# Define a callback function for theme selection
def select_theme(theme_name):
    theme_settings = load_theme_from_file(f'themes/{theme_name}.json')
    apply_theme(theme_settings, textarea, sbar)

for theme in available_themes:
    colormenu.add_command(label=theme, command=lambda theme=theme: select_theme(theme))  # Use select_theme
menubar.add_cascade(label="Themes", menu=colormenu)



helpmenu = Menu(menubar, tearoff=False)
helpmenu.add_command(label='About Editor', command=about)
helpmenu.add_command(label='Keyboard Shortcuts', command=keybindings)
helpmenu.add_command(label='Help', command=get_help)
helpmenu.add_command(label='Update', command=Updater)
menubar.add_cascade(label="More...", menu=helpmenu)

# Status Bar
sbar = Label(root, text="Status: Ready...", anchor=W, relief=SUNKEN)
sbar.pack(side=BOTTOM, fill=X)


# Textarea to write...
textarea = Text(root, font=f"{font} {size}")
textarea.pack(fill=BOTH, expand=True, padx=0, pady=0)

# Remove the scrollbar
textarea.config(yscrollcommand=None)  # Disable vertical scrolling
textarea.bind('<KeyRelease>', on_text_change)
# Key Bindings...
textarea.bind('<Control-x>', key_cut)
textarea.bind('<Control-c>', key_copy)
textarea.bind('<Control-v>', key_paste)
textarea.bind('<KeyPress>', engaged)
textarea.bind('<KeyRelease>', free)
textarea.bind('<Control-f>', fullscreen)
textarea.bind('<Control-z>', reset_win)
textarea.bind('<Up>', font_inc)
textarea.bind('<Down>', font_dec)
textarea.bind('<Control-b>', bold)
textarea.bind('<Control-i>', italic)
textarea.bind('<Control-u>', underline)
textarea.bind('<Control-o>', openfile_shortcut)
textarea.bind('<Control-n>', new_shortcut)
textarea.bind('<Control-s>', savefile_shortcut)
textarea.bind('<Key>', highlight_syntax)
textarea.bind('<Button-1>', highlight_syntax)  # Mouse click

select_theme('dark_theme')
# Root Configuration and Mainloop...
root.config(menu=menubar)
root.mainloop()

