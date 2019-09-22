import tkinter
import tkinter.font

window=tkinter.Tk()
window.title("PYTHON")
window.geometry("640x400+100+100")
window.resizable(True, True)

font=tkinter.font.Font(family="맑은 고딕", size=20, slant="italic")

label=tkinter.Label(window, text="파이썬 3.7", font=font)
label.pack()

window.mainloop()
