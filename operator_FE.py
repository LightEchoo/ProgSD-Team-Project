 
from tkinter import *
import tkinter as tk
from tkinter import ttk
import operator_BE

#=创建全局变量
previous_window=None

def return_to_previous_page(current_window, previous_window):
    
        current_window.destroy()
        previous_window() 
    
        
#用户登录界面
def user_login():
    global user_log
    user_log=Tk()
    user_log.title("user log in")
    user_log.geometry("500x200")
   
    label1=Label(user_log,text="account:")# input user's account
    label1.place(x=30,y=20)
    textbox1=Entry(user_log,text="")
    textbox1.place(x=150,y=20,width=200,height=25)
   
    label2=Label(user_log,text="password:")
    label2.place(x=30,y=50)
    textbox2=Entry(user_log,text="")
    textbox2.place(x=150,y=50,width=200,height=25)
    user_button1=Button(user_log,text="Register",command=register)
    user_button1.place(x=50,y=110,width=70,height=50)
    user_button2=Button(user_log,text="Log",command=log)
    user_button2.place(x=200,y=110,width=70,height=50)
    
    
    
    
#操作员登录界面
def operator_login():
    global operator_log
    operator_log=Tk()
    operator_log.title("Operator")
    operator_log.geometry("500x200")
    label1=Label(operator_log,text="account:")# input operator's account
    label1.place(x=30,y=20)
    textbox1=Entry(operator_log,text="")
    textbox1.place(x=150,y=20,width=200,height=25)
   
    label2=Label(operator_log,text="password:")
    label2.place(x=30,y=50)
    textbox2=Entry(operator_log,text="")
    textbox2.place(x=150,y=50,width=200,height=25)
    
    
    #user_button1=Button(text="Register",command=register)
    #user_button1.place(x=50,y=110,width=70,height=50)
    operator_button2=Button(operator_log,text="Log",command=operatorlog)#进入操作员界面
    operator_button2.place(x=200,y=110,width=70,height=50)
    
#管理员登录界面
def manager_login(): 
    global manager_log
    manager_log=Tk()
    manager_log.title("Manager")
    manager_log.geometry("500x200")
    label1=Label(manager_log,text="account:")# input user's account
    label1.place(x=30,y=20)
    textbox1=Entry(manager_log,text="")
    textbox1.place(x=150,y=20,width=200,height=25)
    label2=Label(manager_log,text="password:")
    label2.place(x=30,y=50)
    textbox2=Entry(manager_log,text="")
    textbox2.place(x=150,y=50,width=200,height=25)
    
    #user_button1=Button(text="Register",command=register)
    #user_button1.place(x=50,y=110,width=70,height=50)
    user_button2=Button(manager_log,text="Log",command=managerlog)#进入管理员界面
    user_button2.place(x=200,y=110,width=70,height=50)
    
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
    
    
#注册按钮
def register():
    user_log.destroy()#关闭原来的界面
    
    register_interface=Tk()
    register_interface.title("Register")
    register_interface.geometry("500x200")
    label1=Label(register_interface,text="user name:")
    label1.place(x=30,y=20)
    textbox1=Entry(register_interface,text="")
    textbox1.place(x=150,y=20,width=200,height=25)
    label2=Label(register_interface,text="password:")
    label2.place(x=30,y=50)
    textbox2=Entry(register_interface,text="")
    textbox2.place(x=150,y=50,width=200,height=25)
    button=Button(register_interface,text="Regist",command=regist)
    button.place(x=350,y=100)
    
    #返回按钮
    return_button=Button(register_interface,text="Return",command=lambda:return_to_previous_page(register_interface,user_login))
    return_button.place(x=350,y=150,width=50,height=25)
    
#注册结果界面
def regist():
    regist_result=Tk()
    label=Label(regist_interface,text="Successgully regist")#登陆成功
    label.place(x=150,y=100)
    label2=Label2(regist_fault,text="Existed user")#用户已存在
    label2.place(x=150,y=140)
   
