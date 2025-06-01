# filename: test_sg.py
import PySimpleGUI as sg

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]
window = sg.Window("Test Window", layout)

event, values = window.read()
window.close()

print("PySimpleGUI test successful!")
