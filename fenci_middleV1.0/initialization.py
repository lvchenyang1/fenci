import tkinter
import configparser
from tkinter import messagebox

win = tkinter.Tk()
win.title("中文分词中间件 版本V1.0")
win.geometry("700x350+200+50")

title = tkinter.Label(win, text="中文分词中间件初始化配置",font=("黑体", 20))
# 相对布局，窗体改变对控件有影响
title.pack( side=tkinter.TOP)

lable1 = tkinter.Label(win,text="中间件支持的模型",font=("黑体", 12))
lable1.place(x=80,y=55)

lable2 = tkinter.Label(win,text="选择的模型",font=("黑体", 12))
lable2.place(x=380,y=55)





frame_left = tkinter.Frame(win,height=250,width=200,borderwidth=1,relief="sunken")
frame_left.place(x=60,y=80)

#jieba
lable_jieba = tkinter.Label(frame_left, text="jieba", font=("黑体", 10))

lable_jieba.place(x=5,y=10)

def func_jieba_add():
    global jieba_content
    jieba_content.set("jieba")

button_jiaba_add = tkinter.Button(frame_left, text = "添加", command = func_jieba_add)
button_jiaba_add.place(x=70,y=5)

def func_jiaba_remove():
    global jieba_content
    jieba_content.set("")
button_jiabe_remove = tkinter.Button(frame_left, text = "移除", command = func_jiaba_remove)
button_jiabe_remove.place(x=130,y=5)


#ltp
lable_ltp = tkinter.Label(frame_left, text="ltp", font=("黑体", 10))

lable_ltp.place(x=5,y=45)

def func_ltp_add():
    global ltp_content
    ltp_content.set("ltp")
button_ltp_add = tkinter.Button(frame_left, text = "添加", command = func_ltp_add)
button_ltp_add.place(x=70,y=40)

def func_ltp_remove():
    global ltp_content
    ltp_content.set("")
button_ltp_remove = tkinter.Button(frame_left, text = "移除", command = func_ltp_remove)
button_ltp_remove.place(x=130,y=40)


#nlpir
lable_nlpir = tkinter.Label(frame_left, text="nlpir", font=("黑体", 10))

lable_nlpir.place(x=5,y=80)

def func_nlpir_add():
    global nlpir_content
    nlpir_content.set("nlpir")
button_nlpir_add = tkinter.Button(frame_left, text = "添加", command = func_nlpir_add)
button_nlpir_add.place(x=70,y=75)


def func_nlpir_remove():
    global nlpir_content
    nlpir_content.set("")
button_nlpir_remove = tkinter.Button(frame_left, text = "移除", command = func_nlpir_remove)
button_nlpir_remove.place(x=130,y=75)



#右边的frame
frame_right = tkinter.Frame(win,height=250,width=200,borderwidth=1,relief="sunken")
frame_right.place(x=330,y=80)

jieba_content = tkinter.StringVar()
entry_jieba = tkinter.Entry(frame_right,textvariable=jieba_content)

entry_jieba.place(x=5,y=10)

ltp_content = tkinter.StringVar()
entry_ltp = tkinter.Entry(frame_right,textvariable=ltp_content)

entry_ltp.place(x=5,y=45)

nlpir_content = tkinter.StringVar()
entry_nlpir = tkinter.Entry(frame_right,textvariable=nlpir_content)

entry_nlpir.place(x=5,y=80)



config = configparser.ConfigParser()

def func_submit():
    global jieba_content
    global ltp_content
    global nlpir_content

    conf_jieba = jieba_content.get()

    conf_ltp = ltp_content.get()

    conf_nlpir = nlpir_content.get()

    r = messagebox.askquestion('消息框', '确定加载？')
    if r == "yes":
        config.add_section("OPTIONS")
        config.add_section("CLIENT")
        if conf_jieba == "jieba":
            config.set("OPTIONS", conf_jieba, conf_jieba)
        if conf_ltp == "ltp":
            config.set("OPTIONS", conf_ltp, conf_ltp)
        if conf_nlpir == "nlpir":
            config.set("OPTIONS", conf_nlpir, conf_nlpir)

        config.set("CLIENT", "USER_CONF",conf_jieba)


        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        messagebox.showinfo(title='加载', message='成功')
    else:
        pass



def func_quit():
    win.quit()
button_submit = tkinter.Button(win,text="确定",command = func_submit)
button_submit.place(x=600,y=200)
button_quit = tkinter.Button(win,text="退出",command = func_quit)
button_quit.place(x=600,y=240)



#选择的模型
# state_jieba = tkinter.Label(frame_right, text="jieba", font=("黑体", 10),state="active")
# state_jieba.place(x=2,y=2)
# state_jieba = tkinter.Label(frame_right, text="jieba", font=("黑体", 10),state="disabled")
# state_jieba.place(x=20,y=2)

















# frame_l = tkinter.Frame(frame_root)
# frame_2 = tkinter.Frame(frame_root)
# #创建一个标签，并在窗口上显示
# tkinter.Label(frame_l, text="中国", bg="green", font=("Arial", 12), width=10, height=2).pack(side=tkinter.TOP)
# tkinter.Label(frame_l, text="日本", bg="green", font=("Arial", 12), width=10, height=2).pack(side=tkinter.TOP)
# tkinter.Label(frame_2, text="美国", bg="green", font=("Arial", 12), width=10, height=2).pack(side=tkinter.TOP)
# tkinter.Label(frame_2, text="韩国", bg="green", font=("Arial", 12), width=10, height=2).pack(side=tkinter.TOP)
# #框架的位置布局
# frame_l.place(x=1,y=1)
# frame_2.place(x=40,y=50)



win.mainloop()