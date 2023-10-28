
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import font
import BE_Function
import SqlFunction
import CommonFunction


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

def info_window(info_detail):
    show_info = Tk()
    show_info.geometry("500x300")
    label = Label(show_info, text = info_detail)
    label.place(x=150, y=100)

#用户登录界面
def user_login():
    
    log_in.withdraw()#隐藏之前的界面
    
    global user_log
    def hide():#恢复界面
        user_log.destroy()
        log_in.deiconify()
        
      
    user_log=Tk()
    user_log.title("user log in")
    user_log.geometry("1800x800")
    center_window(user_log,1600,800)
    
   
    
    #将恢复界面和关闭按钮连接
    user_log.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(user_log,text="account:",)# input user's account
    label1.place(relx=0.1,rely=0.1,relwidth=0.1,relheight=0.1)
    label1.config(font=("Helvetica", 20, "bold"))
    
    textbox1=Entry(user_log,text="")#输入框
    textbox1.place(relx=0.2,rely=0.1,relwidth=0.5,relheight=0.1)
    
    
    label2=Label(user_log,text="password:",font=tkinter_font1)#输入密码
    label2.place(relx=0.1,rely=0.3)
    label2.config(font=("Helvetica", 20, "bold"))
    
    textbox2=Entry(user_log,text="")
    textbox2.place(relx=0.2,rely=0.3,relwidth=0.5,relheight=0.1)
    
    #user_button1=Button(user_log,text="Register",command=register,font=tkinter_font1)#注册按钮
    #user_button1.place(relx=0.2,rely=0.55,relwidth=0.05,relheight=0.05)
    
    user_button2=Button(user_log,text="Log",command=log,font=tkinter_font1)#登录按钮
    user_button2.place(relx=0.6,rely=0.55,relwidth=0.05,relheight=0.05)
    
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
    operator_log.geometry("800x600")
    center_window(operator_log,1600,800)
    
    label1=Label(operator_log,text="account:")# input operator's account
    label1.place(relx=0.1,rely=0.1)
    label1.config(font=("Helvetica", 20, "bold"))
    
    global operator_login_textbox1
    operator_login_textbox1=Entry(operator_log,text="")
    operator_login_textbox1.place(relx=0.2,rely=0.1,relwidth=0.5,relheight=0.05)
   
    label2=Label(operator_log,text="password:")#输入密码
    label2.place(relx=0.1,rely=0.25)
    label2.config(font=("Helvetica", 20, "bold"))
    
    global operator_login_textbox2
    operator_login_textbox2=Entry(operator_log,text="")
    operator_login_textbox2.place(relx=0.2,rely=0.25,relwidth=0.5,relheight=0.05)
    
    
    operator_button2=Button(operator_log,text="Log",command=operatorlog,font=tkinter_font1)#进入操作员界面
    operator_button2.place(relx=0.3,rely=0.5,relwidth=0.1,relheight=0.05)
    
#管理员登录界面
def manager_login(): 
    global manager_log
    
    def hide():#恢复界面
        manager_log.destroy()
        log_in.deiconify()
        
    log_in.withdraw()#隐藏之前的界面
    
    
    manager_log=Tk()
    manager_log.title("Manager")
    manager_log.geometry("800x600")
    center_window(manager_log,1600,800)
    
    #将恢复界面和关闭按钮连接
    manager_log.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(manager_log,text="account:")# input user's account
    label1.place(relx=0.1,rely=0.1)
    label1.config(font=("Helvetica", 20, "bold"))
    
    global manager_log_textbox1
    manager_log_textbox1=Entry(manager_log,text="")
    manager_log_textbox1.place(relx=0.2,rely=0.1,relwidth=0.4,relheight=0.05)
    
    label2=Label(manager_log,text="password:")#输入密码
    label2.place(relx=0.1,rely=0.25)
    label2.config(font=("Helvetica", 20, "bold"))
    
    global manager_log_textbox2
    manager_log_textbox2=Entry(manager_log,text="")
    manager_log_textbox2.place(relx=0.2,rely=0.25,relwidth=0.4,relheight=0.05)
    
    user_button2=Button(manager_log,text="Log",command=managerlog,font=tkinter_font1)#进入管理员界面
    user_button2.place(relx=0.3,rely=0.5,relwidth=0.2,relheight=0.1)
    
