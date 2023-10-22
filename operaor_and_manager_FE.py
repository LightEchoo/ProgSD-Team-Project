'''
from tkinter import *
from tkinter import ttk

import BE_Function

#=创建全局变量
previous_window=None

#def return_to_previous_page(current_window,previous_window):#返回按钮
    #current_window.withdraw()
    #previous_window.deiconify()
    


def center_window(win, width, height):#居中显示
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    win.geometry(f"{width}x{height}+{x}+{y}")
    
#用户登录界面
def user_login():
    
    log_in.withdraw()#隐藏之前的界面

    global user_log
    global login_user_name
    global login_password
    global user_log_textbox1
    def hide():#恢复界面
        user_log.destroy()
        log_in.deiconify()
        
    user_log=Tk()
    user_log.title("user log in")
    user_log.geometry("500x200")
    center_window(user_log,500,200)
    
    #将恢复界面和关闭按钮连接
    user_log.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(user_log,text="account:")# input user's account
    label1.place(x=30,y=20)
    user_log_textbox1=Entry(user_log,text="")#输入框
    user_log_textbox1.place(x=150,y=20,width=200,height=25)
    user_log_textbox1.focus()
    login_user_name = str(user_log_textbox1.get()) #获得输入的用户名，作为后续查询的标志

    label2=Label(user_log,text="password:")#输入密码
    label2.place(x=30,y=50)
    textbox2=Entry(user_log,text="")
    textbox2.place(x=150,y=50,width=200,height=25)
    login_password = str(textbox2.get())#获得输入的用户名，作为后续查询的标志
    
    user_button1=Button(user_log,text="Register",command=register)#注册按钮
    user_button1.place(x=50,y=110,width=70,height=50)
    
    user_button2=Button(user_log,text="Log",command=log)#登录按钮
    user_button2.place(x=200,y=110,width=70,height=50)
    
#操作员登录界面
def operator_login(): 
    
    global operator_log
    def hide():#恢复界面
        operator_log.destroy()
        log_in.deiconify()
        
    log_in.withdraw()#隐藏之前的界面
    
   #操作员登录界面
    operator_log=Tk()
    
    #将恢复界面和关闭按钮连接
    operator_log.protocol("WM_DELETE_WINDOW", hide)
    
    operator_log.title("Operator")
    operator_log.geometry("500x200")
    center_window(operator_log,500,200)
    
    label1=Label(operator_log,text="account:")# input operator's account
    label1.place(x=30,y=20)
    textbox1=Entry(operator_log,text="")
    textbox1.place(x=150,y=20,width=200,height=25)
   
    label2=Label(operator_log,text="password:")#输入密码
    label2.place(x=30,y=50)
    textbox2=Entry(operator_log,text="")
    textbox2.place(x=150,y=50,width=200,height=25)
    
    operator_button2=Button(operator_log,text="Log",command=operatorlog)#进入操作员界面
    operator_button2.place(x=200,y=110,width=70,height=50)
    
#管理员登录界面
def manager_login(): 
    global manager_log
    
    def hide():#恢复界面
        manager_log.destroy()
        log_in.deiconify()
        
    log_in.withdraw()#隐藏之前的界面
    
    
    manager_log=Tk()
    manager_log.title("Manager")
    manager_log.geometry("500x200")
    center_window(manager_log,500,200)
    
    #将恢复界面和关闭按钮连接
    manager_log.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(manager_log,text="account:")# input user's account
    label1.place(x=30,y=20)
    textbox1=Entry(manager_log,text="")
    textbox1.place(x=150,y=20,width=200,height=25)
    
    label2=Label(manager_log,text="password:")#输入密码
    label2.place(x=30,y=50)
    textbox2=Entry(manager_log,text="")
    textbox2.place(x=150,y=50,width=200,height=25)
    
    user_button2=Button(manager_log,text="Log",command=managerlog)#进入管理员界面
    user_button2.place(x=200,y=110,width=70,height=50)
    
#所有的登录按钮，返回登录成功提示
def log():

    login_result = BE_Function.login(login_user_name, login_password)
    log_window = Tk()
    log_window.geometry("500x300")


    if login_result:
        label=Label(log_window,text="Successgully Log in")#登陆成功
        label.place(x=150,y=100)
    else:
        log_fault=Tk()
        label2=Label(log_window,text="Error Log in ")#用户不存在
        label2.place(x=150,y=120)
    

#注册按钮
def register():
    global register_interface
    
    def hide():#恢复界面
        register_interface.destroy()
        user_log.deiconify()
        
    user_log.withdraw()#隐藏之前的界面
    
    register_interface=Tk()
    register_interface.title("Register")
    register_interface.geometry("500x200")
    center_window(register_interface,500,200)
    
    #将恢复界面和关闭按钮连接
    register_interface.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(register_interface,text="user name:")#输入注册的用户名
    label1.place(x=30,y=20)
    
    textbox1=Entry(register_interface,text="")#输入框
    textbox1.place(x=150,y=20,width=200,height=25)
    
    label2=Label(register_interface,text="password:")#输入密码
    label2.place(x=30,y=50)
    
    textbox2=Entry(register_interface,text="")
    textbox2.place(x=150,y=50,width=200,height=25)
    
    button=Button(register_interface,text="Regist",command=regist)#注册按钮
    button.place(x=350,y=100)
    
#注册结果界面
def regist():
    
    label=Label(register_interface,text="Successgully regist")#登陆成功
    label.place(x=150,y=100)
    
    label2=Label(register_fault,text="Existed user")#用户已存在
    label2.place(x=150,y=140)
    
#经理默认界面
def managerlog():
    
    
    global managerlog_in
    
    def hide():#恢复界面
        managerlog_in.destroy()
        manager_log.deiconify()
        
    manager_log.withdraw()#隐藏之前的界面
    
    managerlog_in=Tk()
    managerlog_in.geometry("500x200")
    managerlog_in.title("Manager")
    center_window(managerlog_in,500,200)
    
    #将恢复界面和关闭按钮连接
    managerlog_in.protocol("WM_DELETE_WINDOW", hide)
    
    button1=Button(managerlog_in,text="Report",command=report)#报告按钮
    button1.place(x=30,y=80,width=70,height=50)
    
    button2=Button(managerlog_in,text="codition",command=situation)#车辆情况按钮
    button2.place(x=110,y=80,width=70,height=50)
    
    button3=Button(managerlog_in,text="User situation",command=change)#更改用户信息
    button3.place(x=190,y=80,width=100,height=50)
    
#查看报告界面
def report():
    
    global reportinterface
    
    def hide():#恢复界面
        reportinterface.destroy()
        managerlog_in.deiconify()
        
    managerlog_in.withdraw()#隐藏之前的界面
    
    reportinterface=Tk()
    reportinterface.geometry("500x200")
    reportinterface.title("Report")
    center_window(reportinterface,500,200)
    
    #将恢复界面和关闭按钮连接
    reportinterface.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(reportinterface,text="choose type of vichle")#选择车辆类型
    dd1=ttk.Combobox(reportinterface)
    dd1.place(x=40,y=50)
    dd1["values"]=('bike','scooter')#可选车辆类型
    dd1_get=dd1.get()
    text1=str(dd1_get)
    
    dd2=ttk.Combobox(reportinterface)#选择查看时间
    dd2.place(x=250,y=50)
    dd2["values"]=('10-12','12-1')#时间段

    dd2_get=dd2.get()
    text2=str(dd2_get)
    #更换图片 def changepicture():
    #art=PhotoImage(file='x.file')
    #photobox=Label(reportinterface,image=art)
    #photobox.place(x=100,y=30,width=200,height=150)
    #button=Button(reportinterface,text="see report",command=changepicture)
    
def situation():#车辆使用情况界面

    global situationinterfacee
    
    def hide():#恢复界面
        situationinterface.destroy()
        managerlog_in.deiconify()
        
    managerlog_in.withdraw()#隐藏之前的界面
    
    situationinterface=Tk()
    situationinterface.geometry("500x200")
    situationinterface.title("car coditation")
    center_window(situationinterface,500,200)
    
    #将恢复界面和关闭按钮连接
    situationinterface.protocol("WM_DELETE_WINDOW", hide)
    
    dd1=ttk.Combobox(situationinterface)
    dd1["value"]=('all','car1','car2')
    dd1.place(x=40,y=20)
    dd1_get=dd1.get()
    text1=str(dd1_get)
    car_list=Listbox()
    car_list.place(x=30,y=50,width=200,height=150)

def change():#更改用户相关信息
    

    global  user_management
    
    def hide():#恢复界面
        user_management.destroy()
        managerlog_in.deiconify()
        
    managerlog_in.withdraw()#隐藏之前的界面

    user_management=Tk()  
    user_management.geometry("500x200")
    user_management.title("User management")
    center_window(user_management,500,200)
    
    #将恢复界面和关闭按钮连接
    user_management.protocol("WM_DELETE_WINDOW", hide)
    
    button1=Button(user_management,text="Examine",command=examine)#查看用户信息按钮
    button1.place(x=30,y=80,width=60,height=50)
    
    button2=Button(user_management,text="Add",command=adduser)#增加用户按钮
    button2.place(x=100,y=80,width=60,height=50)
    
    button3=Button(user_management,text="Delete",command=deleteuser)#删除用户信息
    button3.place(x=170,y=80,width=60,height=50)
    
    button4=Button(user_management,text="Change",command=changeuser)#更改用户信息
    button4.place(x=240,y=80,width=60,height=50)
    
def examine():#查看用户信息，输入用户名，查看相关信息
    def clean_userinfo():#清楚用户列表内容
         box2.delete(0,END)
         
    def show():#显示用户信息
         name=box1.get()
         box2.insert(END,name)
         box1.delete(0,END)
    
    global  examineinfo
    
    def hide():#恢复界面
        examineinfo.destroy()
        user_management.deiconify()
        
    user_management.withdraw()#隐藏之前的界面
    
    examineinfo=Tk()
    examineinfo.geometry("500x200")
    examineinfo.title("User information ")
    center_window(examineinfo,500,200)
    
    #将恢复界面和关闭按钮连接
    examineinfo.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(examineinfo,text="Enter user name")#输入用户名
    label1.place(x=20,y=20)
    box1=Entry(examineinfo,text=0)
    box1.place(x=120,y=20,width=100,height=25)
    
    box2=Listbox(examineinfo)
    box2.place(x=120,y=50,width=150,height=50)
    
    button1=Button(examineinfo,text="show",command=show)#显示按钮
    button1.place(x=350,y=20,width=100,height=25)
    
    button2=Button(examineinfo,text="clean the list",command=clean_userinfo)#清空列表
    button2.place(x=350,y=50,width=100,height=25)
    
    
def adduser():#增加一个用户
    
    global  adduser_info
   
    def hide():#恢复界面
        adduser_info.destroy()
        user_management.deiconify()
       
    user_management.withdraw()#隐藏之前的界面 

    adduser_info=Tk()
    adduser_info.geometry("500x200")
    adduser_info.title("Add user ")
    center_window(adduser_info,500,200)
    
    #将恢复界面和关闭按钮连接
    adduser_info.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(adduser_info,text="User name:")#增加的用户名
    label1.place(x=20,y=20)
    
    box1=Entry(adduser_info,text=0)
    box1.place(x=120,y=20,width=100,height=25)
    
    label2=Label(adduser_info,text="password:")#密码
    label2.place(x=20,y=60)
    
    box2=Entry(adduser_info,text=0)
    box2.place(x=120,y=60,width=100,height=25)
    
    button=Button(adduser_info,text="Add")#增加按钮
    button.place(x=250,y=20)
    adduser_info.mainloop()

def deleteuser():#删除一个用户

    global  deleteuser_info
   
    def hide():#恢复界面
        deleteuser_info.destroy()
        user_management.deiconify()
       
    user_management.withdraw()#隐藏之前的界面

    deleteuser_info=Tk()
    deleteuser_info.geometry("500x200")
    deleteuser_info.title("Delete user ")
    center_window(deleteuser_info,500,200)
    
    #将恢复界面和关闭按钮连接
    deleteuser_info.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(deleteuser_info,text="User name:")
    label1.place(x=20,y=20)
    
    box1=Entry(deleteuser_info,text=0)
    box1.place(x=120,y=20,width=100,height=25)
    
    button=Button(deleteuser_info,text="Delete")
    button.place(x=250,y=20)
    
def changeuser():#修改用户信息
    
    global  changeuser_info
   
    def hide():#恢复界面
        changeuser_info.destroy()
        user_management.deiconify()
       
    user_management.withdraw()#隐藏之前的界面

    changeuser_info=Tk()
    changeuser_info.geometry("500x200")
    changeuser_info.title("Change user information ")
    center_window(changeuser_info,500,200)
    
    #将恢复界面和关闭按钮连接
    changeuser_info.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(changeuser_info,text="User name:")
    label1.place(x=20,y=20)
    
    box1=Entry(changeuser_info,text=0)
    box1.place(x=120,y=20,width=100,height=25)
    
    label2=Label(changeuser_info,text="information:")
    label2.place(x=20,y=50)
    
    box2=Entry(changeuser_info,text=0)
    box2.place(x=120,y=50,width=100,height=25)
    
    button=Button(changeuser_info,text="Change")    
    button.place(x=250,y=20)

def operatorlog():#操作员界面


    global operator_log_in
    def hide():#恢复界面
        operator_log_in.destroy()
        operator_log.deiconify()
        
    operator_log.withdraw()#隐藏之前的界面

    operator_log_in=Tk()
    operator_log_in.geometry("500x200")
    operator_log_in.title("Operator")
    center_window(operator_log_in,500,200)
    
    #将恢复界面和关闭按钮连接
    operator_log_in.protocol("WM_DELETE_WINDOW", hide)
    
    button1=Button(operator_log_in,text="Charge",command=charge)#充电按钮
    button1.place(x=130,y=20,width=70,height=25)
    
    button2=Button(operator_log_in,text="repair",command=repair)#维修
    button2.place(x=130,y=50,width=70,height=25)
    
    button3=Button(operator_log_in,text="Move",command=move)#更改位置信息（移动车辆）
    button3.place(x=130,y=80,width=70,height=25)
    
def charge():#充电功能

    global charge_log
    def hide():#恢复界面
        charge_log.destroy()
        operator_log_in.deiconify()
        
    operator_log_in.withdraw()#隐藏之前的界面

    charge_log=Tk()
    charge_log.geometry("500x200")
    charge_log.title("Charge ")
    center_window(charge_log,500,200)
    
    #将恢复界面和关闭按钮连接
    charge_log.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(charge_log,text="Car code::")#输入操作车辆编号
    label1.place(x=20,y=20)
    
    box1=Entry(charge_log,text=0)
    box1.place(x=100,y=20,width=100,height=25)
    
    label2=Label(charge_log, text="Car in low charge:")#显示需要充电的车辆编号
    label2.place(x=20,y=50)
    box2=Listbox(charge_log)
    box2.place(x=150,y=50,width=100,height=50)
    
    button=Button(charge_log,text="Charge",command=charge_car)
    button.place(x=100,y=20,width=100,height=25)

def repair():#维修界面

    global repair_log
    def hide():#恢复界面
        repair_log.destroy()
        operator_log_in.deiconify()
       
    operator_log_in.withdraw()#隐藏之前的界面

    repair_log=Tk()
    repair_log.geometry("500x200")
    repair_log.title("Repair ")
    center_window(repair_log,500,200)
    
    
    #将恢复界面和关闭按钮连接
    repair_log.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(repair_log,text="Car code::")#输入操作车辆编号
    label1.place(x=20,y=20)
    
    box1=Entry(repair_log,text=0)
    box1.place(x=100,y=20,width=100,height=25)
    
    label2=Label(repair_log, text="Car in repairing:")#显示需要维修的所有车辆编号
    label2.place(x=20,y=50)
    box2=Listbox(repair_log)
    box2.place(x=150,y=50,width=100,height=50)
    
    button=Button(repair_log,text="Charge",command=repair_car)
    button.place(x=250,y=20,width=100,height=25)
def move():#移动界面

    global  move_log
    def hide():#恢复界面
        move_log.destroy()
        operator_log_in.deiconify()
       
    operator_log_in.withdraw()#隐藏之前的界面

    move_log=Tk()
    move_log.geometry("500x200")
    move_log.title("Movement ")
    center_window(move_log,500,200)
    
    #将恢复界面和关闭按钮连接
    move_log.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(move_log,text="Car code::")#输入操作车辆编号
    label1.place(x=20,y=20)
    
    box1=Entry(move_log,text=0)
    box1.place(x=100,y=20,width=100,height=25)
    
    label2=Label(move_log, text="New location:")#输入移动车辆后的位置
    label2.place(x=20,y=50)
    box2=Entry(move_log,text=0)
    box2.place(x=110,y=50,width=100,height=50)
    
    button=Button(move_log,text="Move",command=move_car)
    button.place(x=100,y=20,width=100,height=25)
    
    
#regist_interface=Tk()#注册结果页面
#regist_interface.title("registertion result")
#regist_interface.geometry("500x300")  
   
log_in=Tk()#login interface
log_in.title("LOG IN")
log_in.geometry("500x200")
center_window(log_in,500,200)

button1=Button(log_in,text="User", command=user_login)#log in user's interface
button1.place(x=30,y=20)

button2=Button(log_in,text="Operator",command=operator_login)#log in operator's interface
button2.place(x=100,y=20)

button3=Button(log_in,text="Manager",command=manager_login)#log in manager's interface
button3.place(x=200,y=20)

log_in.mainloop()

'''