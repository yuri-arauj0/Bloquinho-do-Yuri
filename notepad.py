import PySimpleGUI as sg
import pathlib

WIN_W = 90
WIN_H = 25

#sg.theme('Kayak')
sg.theme('BrightColors')

menu_layout = [ #layout do menu
    ['File', ['New (Ctrl+N)', 'Open (Ctrl+O)', 'Save (Ctrl+S)', 'Save As', '---', 'Exit']],
    ['Tools', ['Word Count']],
    ['Help', ['About']],
]

layout = [ #layout da janela
    [sg.Menu(menu_layout)],
    [sg.Text('New file', font=('Consolas', 10), size=(WIN_W, 1), key='_INFO_')],
    [sg.Multiline(font=('Consolas', 12), size=(WIN_W, WIN_H), key='_BODY_')]
]

# sg.Window('titulo na barra', layout, redimensionar, >>>finalizar<<<muito importante)
window = sg.Window('Bloquinho do Yu', layout=layout, resizable=True, finalize=True, margins=(0, 0), grab_anywhere=False)
#window.maximize()
window['_BODY_'].expand(expand_x=True, expand_y=True)

def new_file():
    #Reset body and info bar, and clear filename variable
    window['_BODY_'].update(value='')
    window['_INFO_'].update(value='> New File <')
    file = None
    return file

def open_file():
    #Open file and update the infobar
    filename = sg.popup_get_file('Open', no_window=True)
    if filename:
        file = pathlib.Path(filename)
        window['_BODY_'].update(value=file.read_text())
        window['_INFO_'].update(value=file.absolute())
        return file

def save_file(file):
    #Save file instantly if already open; otherwise use `save-as` popup
    if file:
        file.write_text(values.get('_BODY_'))
    else:
        save_file_as()

def save_file_as():
    #Save new file or save existing file with another name
    filename = sg.popup_get_file('Save As', save_as=True, no_window=True)
    if filename:
        file = pathlib.Path(filename)
        file.write_text(values.get('_BODY_'))
        window['_INFO_'].update(value=file.absolute())
        return file

def word_count():
    #Display estimated word count
    words = [w for w in values['_BODY_'].split(' ') if w!='\n']
    word_count = len(words)
    sg.popup_no_wait('Word Count: {:,d}'.format(word_count))

def about_me():
    #A short, pithy quote
    sg.popup_no_wait('"The universe doesn\'t allow perfection." - Stephen Hawking', keep_on_top=True)

while True:
    event, values = window.read()

    if event in('Exit', None):
        break

    if event in ('New (Ctrl+N)', 'n:78'):
        file = new_file()

    if event in ('Open (Ctrl+O)', 'o:79'):
        file = open_file()

    if event in ('Save (Ctrl+S)', 's:83'):
        save_file(file)

    if event in ('Save As',):
        file = save_file_as()   

    if event in ('Word Count',):
        word_count() 
        
    if event in ('About',):
        about_me()