#所有的登录按钮，返回登录成功提示
def log():
    
    log_success=Tk()
    log_success.geometry("500x300")
    label=Label(log_success,text="Successgully Log in")#登陆成功
    label.place(x=150,y=100)
    #label2=Label2(log_fault,text="Unexisted user")#用户不存在
    #label2.place(x=150,y=120)
    #label3=Label(log_password,text="Incorrect password")#密码错误
    #label3.place(x=150,y=140)
    
    log_success.mainloop()
'''
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
    center_window(register_interface,1600,800)
    
    #将恢复界面和关闭按钮连接
    register_interface.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(register_interface,text="user name:")#输入注册的用户名
    label1.place(relx=0.2,rely=0.2)
    
    global register_textbox1
    
    register_textbox1=Entry(register_interface,text="")#输入框
    register_textbox1.place(relx=0.25,rely=0.2,relwidth=0.5,relheight=0.1)
    
    label2=Label(register_interface,text="password:")#输入密码
    label2.place(relx=0.2,rely=0.4)
    
    global register_textbox2
    register_textbox2=Entry(register_interface,text="")
    register_textbox2.place(relx=0.25,rely=0.4,relwidth=0.5,relheight=0.1)
    
    button=Button(register_interface,text="Regist",command=regist)#注册按钮
    button.place(relx=0.8,rely=0.2)
    
#注册结果界面

def regist():
    
    register_name=register_textbox1.get()
    register_password=register_textbox2,get()
    
    label=Label(register_interface,text="Successgully regist")#登陆成功
    label.place(x=150,y=100)
    
    label2=Label(register_fault,text="Existed user")#用户已存在
    label2.place(x=150,y=140)
'''
#经理默认界面
def managerlog():
    
    
    global managerlog_in
    
    def hide():#恢复界面
        managerlog_in.destroy()
        manager_log.deiconify()
        
    manager_log.withdraw()#隐藏之前的界面
    #获得名字和密码
    manager_name=manager_log_textbox1.get()
    manager_password=manager_log_textbox2.get()
    #后台判断是否
    
    managerlog_in=Tk()
    managerlog_in.geometry("500x200")
    managerlog_in.title("Manager")
    center_window(managerlog_in,1600,800)
    
    #将恢复界面和关闭按钮连接
    managerlog_in.protocol("WM_DELETE_WINDOW", hide)

    '''button1=Button(managerlog_in,text="Report",command=report)#报告按钮
    button1.place(relx=0.5,rely=0.1,relwidth=0.3,relheight=0.15)'''
    
    button2=Button(managerlog_in,text="codition",command=situation)#车辆情况按钮
    button2.place(relx=0.5,rely=0.4,relwidth=0.3,relheight=0.15)
    
    button3=Button(managerlog_in,text="User situation",command=change)#更改用户信息
    button3.place(relx=0.5,rely=0.7,relwidth=0.3,relheight=0.15)



#查看报告界面
'''def report():
    
    global reportinterface
    
    def hide():#恢复界面
        reportinterface.destroy()
        managerlog_in.deiconify()
        
    managerlog_in.withdraw()#隐藏之前的界面
    
    reportinterface=Tk()
    reportinterface.geometry("500x200")
    reportinterface.title("Report")
    center_window(reportinterface,1600,800)
    
    #将恢复界面和关闭按钮连接
    reportinterface.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(reportinterface,text="choose type of vichle")#选择车辆类型
    dd1=ttk.Combobox(reportinterface)
    dd1.place(relx=0.15,rely=0.1)
    dd1["values"]=('bike','scooter')#可选车辆类型
    dd1_get=dd1.get()
    text1=str(dd1_get)#标记是否能获得
    
    print(text1)
    dd2=ttk.Combobox(reportinterface)#选择查看时间
    dd2.place(x=0.5,y=0.1)
    dd2["values"]=('10-12','12-1')#时间段

    dd2_get=dd2.get()
    text2=str(dd2_get)
    
    button=Button(reportinterface,text="show picture",command=show_picture)
    
    #更换图片 def changepicture():
    #art=PhotoImage(file='x.file')
    #photobox=Label(reportinterface,image=art)
    #photobox.place(x=100,y=30,width=200,height=150)
    #button=Button(reportinterface,text="see report",command=changepicture)
'''

