import tkinter as tk
import os

ttl = ["SearchX"]

user = "Iland"
path1 = "C:\\Users\\" + user + "\\Desktop\\"
path2 = "C:\\Users\\Public\\Desktop\\"

buttons = []

root = tk.Tk()
root.title(ttl[0])

canvas = tk.Canvas(root, width=400, height=200)
canvas.pack(side="top", anchor="nw", expand=False, fill="x")

canvas2 = tk.Canvas(root, width=400, height=600)
canvas2.pack(side="top", anchor="nw", expand=True, fill="both")

searchInput = tk.Entry(root, width=40)
canvas.create_window(200, 100, window=searchInput)

Text = tk.Label(root, text="Search:")
canvas.create_window(200, 80, window=Text)

SearchBt = tk.Button(width=30, text="Search", command=lambda: search(searchInput.get()))
canvas.create_window(200, 125, window=SearchBt)

root.mainloop()


def osStartfile(buttonPath):
    os.startfile(buttonPath)


def search(Input):

    canvas2.delete("all")

    buttons.clear()
    fileNames = []
    files = []

    for r, d, f in os.walk(path1):
        for file in f:
            if Input.lower() in file.lower():
                files.append(os.path.join(r, file))

    for r, d, f in os.walk(path2):
        for file in f:
            if Input.lower() in file.lower():
                files.append(os.path.join(r, file))

    for filePath in files:
        fileName = filePath.split("\\")[-1].split(".")[0]
        fileNames.append(fileName)

    if not fileNames:
        noResults = tk.Label(root, text="No results")
        canvas2.create_window(200, 20, window=noResults)
    else:
        for name in fileNames:
            btn = tk.Button(
                root,
                text=name,
                command=lambda: osStartfile(files[fileNames.index(name)]),
            )
            buttons.append(btn)

    for button in buttons:
        canvas2.create_window(200, 20 + (buttons.index(button) * 30), window=button)
