from pathlib import Path

import PySimpleGUI as sg
import pandas as pd


sg.theme('DarkTeal9')

current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
EXCEL_FILE = current_dir / 'Origin.xlsx'
df = pd.read_excel(EXCEL_FILE)

layout = [
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('Date', size=(15,2)),            sg.InputText(key='Date'),
    sg.CalendarButton("Select Date", close_when_date_chosen=True, target="Date", format='%d:%m:%Y', size=(10,1))],
    [sg.Text('Supplier Name', size=(15,2)), sg.InputText(key='Supplier Name')],
    [sg.Text('Supplier Code', size=(15,2)), sg.InputText(key='Supplier Code')],
    [sg.Text('Vessel No', size=(15,2)), sg.InputText(key='Vessel No')],
    [sg.Text('Vessel Name', size=(15,2)), sg.InputText(key='Vessel Name')],
    [sg.Text('Vehicle No', size=(15,2)), sg.InputText(key='Vehicle No')],

    [sg.Text('Name of Jetty', size=(15,2)), sg.InputText(key='Name of Jetty')],
    [sg.Text('Fish Type', size=(15,2)), sg.Combo(['OS', 'MK', 'Other'], key='Fish Type')],
    
    [sg.Text('No. of bags', size=(15,2)), sg.Spin([i for i in range(0,16)],
                                                       initial_value=0, key='No. of bags')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

window = sg.Window('Omega Ltd', layout)

def clear_input():
    for key in values:
        window[key]('')
    return None


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        new_record = pd.DataFrame(values, index=[0])
        df = pd.concat([df, new_record], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data saved!')
        clear_input()
window.close()










#Indranil.Co