def situation():#车辆使用情况界面

    global situationinterfacee
    
    def hide():#恢复界面
        situationinterface.destroy()
        managerlog_in.deiconify()
        
    managerlog_in.withdraw()#隐藏之前的界面
    
    situationinterface=Tk()
    situationinterface.geometry("500x200")
    situationinterface.title("car coditation")
    center_window(situationinterface,1600,800)
    
    #将恢复界面和关闭按钮连接
    situationinterface.protocol("WM_DELETE_WINDOW", hide)
    
    #查看是否正确获得
    dd1=ttk.Combobox(situationinterface)
    dd1["value"]=('all','car1','car2')
    dd1.place(x=40,y=20)
    dd1_get=dd1.get()
    text1=str(dd1_get)
    car_list=Listbox(situationinterface)
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
    center_window(user_management,1600,800)
    
    #将恢复界面和关闭按钮连接
    user_management.protocol("WM_DELETE_WINDOW", hide)
    
    button1=Button(user_management,text="Examine",command=examine)#查看用户信息按钮
    button1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.15)
    
    button2=Button(user_management,text="Add",command=adduser)#增加用户按钮
    button2.place(relx=0.2,rely=0.3,relwidth=0.6,relheight=0.15)
    
    button3=Button(user_management,text="Delete",command=deleteuser)#删除用户信息
    button3.place(relx=0.2,rely=0.5,relwidth=0.6,relheight=0.15)
    
    button4=Button(user_management,text="Change",command=changeuser)#更改用户信息
    button4.place(relx=0.2,rely=0.7,relwidth=0.6,relheight=0.15)
    
def examine():#查看用户信息，输入用户名，查看相关信息
    def clean_userinfo():#清楚用户列表内容
         box2.delete(0,END)
         
    def show():#显示用户信息
         #从数据库拿到用户相关信息,姓名，用户，密码，余额
         name=box1.get()
         pwd = 2
         deposit = 3
         due = 4
         box2.insert(END,name, pwd, deposit, due)
         box1.delete(0,END)
    
    global  examineinfo
    
    def hide():#恢复界面
        examineinfo.destroy()
        user_management.deiconify()
        
    user_management.withdraw()#隐藏之前的界面
    
    examineinfo=Tk()
    examineinfo.geometry("500x200")
    examineinfo.title("User information ")
    center_window(examineinfo,1600,800)
    
    #将恢复界面和关闭按钮连接
    examineinfo.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(examineinfo,text="Enter user name")#输入用户名
    label1.place(relx=0.1,rely=0.15)
    box1=Entry(examineinfo,text=0)
    box1.place(relx=0.25,rely=0.15,relwidth=0.5,relheight=0.15)
    
    box2=Listbox(examineinfo)
    box2.place(relx=0.1,rely=0.35,relwidth=0.7,relheight=0.3)
    
    button1=Button(examineinfo,text="show",command=show)#显示按钮
    button1.place(relx=0.8,rely=0.15,relwidth=0.1,relheight=0.15)
    
    button2=Button(examineinfo,text="clean the list",command=clean_userinfo)#清空列表
    button2.place(relx=0.8,rely=0.3,relwidth=0.1,relheight=0.15)
    
    
