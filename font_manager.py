# font_manager.py

import os
import tkinter.font as tkFont

def load_custom_font(font_folder, font_filename, font_size):
    font_path = os.path.join(font_folder, font_filename)
    custom_font = tkFont.Font(family=font_filename, size=font_size)
    custom_font.actual()
    custom_font.configure(family=custom_font.actual()["family"])
    return custom_font
    
def list_available_fonts(font_folder):
    return [filename for filename in os.listdir(font_folder) if filename.endswith(".ttf")]