#管理员默认界面
def managerlog():
    
    manager_log.destroy()#摧毁管理员登录界面
    
    #新的管理员功能界面
    global managerlog1
    managerlog1=Tk()
    managerlog1.geometry("500x200")
    managerlog1.title("Manager")
    
    button1=Button(managerlog1,text="Report",command=report)#报告按钮
    button1.place(x=30,y=80,width=70,height=50)
    
    button2=Button(managerlog1,text="codition",command=situation)#车辆情况按钮
    button2.place(x=110,y=80,width=70,height=50)
    
    button3=Button(managerlog1,text="User situation",command=change)#更改用户信息
    button3.place(x=190,y=80,width=100,height=50)
    
    #返回按钮
    return_button=Button( managerlog1,text="Return",command=lambda:return_to_previous_page(managerlog1,manager_login))
    return_button.place(x=350,y=150,width=50,height=25)
    
#查看报告界面
def report():
    #摧毁管理员功能界面
    managerlog1.destroy()
    #显示报告界面
    global reportinterface
    reportinterface=Tk()
    reportinterface.geometry("500x200")
    reportinterface.title("Report")
    #选择车辆类型
    label1=Label(reportinterface,text="choose type of vichle")
    dd1=ttk.Combobox(reportinterface)
    dd1.place(x=40,y=50)
    #两种车辆
    dd1["value"]=('bike','scooter')
    dd1_get=dd1.get()
    text1=str(dd1_get)
    dd2=ttk.Combobox(reportinterface)
    dd2.place(x=250,y=50)
    dd2["value"]=('10-12','12-1')
    dd2_get=dd2.get()
    text2=str(dd2_get)
    #更换图片 def changepicture():
    #art=PhotoImage(file='x.file')
    #photobox=Label(reportinterface,image=art)
    #photobox.place(x=100,y=30,width=200,height=150)
    #button=Button(reportinterface,text="see report",command=changepicture)
    
    #返回按钮
    return_button=Button( reportinterface,text="Return",command=lambda:return_to_previous_page(reportinterface,managerlogin))
    return_button.place(x=350,y=150,width=50,height=25)
def report1():#返回界面

    managerlog2.destroy()
    #显示报告界面
    global reportinterface1
    reportinterface1=Tk()
    reportinterface1.geometry("500x200")
    reportinterface1.title("Report")
    #选择车辆类型
    label1=Label(reportinterface1,text="choose type of vichle")
    dd1=ttk.Combobox(reportinterface1)
    dd1.place(x=40,y=50)
    #两种车辆
    dd1["value"]=('bike','scooter')
    dd1_get=dd1.get()
    text1=str(dd1_get)
    dd2=ttk.Combobox(reportinterface1)
    dd2.place(x=250,y=50)
    dd2["value"]=('10-12','12-1')
    dd2_get=dd2.get()
    text2=str(dd2_get)
    #更换图片 def changepicture():
    #art=PhotoImage(file='x.file')
    #photobox=Label(reportinterface,image=art)
    #photobox.place(x=100,y=30,width=200,height=150)
    #button=Button(reportinterface,text="see report",command=changepicture)
    
    #返回按钮
    return_button=Button( reportinterface1,text="Return",command=lambda:return_to_previous_page(reportinterface1,managerlogin))
    return_button.place(x=350,y=150,width=50,height=25)

#生成一个不关闭之前界面的管理员功能页面，用来返回
def managerlogin():
    global managerlog2
    managerlog2=Tk()
    managerlog2.geometry("500x200")
    managerlog2.title("Manager")
    
    button1=Button(managerlog2,text="Report",command=report1)#报告按钮
    button1.place(x=30,y=80,width=70,height=50)
    
    button2=Button(managerlog2,text="codition",command=situation1)#车辆情况按钮
    button2.place(x=110,y=80,width=70,height=50)
    
    button3=Button(managerlog2,text="User situation",command=change1)#更改用户信息
    button3.place(x=190,y=80,width=100,height=50)
    
    #返回按钮
    return_button=Button( managerlog2,text="Return",command=lambda:return_to_previous_page(managerlog2,manager_login))
    return_button.place(x=350,y=150,width=50,height=25)
    
def situation():#车辆使用情况界面
    #关闭默认管理员功能界面
    managerlog1.destroy()
    #车辆使用情况界面
    situationinterface=Tk()
    situationinterface.geometry("500x200")
    situationinterface.title("car coditation")
    
    dd1=ttk.Combobox(situationinterface)
    dd1["value"]=('all','car1','car2')
    dd1.place(x=40,y=20)
    dd1_get=dd1.get()
    text1=str(dd1_get)
    car_list=Listbox(situationinterface)
    car_list.place(x=30,y=50,width=200,height=150)
    button1=Button(situationinterface,text="show")
    button1.place(x=300,y=25)
    
    #返回按钮
    return_button=Button( situationinterface,text="Return",command=lambda:return_to_previous_page(situationinterface,managerlogin))
    return_button.place(x=350,y=150,width=50,height=25)

