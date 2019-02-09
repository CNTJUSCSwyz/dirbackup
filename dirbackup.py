#coding=utf-8
import requests
import sys
from tkinter import *

headers =  {"Accept-Encoding": "gzip", "Accept-Language": "zh-CN,zh;q=0.8", "Referer": "http://www.example.com/", "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"}

class FindBackUp(object):
    def __init__(self):
        # 创建主窗口,用于容纳其它组件
        self.root = Tk()
        # 给主窗口设置标题内容
        self.root.title("备份文件扫描器v1.0")
        #设置用来获取输入框的变量
        url_text=StringVar()
        # 第一行，靠左
        Label(self.root, text="URL: ", width=10).grid(row=0)
        # 创建一个输入框,并设置尺寸
        self.addressEntry = Entry(self.root, width=30, textvariable=url_text)
        self.address_input = self.addressEntry.grid(
            row=0, column=1,  sticky=W)
        url_text.set(" ")
        # 创建一个回显列表
        self.displayList = Listbox(self.root, width=60)
        self.display_info = self.displayList.grid(row=1, column=1,)

        # 创建一个查询结果的按钮
        self.result_button = Button(
            self.root, command=self.find_backup, text="查询").grid(row=2, column=0, sticky=W)

        # 创建一个退出程序的按钮
        self.exit_button = Button(
            self.root, command=self.tryExit, text="退出").grid(row=2, column=1, )
            # 完成布局
    def gui_arrang(self):
        self.address_input.pack()
        self.display_info.pack()
        self.result_button.pack()
        self.exit_button.pack()

    def tryExit(self):
        sys.exit(0)

    def find_backup(self):
        try:
        # 获取输入信息
            self.url = self.addressEntry.get().replace(' ','')
            if self.url[-1]!='/':
                self.url+='/'
            if self.url[:4]!='http':
                self.url='http://'+self.url
        # 为了避免非法值,导致程序崩溃,有兴趣可以用正则写一下具体的规则,我为了便于新手理解,减少代码量,就直接粗放的过滤了
        except:
            pass

       #清空回显列表可见部分,类似clear命令
        for item in range(10):
            self.displayList.insert(0, " ")
        backUpFile=self.setBackUpFile(['index.php'])
        # 为回显列表赋值
        for item in backUpFile:
            address = self.url + item
            print address
            r = requests.get(address, headers=headers)
            if r.status_code !=404:
                self.displayList.insert(0, address)
            else :
                pass



    def setBackUpFile(self,files):
        dirs=[]
        a = ['.bak', '.zip', '.rar', '.tar.gz', '.txt','~']
        b = ['.swp', '.swo', '.swn']
        c = ['www.zip','.DS_Store','robots.txt','.git']
        for f in files:
            for i in a:
                dirs.append(f+i)
            for j in b:
                dirs.append('.'+f+j)
        for k in c:
            dirs.append(k)
            
        return dirs
def main():
    # 初始化对象
    FL = FindBackUp()
    # 进行布局
    # FL.gui_arrang()
    # 主程序执行
    tkinter.mainloop()
    pass
if __name__ == "__main__":
    main()
