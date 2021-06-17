from structures import read_data, Song
import tkinter as tk

def gen(name):
    songs = read_data("data.txt")
    for song in songs:
        x = song.search_by_name(name)
        if not(x is None):
            yield x
    while True:
        yield None

def func(get):
    strr = ""
    x = next(get)
    if x is None:
        return None
    for i in x:
        strr = strr + str(i) + ", "
    return strr

prev = ''
get = gen(prev)
def get_name(pressed=None):
    name = entry.get()
    global prev, get
    if not(name == prev):
        get = gen(name)
    getter = func(get)
    if getter is None:
        result["text"] = "Píseň nenalezena"
    else:
        result["text"] = getter
    prev = name

window = tk.Tk()
window.title("CoverSong")
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
entry = tk.Entry(master=frm_entry, width=40)
label = tk.Label(master=frm_entry, text="Zadej Jméno písničky")

entry.grid(row=0, column=0, sticky="e")
label.grid(row=0, column=1, sticky="w")

window.bind('<Return>', get_name)
button = tk.Button(master=window, text="Najdi", command=get_name)

result = tk.Label(master=window, text="")

frm_entry.grid(row=0, column=0, padx=10)
button.grid(row=0, column=1, pady=10)
result.grid(row=0, column=2, padx=10)

window.mainloop()
