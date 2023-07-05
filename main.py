from tkinter import *
from tkinter import filedialog

def open_file():
    file_name = filedialog.askopenfilename(initialdir="/",title="Select file",filetypes=(("txt files","*.txt"),("all files","*.*")))
    f = open(file_name,"r")
    data = f.read()
    f.close()
    text_box.delete("1.0",END)
    text_box.insert(END,data)

def save_file():
    file_name = filedialog.asksaveasfilename(initialdir="/",title="Select file",filetypes=(("txt files","*.txt"),("all files","*.*")))
    f = open(file_name,"w")
    data = text_box.get("1.0",END)
    f.write(data)
    f.close()

def new_file():
    text_box.delete("1.0",END)

root = Tk()
root.title("Text Editor")
root.geometry("500x500")
root.resizable(False, False)
root.config(bg="black")

# Menu bar containing file: create, open, save and exit
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New File", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
root.config(menu=menubar)

# Text box
text_box = Text(root, bg="black", fg="white", font=("Courier", 12))
text_box.pack(expand=True, fill=BOTH)

root.mainloop()