def adduser():#增加一个用户
    
    global  adduser_info
   
    def hide():#恢复界面
        adduser_info.destroy()
        user_management.deiconify()
    def add():#增加用户
        name=box1.get()
        password=box2.get()
        #数据库操作
        
    
    
    user_management.withdraw()#隐藏之前的界面 

    adduser_info=Tk()
    adduser_info.geometry("500x200")
    adduser_info.title("Add user ")
    center_window(adduser_info,1600,800)
    
    #将恢复界面和关闭按钮连接
    adduser_info.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(adduser_info,text="User name:")#增加的用户名
    label1.place(relx=0.1,rely=0.1)
    
    box1=Entry(adduser_info,text=0)
    box1.place(relx=0.25,rely=0.1,relwidth=0.4,relheight=0.15)
    
    label2=Label(adduser_info,text="password:")#密码
    label2.place(relx=0.1,rely=0.3)
    
    box2=Entry(adduser_info,text=0)
    box2.place(relx=0.25,rely=0.3,relwidth=0.40,relheight=0.15)
    
    button=Button(adduser_info,text="Add",command=add)#增加按钮
    button.place(relx=0.8,rely=0.1)
    
    

def deleteuser():#删除一个用户

    global  deleteuser_info
   
    def hide():#恢复界面
        deleteuser_info.destroy()
        user_management.deiconify()
    
    def delete():
        name=box1.get()
        #数据库操作
        
        
    user_management.withdraw()#隐藏之前的界面

    deleteuser_info=Tk()
    deleteuser_info.geometry("500x200")
    deleteuser_info.title("Delete user ")
    center_window(deleteuser_info,800,600)
    
    #将恢复界面和关闭按钮连接
    deleteuser_info.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(deleteuser_info,text="User name:")
    label1.place(relx=0.2,rely=0.3)
    
    box1=Entry(deleteuser_info,text=0)
    box1.place(relx=0.2,rely=0.5,relwidth=0.4,relheight=0.15)
    
    button=Button(deleteuser_info,text="Delete", command=delete)
    button.place(relx=0.5,rely=0.8)
    
def changeuser():#修改用户信息
    
    global  changeuser_info
   
    def hide():#恢复界面
        changeuser_info.destroy()
        user_management.deiconify()
    def change():
        change_name=box1.get()
        change_info=box2.get()
        #数据库
       
    user_management.withdraw()#隐藏之前的界面

    changeuser_info=Tk()
    changeuser_info.geometry("500x200")
    changeuser_info.title("Change user information ")
    center_window(changeuser_info,800,600)
    
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
        
    #operator_log.withdraw()#隐藏之前的界面

#获取操作员的用户名和密码用于判断
    operator_name = operator_login_textbox1.get()
    operator_password = operator_login_textbox2.get()

    operator_login_textbox1.delete(0,END)
    operator_login_textbox2.delete(0,END)

    print(operator_name, operator_password)
    opt_login = BE_Function.login(operator_name, operator_password)

    if opt_login == 1:

        operator_log.withdraw()  # 隐藏之前的界面
        operator_log_in=Tk()
        operator_log_in.geometry("500x200")
        operator_log_in.title("Operator")
        center_window(operator_log_in,1600,800)

        #将恢复界面和关闭按钮连接
        operator_log_in.protocol("WM_DELETE_WINDOW", hide)

        button1=Button(operator_log_in,text="Charge",command=charge)#充电按钮
        button1.place(x=130,y=20,width=70,height=25)

        button2=Button(operator_log_in,text="repair",command=repair)#维修
        button2.place(x=130,y=50,width=70,height=25)

        button3=Button(operator_log_in,text="Move",command=move)#更改位置信息（移动车辆）
        button3.place(x=130,y=80,width=70,height=25)
    elif opt_login == 0 or opt_login == 2: info_window("Not an Operator")
    elif opt_login == "NoUserFalse": info_window("No Such Operator")
    else: info_window("Login Error")

    
