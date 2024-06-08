import tkinter as tk
from tkinter import Text,END,filedialog
import os,chardet,datetime

def getFileEncoding(path:str):
    with open(path,'rb') as f:
        text = f.read()
    fileEncoding = chardet.detect(text)['encoding']
    return fileEncoding

def on_drag(event):
    # 拖动窗口
    root.geometry(f"+{event.x_root - 170}+{event.y_root - 170}")

def on_close(event):
    # 关闭窗口，同时把文本框中的文本保存下来
    if not os.path.exists(os.path.join(os.getcwd(),'记录')):
        os.mkdir(os.path.join(os.getcwd(),'记录'))
    filename = os.path.join(os.getcwd(),'记录',datetime.datetime.now().strftime("%Y年%m月%d日%H-%M-%S-%f")+'.txt')
    with open(file=filename,mode='w',encoding='utf-8') as f:
        f.write(text.get('1.0',END))
    root.destroy()

# 修改字体大小
def increase_font_size(event=None):
    current_size = text.cget("font").split(" ")[1]
    size = int(current_size)
    text.config(font=('宋体', str(size + 1)))
 
def decrease_font_size(event=None):
    current_size = text.cget("font").split(" ")[1]
    size = int(current_size)
    text.config(font=('宋体', str(max(size - 1, 1))))

# 修改窗口宽度
def increase_width(event=None):
    current_width = text.cget("width")
    width = int(current_width)
    text.config(width=width + 1)
 
def decrease_width(event=None):
    current_width = text.cget("width")
    width = int(current_width)
    text.config(width=max(width - 1, 1))

# 修改窗口高度
def increase_height(event=None):
    current_height = text.cget("height")
    height = int(current_height)
    text.config(height=height + 1)
 
def decrease_height(event=None):
    current_height = text.cget("height")
    height = int(current_height)
    text.config(height=max(height - 1, 1))

# 修改行间距
def increase_spacing(event=None):
    current_spacing1 = text.cget("spacing1")
    spacing1 = int(current_spacing1)
    text.config(spacing1=spacing1 + 1)

    current_spacing2 = text.cget("spacing2")
    spacing2 = int(current_spacing2)
    text.config(spacing2=spacing2 + 1)
 
def decrease_spacing(event=None):
    current_spacing1 = text.cget("spacing1")
    spacing1 = int(current_spacing1)
    text.config(spacing1=max(spacing1 - 1, 1))

    current_spacing2 = text.cget("spacing2")
    spacing2 = int(current_spacing2)
    text.config(spacing2=max(spacing2 - 1, 1))

root = tk.Tk()
textContent = ''

options = {"initialdir": os.getcwd(), "title": "请选择一个txt文件",'filetypes':[('文本文件','.txt')]}
file_path = filedialog.askopenfilename(**options)
if file_path:
    with open(file=file_path,mode='r',encoding=getFileEncoding(file_path)) as f:
        textContent = f.read()

root.overrideredirect(True)

text = Text(root,font=('宋体', 16),	height=8,width=30,spacing1=19,spacing2=19,relief=None,bg='white',fg='black',borderwidth=0)
text.insert(END, textContent)
text.pack()

# 快捷键：
# 右键：拖动窗口
# ESC：关闭窗口
# Ctrl +：增大字体
# Ctrl -：减小字体
# Ctrl 0：扩大宽度
# Ctrl 9：减小宽度
# Alt +：增大高度
# Alt -：减小高度
# Ctrl Alt +：增大行间距
# Ctrl Alt -：减小行间距
text.bind("<B3-Motion>", on_drag)
root.bind("<Escape>", on_close)
root.bind("<Control-equal>", increase_font_size)
root.bind("<Control-minus>", decrease_font_size)
root.bind("<Control-0>", increase_width)
root.bind("<Control-9>", decrease_width)
root.bind("<Alt-equal>", increase_height)
root.bind("<Alt-minus>", decrease_height)
root.bind("<Control-Alt-equal>", increase_spacing)
root.bind("<Control-Alt-minus>", decrease_spacing)

root.attributes('-topmost', True)
root.mainloop()
