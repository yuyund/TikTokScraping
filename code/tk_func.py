import tkinter
import tkinter.ttk as ttk

class UI:
    def __init__(self,gj_obj,sj_obj):
        self.__create_UI()
        self.set_accountaddr(gj_obj['client_email'])
        self.set_sheetbox(sj_obj.get("sheet_url"))
        self.set_verify_addr(sj_obj.get("custom_verifyFp"))
        self.set_interval_box(sj_obj.get("interval"))

    def __create_UI(self):
        self.root = tkinter.Tk()
        self.root.title("設定")
        self.root.geometry("600x400")
        self.frame = ttk.Frame(self.root)
        self.frame.grid(column=0,row=0, sticky=tkinter.N+tkinter.E+tkinter.S+tkinter.W ,padx=50, pady=100)
        self.label_sheet = tkinter.Label(self.frame,text="Sheet_URL")
        self.label_customverifyFp = tkinter.Label(self.frame,text="s_v_web_id")
        self.label_account = tkinter.Label(self.frame,text="Service_Address")
        self.label_interval = tkinter.Label(self.frame,text="取得間隔(時)")
        self.account_addr = ttk.Label(self.frame,text="")
        self.sheet_addr_box = ttk.Entry(self.frame,width=70)
        self.interval_box = ttk.Entry(self.frame,width=70)
        self.custum_verifyFp_box = ttk.Entry(self.frame,width=70)
        self.button_frame = ttk.Frame(self.frame)

        self.okbutton = ttk.Button(self.button_frame,text="OK")
        self.cancelbutton = ttk.Button(self.button_frame,text="キャンセル")
        self.__grid_objs()

    def __grid_objs(self):
        self.label_account.grid(row=0,column=0,sticky=tkinter.W)
        self.label_sheet.grid(row=1,column=0,sticky=tkinter.E)
        # self.label_customverifyFp.grid(row=2,column=0,sticky=tkinter.E)
        self.label_interval.grid(row=3,column=0,sticky=tkinter.E)
        self.account_addr.grid(row=0,column=1,sticky=tkinter.W)
        self.sheet_addr_box.grid(columnspan=2 ,row=1,column=1,sticky=tkinter.W)
        # self.custum_verifyFp_box.grid(columnspan=2, row=2, column=1,sticky=tkinter.W)
        self.interval_box.grid(columnspan=2,row=3,column=1,sticky=tkinter.W)
        self.button_frame.grid(row=4,column=1,sticky=tkinter.W)
        self.okbutton.grid(row=0,column=0,sticky=tkinter.W)
        self.cancelbutton.grid(row=0,column=1,sticky=tkinter.E)

    def set_sheetbox(self,text):
        if text:
            self.sheet_addr_box.delete(0,tkinter.END)
            self.sheet_addr_box.insert(tkinter.END,text)
    def set_accountaddr(self,text):
        if text:
            self.account_addr.configure(text=text)
    def set_verify_addr(self,text):
        if text:
            self.custum_verifyFp_box.delete(0,tkinter.END)
            self.custum_verifyFp_box.insert(tkinter.END,text)
    def set_interval_box(self,text):
        if text:
            self.interval_box.delete(0,tkinter.END)
            self.interval_box.insert(tkinter.END,text)
    def get_sheetbox(self):
        return self.sheet_addr_box.get()
    def get_verify_addr(self):
        return self.custum_verifyFp_box.get()
    def get_interval(self):
        return self.interval_box.get()
    def set_okbutton(self,func):
        self.okbutton.configure(command=func)
    def set_cancelbutton(self,func):
        self.cancelbutton.configure(command=func)
    def start(self):
        self.root.mainloop()
    def ok(self): #need override
        pass
    def cancel(self): #need override
        pass

# set_sheetbox
# set_accountaddr
# set_verify_addr
# start
#
# ok
# cancel

# オーバーライドしてから、commandオプション登録