def situation1():#车辆使用情况界面返回界面
    
    managerlog2.destroy()
    #车辆使用情况界面
    situationinterface1=Tk()
    situationinterface1.geometry("500x200")
    situationinterface1.title("car coditation")
    
    dd1=ttk.Combobox(situationinterface1)
    dd1["value"]=('all','car1','car2')
    dd1.place(x=40,y=20)
    dd1_get=dd1.get()
    text1=str(dd1_get)
    car_list=Listbox(situationinterface1)
    car_list.place(x=30,y=50,width=200,height=150)
    button1=Button(situationinterface1,text="show")
    button1.place(x=300,y=25)
    
    #返回按钮
    return_button=Button( situationinterface1,text="Return",command=lambda:return_to_previous_page(situationinterface1,managerlogin))
    return_button.place(x=350,y=150,width=50,height=25)
def change():#更改用户相关信息
#关闭之前的界面
    managerlog1.destroy()
    #新建更改用户信息界面
    global user_management
    user_management=Tk()
    user_management.geometry("500x200")
    user_management.title("User management")
    button1=Button(user_management,text="Examine",command=examine)#查看用户信息按钮
    button1.place(x=30,y=80,width=60,height=50)
    
    button2=Button(user_management,text="Add",command=adduser)#增加用户按钮
    button2.place(x=110,y=80,width=60,height=50)
    
    button3=Button(user_management,text="Delete",command=deleteuser)#删除用户信息
    button3.place(x=170,y=80,width=60,height=50)
    
    button4=Button(user_management,text="Change",command=changeuser)#更改用户信息
    button4.place(x=230,y=80,width=60,height=50)
    
    #返回按钮
    return_button=Button(user_management,text="Return",command=lambda:return_to_previous_page(user_management,managerlogin))
    return_button.place(x=350,y=150,width=50,height=25)

def change1():#更改用户相关信息返回界面
    managerlog2.destroy()
    #新建更改用户信息界面
    user_management1=Tk()
    user_management1.geometry("500x200")
    user_management1.title("User management")
    button1=Button(user_management1,text="Examine",command=examine)#查看用户信息按钮
    button1.place(x=30,y=80,width=60,height=50)
    
    button2=Button(user_management1,text="Add",command=adduser)#增加用户按钮
    button2.place(x=110,y=80,width=60,height=50)
    
    button3=Button(user_management1,text="Delete",command=deleteuser)#删除用户信息
    button3.place(x=170,y=80,width=60,height=50)
    
    button4=Button(user_management1,text="Change",command=changeuser)#更改用户信息
    button4.place(x=230,y=80,width=60,height=50)
    
    #返回按钮
    return_button=Button( user_management1,text="Return",command=lambda:return_to_previous_page(user_management1,managerlogin))
    return_button.place(x=350,y=150,width=50,height=25)    
def examine():#查看用户信息，输入用户名，查看相关信息

    
    def clean_userinfo():#清楚用户列表内容
         box2.delete(0,END)
    def show():#显示用户信息
         name=box1.get()
         box2.insert(END,name)
         box1.delete(0,END)
    examineinfo=Tk()
    examineinfo.geometry("500x200")
    examineinfo.title("User information ")
    label1=Label(examineinfo,text="Enter user name")#输入查看的用户名
    label1.place(x=20,y=20)
    box1=Entry(examineinfo,text=0)
    box1.place(x=120,y=20,width=100,height=25)
    
    box2=Listbox(examineinfo)#显示相关信息
    box2.place(x=120,y=50,width=150,height=50)
    
    button1=Button(examineinfo,text="show",command=show)#查看按钮
    button1.place(x=250,y=20,width=100,height=25)
    
    button2=Button(examineinfo,text="clean the list",command=clean_userinfo)#清空信息
    button2.place(x=300,y=50,width=100,height=25)
    

    
def adduser():#增加一个用户
    adduser_info=Tk()
    adduser_info.geometry("500x200")
    adduser_info.title("Add user ")
    label1=Label(adduser_info,text="User name:")#想要增加的用户名
    label1.place(x=20,y=20)
    
    box1=Entry(adduser_info,text=0)
    box1.place(x=120,y=20,width=100,height=25)
    
    label2=Label(adduser_info,text="password:")#用户名对应的密码
    label2.place(x=20,y=60)
    
    box2=Entry(adduser_info,text=0)
    box2.place(x=120,y=60,width=100,height=25)
    
    button=Button(adduser_info,text="Add")
    button.place(x=250,y=20)
    