def charge():#充电功能

    global charge_log
    def hide():#恢复界面
        charge_log.destroy()
        operator_log_in.deiconify()
    
    def charge_car():
        charge_car_name=box1.get()
        charge_info = BE_Function.opt_update_car("charge", charge_car_name)
        if charge_info == "ChargeSuccess": info_window("Successgully")
        elif charge_info == "CarFalse": info_window("Error: No Such Car")
        elif charge_info == "RepairFalse": info_window("Error: Need to Repair First")
        elif charge_info == "RentFalse": info_window("Error: Car In Rent")
        else: info_window("Error: Charge Failed")

        charge_car_info = BE_Function.filter_car("state", "lowpower")
        box2.delete(0,END)
        for car in charge_car_info:
            charge_detail = "Car ID: " + str(car[0]) + " | Car Power: " + str(car[4])
            box2.insert(END, charge_detail)

    operator_log_in.withdraw()#隐藏之前的界面

    charge_log=Tk()
    charge_log.geometry("500x200")
    charge_log.title("Charge ")
    center_window(charge_log,800,600)
    
    #将恢复界面和关闭按钮连接
    charge_log.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(charge_log,text="Car code::")#输入操作车辆编号
    label1.place(x=20,y=20)
    
    global charge_car_name_box
    
    box1=Entry(charge_log,text=0)
    box1.place(x=100,y=20,width=100,height=25)
    
    label2=Label(charge_log, text="Car in low charge:")#显示需要充电的车辆编号
    label2.place(x=20,y=50)
    box2=Listbox(charge_log)
    box2.place(x=150,y=50,width=100,height=50)

    #所有需要充电车辆编号 List
    charge_car_info = BE_Function.filter_car("state", "lowpower")
    for car in charge_car_info:
        charge_detail = "Car ID: " + str(car[0]) + " | Car Power: " + str(car[4])
        box2.insert(END, charge_detail)

    button=Button(charge_log,text="Charge",command=charge_car)
    button.place(x=300,y=20,width=100,height=25)

def repair():#维修界面

    global repair_log
    def hide():#恢复界面
        repair_log.destroy()
        operator_log_in.deiconify()
    
    def repair_car():
        repair_car_name=box1.get()
        repair_info = BE_Function.opt_update_car("repair", repair_car_name)
        if repair_info == "RepairSuccess": info_window("Successgully")
        elif repair_info == "RentFalse": info_window("Error: Car In Rent")
        elif repair_info == "NoRepairFalse": info_window("Error: No Need To Repair")
        elif repair_info == "CarFalse": info_window("Error: No Such Car")
        else: info_window("Error: Move Failed")

        repair_car_info = BE_Function.filter_car("state", "repair")
        box2.delete(0,END)
        for car in repair_car_info:
            repair_detail = "Car ID: " + str(car[0]) + " | Repair Detail: " + car[7]
            box2.insert(END,repair_detail)

    operator_log_in.withdraw()#隐藏之前的界面

    repair_log=Tk()
    repair_log.geometry("500x200")
    repair_log.title("Repair ")
    center_window(repair_log,800,600)

    #将恢复界面和关闭按钮连接
    repair_log.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(repair_log,text="Car code::")#输入操作车辆编号
    label1.place(relx=0.05,rely=0.04)
    
    box1=Entry(repair_log,text=0)
    box1.place(relx=0.15,rely=0.04,relwidth=0.2,relheight=0.05)
    
    label2=Label(repair_log, text="Car in repairing:")#显示需要维修的所有车辆编号
    label2.place(relx=0.05,rely=0.1)
    box2=Listbox(repair_log)
    box2.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.6)

    repair_car_info = BE_Function.filter_car("state", "repair")
    for car in repair_car_info:
        repair_detail = "Car ID: " + str(car[0]) + " | Repair Detail: " + car[7]
        box2.insert(END, repair_detail)

    button=Button(repair_log,text="Repair",command=repair_car)
    button.place(relx=0.5,rely=0.04,relwidth=0.08,relheight=0.06)


