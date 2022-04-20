import wolframalpha
client = wolframalpha.Client("8HXT37-UA5YL7W2J3")

import wikipedia

import PySimpleGUI as sg

#Theme
sg.theme('DarkBlue')

layout = [
    [sg.Text("Enter something: "), sg.InputText()],
    [sg.Button("OK"), sg.Button("Cancel")]   ]

# Create the window
window = sg.Window("Jarvis", layout)

# Create an event loop
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try: 
        wiki_res = wikipedia.summary(values[0], sentences=2, auto_suggest=False)
        wolfram_res = next(client.query(values[0]).results).text
        sg.PopupNonBlocking("Wolfram Result: "+wolfram_res, "Wiki Results: "+wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        sg.PopupNonBlocking(wolfram_res)
    except: 
        wiki_res = wikipedia.summary(values[0], sentences=2, auto_suggest=False)
        sg.PopupNonBlocking(wiki_res)
window.close()