def deleteuser():#删除一个用户
    deleteuser_info=Tk()
    deleteuser_info.geometry("500x200")
    deleteuser_info.title("Delete user ")
    label1=Label(deleteuser_info,text="User name:")#想要删除的用户名
    label1.place(x=20,y=20)
    
    box1=Entry(deleteuser_info,text=0)
    box1.place(x=100,y=20,width=100,height=25)
    
    button=Button(deleteuser_info,text="Delete")
    button.place(x=250,y=20)
def changeuser():#修改用户信息
    changeuser_info=Tk()
    changeuser_info.geometry("500x200")
    changeuser_info.title("Change user information ")
    label1=Label(changeuser_info,text="User name:")#输入想要更改新的用户名
    label1.place(x=20,y=20)
    
    box1=Entry(changeuser_info,text=0)
    box1.place(x=100,y=20,width=100,height=25)
    
    label2=Label(changeuser_info,text="information:")#想要更改的相关信息
    label2.place(x=20,y=50)
    
    box2=Entry(changeuser_info,text=0)
    box2.place(x=120,y=50,width=100,height=25)
    
    button=Button(changeuser_info,text="Change")    
    button.place(x=250,y=20)

def operatorlog():#操作员界面
    operator_log=Tk()
    operator_log.geometry("500x200")
    operator_log.title("Operator")
    button1=Button(operator_log,text="Charge",command=charge)#充电按钮
    button1.place(x=130,y=20,width=70,height=25)
    button2=Button(operator_log,text="repair",command=repair)#维修
    button2.place(x=130,y=50,width=70,height=25)
    button3=Button(operator_log,text="Move",command=move)#更改位置信息（移动车辆）
    button3.place(x=130,y=80,width=70,height=25)
    #返回按钮
    return_button=Button(operator_log,text="Return",command=lambda:return_to_previous_page(operator_log))
    return_button.place(x=300,y=150,width=50,height=25)
def charge():
    charge_log=Tk()
    charge_log.geometry("500x200")
    charge_log.title("Charge ")
    label1=Label(charge_log,text="Car code:")#输入操作车辆编号
    label1.place(x=20,y=20)
    
    box1=Entry(charge_log,text=0)
    car_id = box1.get()
    box1.place(x=100,y=20,width=100,height=25)
    
    label2=Label(charge_log, text="Car in low charge:")#显示需要充电的车辆编号
    label2.place(x=20,y=50)
    box2=Listbox(charge_log)
    box2.place(x=100,y=50,width=100,height=50)
    button=Button(charge_log,text="Charge",command=lambda:operator_BE.charge(charge_log, car_id))
    button.place(x=200,y=20,width=100,height=25)

def repair():
    repair_log=Tk()
    repair_log.geometry("500x200")
    repair_log.title("Repair ")
    
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
def move():
    #移动车辆界面
    move_log=Tk()
    move_log.geometry("500x200")
    move_log.title("Movement ")
    
    label1=Label(move_log,text="Car code::")#输入操作车辆编号
    label1.place(x=20,y=20)
    
    box1=Entry(move_log,text=0)
    box1.place(x=100,y=20,width=100,height=25)
    
    label2=Label(move_log, text="New location:")#输入移动车辆后的位置
    label2.place(x=20,y=50)
    box2=Entry(move_log,text=0)
    box2.place(x=110,y=50,width=100,height=50)
    
    button=Button(repair_log,text="Move",command=move_car)#移动按钮
    button.place(x=100,y=20,width=100,height=25)
    
    
#regist_interface=Tk()#注册结果页面
#regist_interface.title("registertion result")
#regist_interface.geometry("500x300")   

log_in=tk.Tk()#login interface
previous_window=log_in
log_in.title("LOG IN")
log_in.geometry("500x200")
button1=Button(log_in,text="User", command=user_login)#log in user's interface
button1.place(x=30,y=20)
button2=Button(log_in,text="Operator",command=operator_login)#log in operator's interface
button2.place(x=100,y=20)
button3=Button(log_in,text="Manager",command=manager_login)#log in manager's interface
button3.place(x=200,y=20)

log_in.mainloop()


