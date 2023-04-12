import os,chardet,windnd
from configparser import ConfigParser
from tkinter.filedialog import *
from tkinter.colorchooser import *
from tkinter import *
from tkinter import messagebox

class Application():
    def __init__(self):
        icon_path = os.path.join(os.getcwd(), "图标.ico")
        root.iconbitmap(icon_path)
        #读取配置文件并进行赋值
        self.file_path="None"
        self.config_path="None"
        self.color="None"
        self.encoding="utf-8"
        self.buffer=None  #缓冲区
        #创建主菜单
        menubar=Menu(root)
        #创建子菜单
        menufile=Menu(menubar)
        menuset=Menu(menubar)
        menuhelp=Menu(menubar)
        #在主菜单中添加按键
        menubar.add_cascade(label="文件",menu=menufile)
        menubar.add_cascade(label="设置",menu=menuset)
        menubar.add_cascade(label="帮助", menu=menuhelp)
        #添加文件菜单项
        menufile.add_command(label="新建",accelerator="ctrl+n",command=self.create_newfile)
        menufile.add_command(label="打开",accelerator="ctrl+o",command=self.open_file)
        menufile.add_command(label="保存", accelerator="ctrl+s", command=self.save_file)
        menufile.add_command(label="退出", accelerator="ctrl+q", command=self.exit)
        #添加设置菜单项
        menuset.add_command(label="背景颜色",  command=self.bg_color)
        #添加帮助菜单项
        menuhelp.add_command(label="关于记事本",accelerator="ctrl+h",command=self.help)
        menuhelp.add_command(label="快捷键",command=self.hot_key)
        #将主菜单添加到根窗口
        root["menu"]=menubar
        #文本编辑区
        self.textpad=Text(root,width=300,height=300)
        self.textpad.pack()
        #创建上下文菜单
        self.contextmenu=Menu(root)
        self.contextmenu.add_command(label="背景颜色",command=self.bg_color)
        #绑定快捷键
        #右键换颜色
        root.bind("<Button-3>",self.create_context_menu)
        #ctr+n新建文件
        root.bind("<Control-n>",lambda event:self.create_newfile())
        #ctr+o打开文件
        root.bind("<Control-o>",lambda event:self.open_file())
        # ctr+s保存文件
        root.bind("<Control-s>", lambda event: self.save_file())
        # ctr+h查看帮助
        root.bind("<Control-h>", lambda event: self.help())
        # ctr+q退出
        root.bind("<Control-q>", lambda event: self.exit())
        #设置默认配置文件路径
        self.set_default_config_path()
        #打开并读取上次使用文件
        self.get_last_file_object()
        #拖拽并读取文件
        windnd.hook_dropfiles(tkwindow_or_winfoid=root,func=self.drag_files)

    #设置默认配置文件路径
    def set_default_config_path(self):
        self.config_dirname=os.getcwd()
        self.config_path=fr"{self.config_dirname}\file_config.ini"

    #获取上一次文件内容
    def get_last_file_object(self):
        #读取上一次文件配置
        self.read_config()
        if self.color!="None":
            self.textpad.config(bg=self.color)
        #如果文件存在
        if self.file_path!="None" and os.path.exists(self.file_path):
            #打开文件并显示
            answer = messagebox.askquestion("通知选项", "是否打开最近使用文件?")
            if answer == "yes":
                #获取文件编码方式
                self.get_encoding()
                self.text_pad()
        #否则将文件置为空
        else:
            self.file_path="None"

    def create_context_menu(self,event):
        #在菜单右键单击处显示
        self.contextmenu.post(event.x_root,event.y_root)

    #设置背景板颜色
    def bg_color(self):
        self.color=askcolor(color="red",title="选择背景色")[1]
        self.textpad.config(bg=self.color)

    #在窗口上显示文件名
    def window_filename_show(self):
        root.title(f"记事本({self.file_path})")

    #新建文件
    def create_newfile(self):
        #创建新文件名称
        self.file_path = asksaveasfilename(defaultextension=".txt",initialfile="未命名.txt",filetypes=[("文本文档","*.txt"),("python文件","*.py"),("word文件","*.docx"),("excel文件","*.csv")],title="新建文件")
        # 保存文件并新建文件
        self.save_file()
        #保存配置
        self.save_config()
        #打开文件进行编辑
        self.text_pad()

    #获取文件编码方式
    def get_encoding(self):
        if self.file_path!="None":
            with open(file=self.file_path, mode="rb") as fp:
                content = fp.read()
            result = chardet.detect(content)
            self.encoding = result["encoding"]
            #如果编码方式并非gbk或者utf-8
            if self.encoding!="gbk" or self.encoding!="utf-8":
                content=content.decode(self.encoding).encode("utf-8")
                with open(file=self.file_path,mode="wb") as fp:
                    fp.write(content)
                self.encoding="utf-8"

    #打开文件
    def open_file(self):
        self.file_path=askopenfilename(defaultextension=".txt",filetypes=[("文本文档","*.txt"),("python文件","*.py"),("word文件","*.docx"),("excel文件","*.csv")],title='打开文件')
        #获取文件编码方式
        self.get_encoding()
        #保存配置
        self.save_config()
        #读取文件并输入记事本显示
        self.text_pad()

    #实现文件拖拽入窗口
    def drag_files(self,files):
        try:
            # 打开成功
            self.file_path="\n".join(item.decode("gbk") for item in files)
            # 获取文件编码方式
            self.get_encoding()
            # 保存配置
            self.save_config()
            # 读取文件并输入记事本显示
            self.text_pad()
        except:
            #打开失败
            messagebox.showerror(title="错误",message="目前只支持txt文本文件格式")

    #读取并显示文件
    def text_pad(self):
        with open(file=self.file_path,mode="r+",encoding=self.encoding) as fp:
            #读取文件内容
            self.buffer=fp.read()
            #清空窗口
            self.textpad.delete(1.0,END)
            #将读取到的文件显示出来
            self.textpad.insert(INSERT,self.buffer)
        #每次重新显示的时候将文字名字进行更改
        self.window_filename_show()

    #保存文件
    def save_file(self):
        #判断文件是否打开过
        if self.file_path=="None":
            #如果文件没有打开过就新建
            self.create_newfile()
        else:
            #如果打开过就保存
            with open(self.file_path,"w+",encoding=self.encoding) as fp:
                self.buffer=self.textpad.get(1.0,END)
                fp.write(self.buffer)
            #保存配置文件
            self.save_config()

    #查看帮助
    def help(self):
        messagebox.showinfo(title="帮助信息",message="本记事本软件已经在github上进行开源:https://gitclone.com/github.com/183815/-.git\n本软件支持拖拽读取文件\n版权所有，不得侵权！\n开发者：帅益舟")

    #快捷键
    def hot_key(self):
        messagebox.showinfo(title="快捷键",message="保存:control+s\n新建:control+n\n打开:control+o\n退出:control+q\n帮助:control+h")

    # 退出
    def exit(self):
        #判断文件是否修改过
        if self.buffer!=self.textpad.get(1.0,END):
            #如果修改过就提示是否保存文件
            anwser=messagebox.askquestion(title="保存提示",message="文件未保存，是否保存文件？")
            if anwser=="yes":
                self.save_file()
        root.quit()

    #读取文件配置信息
    def read_config(self):
        conf = ConfigParser()
        conf.read(self.config_path, encoding="utf-8")
        try:
            self.file_path=conf.get("文件配置","文件路径")
        except:
            self.file_path="None"
        try:
            self.color=conf.get("文件配置","背景颜色")
        except:
            self.color="None"

    #保存文件配置信息
    def save_config(self):
        conf=ConfigParser()
        conf.add_section("文件配置")
        conf.set("文件配置","文件路径",self.file_path)
        conf.set("文件配置", "背景颜色", self.color)
        with open(self.config_path,"w+",encoding="utf-8") as fp:
            conf.write(fp)



if __name__=="__main__":
    root=Tk()
    root.geometry("500x500")
    root.title("记事本(支持拖拽读取)")
    #实例化一个应用对象
    app=Application()
    root.mainloop()