def move():  # 移动界面

    global move_log

    def hide():  # 恢复界面
        move_log.destroy()
        operator_log_in.deiconify()

    def move_car():
        move_car_name = box1.get()
        move_car_location = dd1.get()

        '''
        bug:输入 car_name 的时候会同步到 car_location 里面
        '''

        move_result = BE_Function.opt_update_car("move", move_car_name, move_car_location)
        if move_result == "MoveSuccess":
            info_show = "Move Successfully!!! Current location of Car " + move_car_name + " is " + move_car_location
            info_window(info_show)
        elif move_result == "RentFalse":
            info_window("Error: Car In Rent")
        elif move_result == "CarFalse":
            info_window("Error: No such car")
        else:
            info_window("Error: Move Failed")

    operator_log_in.withdraw()  # 隐藏之前的界面

    move_log = Tk()
    move_log.geometry("800x600")
    move_log.title("Movement ")
    center_window(move_log, 1600, 800)

    # 将恢复界面和关闭按钮连接
    move_log.protocol("WM_DELETE_WINDOW", hide)

    label1 = Label(move_log, text="Car code:", font=tkinter_font1)  # 输入操作车辆编号
    label1.place(relx=0.1, rely=0.1)

    box1 = Entry(move_log, text=0)
    box1.place(relx=0.21, rely=0.1, relwidth=0.08, relheight=0.05)

    label2 = Label(move_log, text="New location:", font=tkinter_font1)  # 输入移动车辆后的位置
    label2.place(relx=0.1, rely=0.2)

    dd1 = ttk.Combobox(move_log)  # 可选的位置
    dd1.place(relx=0.24, rely=0.2)
    dd1["values"] = ('Learning Hub', 'Adam Smith Building', 'Boyd Orr Building', 'Main Building')  # 可选车辆类型

    button = Button(move_log, text="Move", command=move_car, font=tkinter_font1)
    button.place(relx=0.32, rely=0.1, relwidth=0.08, relheight=0.05)

'''def move():#移动界面

    global  move_log
    def hide():#恢复界面
        move_log.destroy()
        operator_log_in.deiconify()
    
    def move_car():
        move_car_name=box1.get()
        move_car_location=box2.get()

     
        bug:输入 car_name 的时候会同步到 car_location 里面
    

        move_result = BE_Function.opt_update_car("move", move_car_name, move_car_location)
        if move_result == "MoveSuccess":
            info_show = "Move Successfully!!! Current location of Car " + move_car_name + " is " + move_car_location
            info_window(info_show)
        elif move_result == "RentFalse": info_window("Error: Car In Rent")
        elif move_result == "CarFalse": info_window("Error: No such car")
        else: info_window("Error: Move Failed")

     
        期望 box2 按照下拉列表的方式来显示所有地址，包括：
            1. main building
            2. learning hub
            3. adam smith building
        

    operator_log_in.withdraw()#隐藏之前的界面

    move_log=Tk()
    move_log.geometry("500x200")
    move_log.title("Movement ")
    center_window(move_log,800,600)
    
    #将恢复界面和关闭按钮连接
    move_log.protocol("WM_DELETE_WINDOW", hide)
    
    label1=Label(move_log,text="Car code::")#输入操作车辆编号
    label1.place(x=20,y=20)

    box1=Entry(move_log,text=0)
    box1.place(x=100,y=20,width=100,height=25)

    label2=Label(move_log, text="New location:")#输入移动车辆后的位置
    label2.place(x=20,y=50)
    box2=Entry(move_log)
    box2.place(x=110,y=50,width=100,height=50)

    button=Button(move_log,text="Move",command=move_car)
    button.place(x=300,y=20,width=100,height=25)'''
    
    
#regist_interface=Tk()#注册结果页面
#regist_interface.title("registertion result")
#regist_interface.geometry("500x300")  
   
log_in=Tk()#login interface
log_in.title("LOG IN")
log_in.geometry("800x600")
center_window(log_in,1600,800)
log_in.resizable(True, True)

tkinter_font1 = font.Font(family="Helvetica", size=20, weight="bold")#字体大小

button1=Button(log_in,text="User", command=user_login, font=tkinter_font1)#log in user's interface
button1.place(relx=0.25,rely=0.4,relwidth=0.1,relheight=0.09)

button2=Button(log_in,text="Operator",command=operator_login,font=tkinter_font1)#log in operator's interface
button2.place(relx=0.45,rely=0.40,relwidth=0.1,relheight=0.09)

button3=Button(log_in,text="Manager",command=manager_login,font=tkinter_font1)#log in manager's interface
button3.place(relx=0.65,rely=0.40,relwidth=0.1,relheight=0.09)

#logo=Image.open('./1.png')
#logo=tk.PhotoImage(file="1.png")
#logoimange=Label(log_in,image=logo)
#logoimage.place(x=100,y=50,width=250,height=140)

log_in.mainloop()