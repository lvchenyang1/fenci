import tkinter
from tkinter import ttk
from middle_fenci import wrap
from tkinter.filedialog import askopenfilenames
from tkinter import messagebox
from middle_fenci.config import configini
import os
import shutil

win = tkinter.Tk()
win.title("中文分词中间件 版本V1.0")
win.geometry("1000x650+200+50")

#初始化四个值
default_model = "jieba"
default_type = "字符串"
default_flag = "no"
default_path = False


def change_model():
    global default_model
    default_model = model_choice.get()
    print(default_model)




def hello():
    pass
# 菜单条
menubar = tkinter.Menu(win)
filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=win.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = tkinter.Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = tkinter.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)



# display the menu

win.config(menu=menubar)


title = tkinter.Label(win, text="中文分词系统",font=("黑体", 20))
# 相对布局，窗体改变对控件有影响
title.pack( side=tkinter.TOP)

model = tkinter.Label(win,text="模型：",font=("黑体", 12))
model.place(x=100,y=50)
# 绑定变量

#获取ini文件中的所有模型
user_conf_content = configini.get_model()


model_list = tkinter.StringVar()
model_choice = ttk.Combobox(win, textvariable=model_list)
model_choice.place(x=150,y=50)
# 设置下拉数据
model_choice["value"] =tuple(user_conf_content)
# 设置默认值
model_choice.current(0)
# 绑定事件
def change_model(event):
    global default_model
    default_model = model_choice.get()
    print(default_model)
model_choice.bind("<<ComboboxSelected>>", change_model)

"""是否加载字典"""
def func_loadDict():
    srcfile = loadDict_path.get()[2:-3]
    file_name = os.path.split(srcfile)[1]

    dstfile = r'./middle_fenci/public_dict/'+file_name

    shutil.copyfile(srcfile,dstfile)
    messagebox.showinfo(title='加载字典', message='加载成功')
loadDict = tkinter.Label(win,text="个人字典文件路径：",font=("黑体", 12))
loadDict.place(x=450,y=50)

loadDict_button = tkinter.Button(win,text="字典加载",command = func_loadDict)
loadDict_button.place(x=880,y=47)

"""选择文件"""
def select_loadDict_Path():
    loadDict_path_ = askopenfilenames()
    loadDict_path.set(loadDict_path_)
    c = loadDict_path.get()


loadDict_path = tkinter.StringVar()

loadDict_file_dir = tkinter.Entry(win, textvariable = loadDict_path)
loadDict_file_dir.place(x=600,y=50)

file_button = tkinter.Button(win, text = "字典路径选择", command = select_loadDict_Path)
file_button.place(x=750,y=47)


















types = tkinter.Label(win,text="输出类型：",font=("黑体", 12))
types.place(x=50,y=300)
# 绑定变量
type_list = tkinter.StringVar()

type_choice = ttk.Combobox(win, textvariable=type_list)
type_choice.place(x=140,y=300)

# 设置下拉数据
type_choice["value"] = ("字符串", "列表")
# 设置默认值
type_choice.current(0)

# 绑定事件


def change_type(event):
    global default_type
    default_type = type_choice.get()
    print(default_type)


type_choice.bind("<<ComboboxSelected>>", change_type)


separator = tkinter.Label(win,text="分隔符：",font=("黑体", 12))
separator.place(x=350,y=300)
# 绑定变量
cnames = tkinter.StringVar()
cnames.set(" ")
separator_content = tkinter.Entry(win,textvariable=cnames)

separator_content.place(x=430,y=300)


flag = tkinter.Label(win,text="是否显示词性：",font=("黑体", 12))
flag.place(x=600,y=300)
# 绑定变量
flag_list = tkinter.StringVar()

flag_choice = ttk.Combobox(win, textvariable=flag_list)
flag_choice.place(x=730,y=300)

# 设置下拉数据
flag_choice["value"] = ("yes", "no")
# 设置默认
flag_choice.current(1)

# 绑定事件

def change_flag(event):
    global default_flag
    default_flag = flag_choice.get()
    print(default_flag)
flag_choice.bind("<<ComboboxSelected>>", change_flag)



"""text文本输入框"""
text_content = tkinter.Text(win, width=100, height=13)
text_content.insert(tkinter.INSERT, "请输入要分析的内容")
text_content.place(x=100,y=100)

"""选择文件"""
def selectPath():
    global default_path
    path_ = askopenfilenames()
    path.set(path_)
    c = path.get()

    default_path = True

def clearPath():
    global default_path
    path.set("")
    default_path = False
path = tkinter.StringVar()

file_path = tkinter.Label(win,text = "目标路径:")
file_path.place(x=830,y=170)
file_dir = tkinter.Entry(win, textvariable = path)
file_dir.place(x=830,y=230)

file_button = tkinter.Button(win, text = "路径选择", command = selectPath)
file_button.place(x=830,y=200)

file_clear_path = tkinter.Button(win,text = "清除路径",command = clearPath)
file_clear_path.place(x=830,y=250)



def analyse():
    #加载public_dict字典
    user_dict = wrap.All_model_loadDict()
    user_dict.loadDict()
    global default_model
    global default_type
    global default_flag
    global default_path

    if default_type == "字符串":
        default_type = "str"
    if default_type == "列表":
        default_type = "list"
    if default_path == True:
        content_analyse = path.get()[2:-3]
    if default_path == False:
        content_analyse = text_content.get("1.0", "end")


    c = wrap.All_model_fenci(contents_dir=content_analyse, model=default_model, types=default_type, separator=separator_content.get(),flag=default_flag)
    result = c.fenci()
    result_content = str(result)+"\n"
    print(result)
    text_result.insert(tkinter.INSERT, result_content)
#分析按钮
fenci_button = tkinter.Button(win,text="分析",font=("黑体", 15),command=analyse,width=12,height=2)
fenci_button.place(x=400,y=350)
#结果展示框
text_result = tkinter.Text(win, width=100, height=13)

text_result.place(x=100, y=450)

def clear_text_result():

    text_result.delete(1.0, tkinter.END)

clear_button = tkinter.Button(win,text="清空",command=clear_text_result)
clear_button.place(x=830,y=530)

win.mainloop()