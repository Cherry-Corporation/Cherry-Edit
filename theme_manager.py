import json
import os
import glob

def load_theme_from_file(theme_file):
    try:
        with open(theme_file, 'r') as theme_file:
            theme_settings = json.load(theme_file)
            return theme_settings
    except FileNotFoundError:
        return None

def apply_theme(theme_settings, textarea, sbar):
    if theme_settings:
        # Apply general theme settings
        textarea['bg'] = theme_settings.get('bg_color', '')
        textarea['fg'] = theme_settings.get('text_color', '')
        textarea['insertbackground'] = theme_settings.get('cursor_color', '')
        sbar['bg'] = theme_settings.get('status_bar_color', '')
        sbar['fg'] = theme_settings.get('status_bar_text_color', '')

        # Apply text highlighting colors
        textarea.tag_configure('keyword', foreground=theme_settings.get('keyword_color', ''))
        textarea.tag_configure('string', foreground=theme_settings.get('string_color', ''))
        textarea.tag_configure('comment', foreground=theme_settings.get('comment_color', ''))

def list_available_themes():
    theme_files = glob.glob('themes/*.json')
    return [os.path.basename(file).replace('.json', '') for file in theme_files]
