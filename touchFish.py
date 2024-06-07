import tkinter as tk
import tkinter.font as tkFont
from tkinter import Text,INSERT,END,filedialog
import os
import chardet

def on_drag(event):
    root.geometry(f"+{event.x_root - 170}+{event.y_root - 170}")

def on_close(event):
    root.destroy()

def getFileEncoding(path:str):
    with open(path,'rb') as f:
        text = f.read()
    fileEncoding = chardet.detect(text)['encoding']
    return fileEncoding

root = tk.Tk()
textContent = ''

options = {"initialdir": os.getcwd(), "title": "请选择一个文件",'filetypes':[('文本文件','.txt')]}
file_path = filedialog.askopenfilename(**options)
if file_path:
    with open(file=file_path,mode='r',encoding=getFileEncoding(file_path)) as f:
        textContent = f.read()

root.overrideredirect(True)

mainFont = tkFont.Font(family='宋体', size=16, weight=tkFont.NORMAL, slant=tkFont.ROMAN, underline=0, overstrike=0)

text = Text(root,font=mainFont,	height=8,width=30,spacing1=19,spacing2=19,relief=None,bg='white',fg='black',borderwidth=0)
text.insert(END, textContent)
text.pack()

# 监听鼠标拖动事件
text.bind("<B3-Motion>", on_drag)

# 监听鼠标关闭事件
root.bind("<Escape>", on_close)

root.attributes('-topmost', True)
root.mainloop()
