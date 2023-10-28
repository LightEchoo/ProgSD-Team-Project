#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:53:33 2023

@author: renpei
"""

import tkinter as tk
from ttkbootstrap import Style
from tkinter import ttk
from PIL import Image, ImageTk
from functools import partial
import tkinter.messagebox as messagebox
import math
import BE_Function
import SqlFunction



'''class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
      
        # 中央容器，用于保持内容居中
        center_frame = tk.Frame(self)
        center_frame.place(relx=0.4, rely=0.4, anchor=tk.CENTER)

        # 错误消息标签
        self.error_label = tk.Label(center_frame, text="", fg="red")
        self.error_label.pack()

        # 应用图标和标题
        lbl_title = tk.Label(center_frame, text="Sign up", font=("Arial", 24))
        lbl_title.pack(pady=20)

        # 用户名输入框
        self.entry_username = ttk.Entry(center_frame)
        self.entry_username.insert(0, "输入注册的手机号码")
        self.entry_username.bind("<FocusIn>", lambda event: self.entry_username.delete(0, tk.END))
        self.entry_username.pack(pady=10)

        # 密码输入框
        self.entry_password = ttk.Entry(center_frame)  # 注意：这里改了变量名，避免和用户名输入框重复
        self.entry_password.insert(0, "输入密码")
        self.entry_password.bind("<FocusIn>", lambda event: self.entry_password.delete(0, tk.END))
        self.entry_password.pack(pady=10)

        # 底部图标
        bottom_frame = ttk.Frame(center_frame)
        bottom_frame.pack(pady=20)

        btn_register = ttk.Button(bottom_frame, text="注册", command=partial(self.register, controller))
        btn_register.grid(row=0, column=0, padx=10)

        btn_login = ttk.Button(bottom_frame, text="登录", command=lambda: controller.show_frame(LoginPage))
        btn_login.grid(row=0, column=1, padx=10)

    def register(self,controller):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # 检查用户名和密码是否为空
        if not username or not password:
            self.error_label.config(text="Empty username / password", fg="red")

        else:
            register_result = BE_Function.register(username, password)

            # 在这里添加检查用户名和密码是否与数据库匹配的逻辑
            if register_result == "Successful":
                self.error_label.config(text="Register successfully", fg="green")
            elif register_result == "ExistFalse":
                self.error_label.config(text="There is an exist user", fg="red")

        if check_credentials(self, username, password):
            self.error_label.config(text="Register successfully", fg="green")
            return
        else:
            self.error_label.config(text="There is an exist user", fg="red")
            return'''

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        '''# 在代码中添加一个虚假的用户数据库字典
        self.fake_user_database = {
            "user1": "password1",
            "user2": "password2",
            "user3": "password3"
        }'''

        # 中央容器，用于保持内容居中
        center_frame = tk.Frame(self)
        center_frame.place(relx=0.4, rely=0.4, anchor=tk.CENTER)

        # 错误消息标签
        self.error_label =tk.Label(center_frame, text="", fg="red")
        self.error_label.pack()

        # 应用图标和标题
        lbl_title = tk.Label(center_frame, text="Login", font=("Arial", 24))
        lbl_title.pack(pady=20)

        # 用户名输入框
        self.entry_username = ttk.Entry(center_frame)
        self.entry_username.insert(0, "输入手机号码")
        self.entry_username.bind("<FocusIn>", lambda event: self.entry_username.delete(0, tk.END))
        self.entry_username.pack(pady=10)

        # 密码输入框
        self.entry_password = ttk.Entry(center_frame)  # 注意：这里改了变量名，避免和用户名输入框重复
        self.entry_password.insert(0, "输入密码")
        self.entry_password.bind("<FocusIn>", lambda event: self.entry_password.delete(0, tk.END))
        self.entry_password.pack(pady=10)

        # 底部图标
        bottom_frame = ttk.Frame(center_frame)
        bottom_frame.pack(pady=20)

        btn_icon1 = ttk.Button(bottom_frame, text="注册", command=lambda: controller.show_frame(RegisterPage))
        btn_icon1.grid(row=0, column=0, padx=10)

       # 修改登录按钮，使用 functools.partial 包装 login 方法并传递 controller 参数
        from functools import partial
        btn_login = ttk.Button(bottom_frame, text="登录", command=partial(self.user_login, controller))
        btn_login.grid(row=0, column=1, padx=10)

    def user_login(self, controller, login_result=None):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if login_result == "LoginSuccess":
            # 登录成功，设置当前用户
            controller.current_user = username
            controller.show_frame(MainPage)

        # 检查用户名和密码是否为空
        if not username or not password:
            self.error_label.config(text="Empty entry", fg="red")
        else:
            login_result = BE_Function.login(username,password)

            if login_result == "LoginSuccess":
                controller.show_frame(MainPage)
            elif login_result == "NoUserFalse":
                self.error_label.config(text="No such user", fg="red")
            elif login_result == "LoginFalse":
                self.error_label.config(text="Invaild uername / password", fg="red")

        '''
        # 在这里添加检查用户名和密码是否与数据库匹配的逻辑
        if not self.check_credentials(username, password):
            self.error_label.config(text="用户名或密码不正确", fg="red")
            return

       # 登录成功的逻辑
        controller.show_frame(MainPage)

    def check_credentials(self, username, password):
        # 检查用户名是否存在于虚假的用户数据库中，并验证密码是否匹配
        if username in self.fake_user_database and self.fake_user_database[username] == password:
            return True  # 登录成功
        else:
            return False  # 登录失败'''


class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        '''# 在代码中添加一个虚假的用户数据库字典
        self.fake_user_database = {
            "user1": "password1",
            "user2": "password2",
            "user3": "password3"
        }'''

        # 中央容器，用于保持内容居中
        center_frame = tk.Frame(self)
        center_frame.place(relx=0.4, rely=0.4, anchor=tk.CENTER)

        # 错误消息标签
        self.error_label = tk.Label(center_frame, text="", fg="red")
        self.error_label.pack()

        # 应用图标和标题
        lbl_title = tk.Label(center_frame, text="Register", font=("Arial", 24))
        lbl_title.pack(pady=20)

        # 用户名输入框
        self.entry_username = ttk.Entry(center_frame)
        self.entry_username.insert(0, "输入手机号码")
        self.entry_username.bind("<FocusIn>", lambda event: self.entry_username.delete(0, tk.END))
        self.entry_username.pack(pady=10)

        # 密码输入框
        self.entry_password = ttk.Entry(center_frame)  # 注意：这里改了变量名，避免和用户名输入框重复
        self.entry_password.insert(0, "输入密码")
        self.entry_password.bind("<FocusIn>", lambda event: self.entry_password.delete(0, tk.END))
        self.entry_password.pack(pady=10)

        # 底部图标
        bottom_frame = ttk.Frame(center_frame)
        bottom_frame.pack(pady=20)

        btn_icon1 = ttk.Button(bottom_frame, text="返回", command=lambda: controller.show_frame(LoginPage))
        btn_icon1.grid(row=0, column=0, padx=10)

       # 修改登录按钮，使用 functools.partial 包装 login 方法并传递 controller 参数
        from functools import partial
        btn_login = ttk.Button(bottom_frame, text="注册", command=partial(self.user_register, controller))
        btn_login.grid(row=0, column=1, padx=10)

    def user_register(self,controller):
        username = self.entry_username.get()
        password = self.entry_password.get()

        #print("get:",username,password)

        # 检查用户名和密码是否为空
        if not username or not password:
            self.error_label.config(text="Empty entry", fg="red")
        else:
            register_result = BE_Function.register(username,password)
            #print("register:", register_result)

            if register_result == "RegisterSuccessful":
                self.error_label.config(text="Register Successfully", fg="green")
            elif register_result == "ExistFalse":
                self.error_label.config(text="User Exist, Please Login", fg="red")
            else:
                self.error_label.config(text="Error in Register, try again", fg="red")
        
class MapPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # 创建地图
        self.create_map()

        # 返回按钮，点击返回主页面
        return_button = ttk.Button(self, text="返回", command=lambda: controller.show_frame(MainPage))
        return_button.grid(row=0, column=0, padx=10, pady=10)


class AccountPage(tk.Frame):
    def __init__(self, parent, controller):
        # 初始化个人账户页面
        tk.Frame.__init__(self, parent)

        self.controller = controller  # 保存controller作为实例属性

        # 初始化当前行为历史记录的起始行
        self.current_row = 4

        # 创建个人账户页面标签
        label = tk.Label(self, text="个人账户页面")
        label.grid(row=0, column=7, padx=10, pady=10, columnspan=3, sticky="n")

        # 创建退出账户按钮
        logout_button = ttk.Button(self, text="退出账户", command=self.logout)
        logout_button.grid(row=0, column=10, padx=10, pady=10, sticky="n")

        # 创建用户信息卡片
        user_info = {"username": "用户名", "account_balance": "$1000"}
        self.create_user_info_card(user_info)

        # 创建历史订单记录卡片
        history_data = [
            {"order_number": "001", "order_status": "已完成", "vehicle_number": "12345", "payment_amount": "$10", "usage_time": "1小时"},
            {"order_number": "002", "order_status": "已取消", "vehicle_number": "54321", "payment_amount": "$5", "usage_time": "30分钟"},
        ]

        for order_info in history_data:
            self.create_history_card(order_info)

      # 创建返回按钮
        return_button = ttk.Button(self, text="返回", command=lambda: controller.show_frame(MainPage))
        return_button.grid(row=self.current_row + 1, column=0, padx=10, pady=10, columnspan=3)

    def logout(self):
        # 添加退出账户逻辑，返回到登录页面
        self.controller.show_frame(LoginPage)



    def create_user_info_card(self, user_info):
        # 创建用户信息卡片的 Frame
        user_info_frame = tk.Frame(self, bd=2, relief="solid")
        user_info_frame.grid(row=2, column=7, padx=10, pady=10, columnspan=3, sticky="n")

        # 显示用户信息
        username_label = tk.Label(user_info_frame, text=f"用户名: {user_info['username']}", font=("Arial", 12))
        username_label.grid(row=0, column=0, padx=10, pady=5, columnspan=3)

        balance_label = tk.Label(user_info_frame, text=f"账户余额: {user_info['account_balance']}")
        balance_label.grid(row=1, column=0, padx=10, pady=5, columnspan=3)

    def create_history_card(self, order_info):
        # 创建历史订单记录卡片的 Frame
        history_frame = tk.Frame(self, bd=2, relief="solid")
        history_frame.grid(row=self.current_row, column=0, padx=10, pady=10, columnspan=3)

        # 更新下一个历史记录的行号
        self.current_row += 2

        # 创建历史记录标签
        label = tk.Label(history_frame, text="历史记录")
        label.grid(row=0, column=0, padx=10, pady=10)

        # 显示历史订单信息
        order_label = tk.Label(history_frame, text=f"订单号: {order_info['order_number']}", font=("Arial", 12))
        order_label.grid(row=0, column=0, padx=10, pady=5)

        status_label = tk.Label(history_frame, text=f"订单状态: {order_info['order_status']}")
        status_label.grid(row=1, column=0, padx=10, pady=5)

        vehicle_label = tk.Label(history_frame, text=f"车辆编号: {order_info['vehicle_number']}")
        vehicle_label.grid(row=2, column=0, padx=10, pady=5)

        amount_label = tk.Label(history_frame, text=f"支付金额: {order_info['payment_amount']}")
        amount_label.grid(row=3, column=0, padx=10, pady=5)

        time_label = tk.Label(history_frame, text=f"使用时间: {order_info['usage_time']}")
        time_label.grid(row=4, column=0, padx=10, pady=5)



 


class AppManager(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # 设置应用程序主窗口的标题
        self.title("shared e-bikes and e-scooters")

        # 设置窗口大小为 iPhone 12 的大小
        self.geometry("360x700")

        # 居中窗口
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 700) // 2
        self.geometry(f"+{x}+{y}")

        # 使用 ttkbootstrap 主题
        self.style = Style(theme="morph")

        # 创建一个字典用于存储不同页面的框架
        self.frames = {}

        # 全局用户登录状态
        self.user_logged_in = False



        # 添加用于存储当前用户的用户名的属性
        self.current_user = None

        # 添加页面类到字典中
        for F in (LoginPage, MainPage, AccountPage, ReservationPage, EndOrderPage,PaymentPage,RegisterPage,EndPayPage):
            frame = F(self, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # 显示登录页面
        self.show_frame(LoginPage)

    def show_frame(self, page_name, vehicle_info=None):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        
        if vehicle_info:
            frame.set_vehicle_info(vehicle_info)
        
        frame.tkraise()

        # 添加一个方法来设置当前用户的用户名
    def set_current_username(self, username):
        self.current_username = username

        # 添加一个方法来获取当前用户的用户名
    def get_current_username(self):
        return self.current_username

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        # 初始化主页面
        tk.Frame.__init__(self, parent)

        # 获取当前登录的用户名
        current_username = controller.current_user

        # Frame 1: 个人账户
        frame1 = tk.Frame(self)
        frame1.grid(row=0, column=0, padx=10, pady=10, sticky='nw')

        account_button = ttk.Button(frame1, text="个人账户", command=lambda: controller.show_frame(AccountPage),
                                    style="TButton")
        account_button.grid(row=0, column=0, padx=10, pady=10, sticky='nw')

        # 中央容器，用于保持内容居中
        center_frame = tk.Frame(self)
        center_frame.place(relx=0.4, rely=0.4, anchor=tk.CENTER)

        # 应用图标和标题
        lbl_title = tk.Label(center_frame, text="Search your vehicle", font=("Arial", 24))
        lbl_title.pack(pady=20)

        # 创建单选按钮及其对应的`StringVar`
        self.selected_option = tk.StringVar()

        option_radio1 = ttk.Radiobutton(center_frame, text="选项1", variable=self.selected_option, value="选项1")
        option_radio2 = ttk.Radiobutton(center_frame, text="选项2", variable=self.selected_option, value="选项2")
        option_radio3 = ttk.Radiobutton(center_frame, text="选项3", variable=self.selected_option, value="选项3")
        option_radio4 = ttk.Radiobutton(center_frame, text="选项4", variable=self.selected_option, value="选项4")

        option_radio1.pack(pady=5)
        option_radio2.pack(pady=5)
        option_radio3.pack(pady=5)
        option_radio4.pack(pady=5)



        # 创建预约车辆按钮
        reservation_button = ttk.Button(center_frame, text="预约车辆",
                                        command=lambda: controller.show_frame(ReservationPage))
        reservation_button.pack(pady=10)

        # 创建按钮，点击按钮进入地图页面
        map_button = ttk.Button(center_frame, text="查看地图", command=lambda: controller.show_frame(MapPage))
        map_button.pack(pady=10)

        # 设置行和列的权重，使其自适应
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


class ReservationPage(tk.Frame):
    def __init__(self, parent, controller):
        # 初始化预约车辆页面
        tk.Frame.__init__(self, parent)
        self.vehicle_info = None
        self.controller = controller
        self.current_page = 1  # 当前页码
        self.vehicles_per_page = 6  # 每页显示的车辆数量
        self.selected_vehicle_type = None  # 选定的车辆类型

        # 创建车辆信息区域的容器
        self.cards_container = tk.Frame(self)
        self.cards_container.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # 创建车辆详情页面标签
        # label = tk.Label(self, text="附近车辆")
        # label.grid(row=0, column=0, padx=10, pady=10)

        # 创建返回按钮
        return_button = ttk.Button(self, text="返回", command=lambda: controller.show_frame(MainPage))
        return_button.grid(row=0, column=1, padx=10, pady=10)

        # 创建按钮样式
        style = ttk.Style()
        style.configure("TButton", foreground="white", background="blue", font=("Arial", 12))
        style.map("TButton", foreground=[("active", "blue")])

        # Frame 2: 按钮区域
        frame2 = tk.Frame(self)
        frame2.grid(row=0, column=0, padx=10, pady=10)

        button1 = ttk.Button(frame2, text="E-scooter", command=lambda: self.filter_vehicle_type("E-scooter"),
                             style="TButton.Success.TButton")
        button1.grid(row=0, column=0, padx=10, pady=10, sticky='nw')

        button2 = ttk.Button(frame2, text="Ebike", command=lambda: self.filter_vehicle_type("Ebike"),
                             style="TButton.Info.TButton")
        button2.grid(row=0, column=1, padx=10, pady=10, sticky='nw')

        # 创建上一页和下一页按钮
        prev_button = ttk.Button(self, text="上一页", command=self.prev_page)
        prev_button.grid(row=2, column=0, padx=10, pady=10)

        next_button = ttk.Button(self, text="下一页", command=self.next_page)
        next_button.grid(row=2, column=1, padx=10, pady=10)

        # 创建车辆信息区域
        self.create_vehicle_cards()

    def prev_page(self):
        # 切换到上一页
        if self.current_page > 1:
            self.current_page -= 1
            self.create_vehicle_cards()

    def next_page(self):
        # 切换到下一页
        total_pages = math.ceil(len(self.vehicle_info_list) / self.vehicles_per_page)
        if self.current_page < total_pages:
            self.current_page += 1
            self.create_vehicle_cards()

    def filter_vehicle_type(self, vehicle_type):
        # 根据车辆类型筛选车辆信息
        self.selected_vehicle_type = vehicle_type
        self.create_vehicle_cards()

    def create_vehicle_card(self, vehicle_info, row, column):
        # 创建车辆卡片，显示车辆信息
        card_frame = tk.Frame(self.cards_container, bd=2, relief="solid")
        card_frame.grid(row=row, column=column, padx=10, pady=10)

        number_label = tk.Label(card_frame, text=f"车辆编号: {vehicle_info['number']}")
        number_label.grid(row=1, column=0, padx=10, pady=5)

        type_label = tk.Label(card_frame, text=f"车辆类型: {vehicle_info['type']}")
        type_label.grid(row=2, column=0, padx=10, pady=5)

        battery_label = tk.Label(card_frame, text=f"电量: {vehicle_info['battery']}")
        battery_label.grid(row=3, column=0, padx=10, pady=5)

        rental_label = tk.Label(card_frame, text=f"租金: {vehicle_info['rental_price']} ")
        rental_label.grid(row=4, column=0, padx=10, pady=5)
        
        # 获取个人账户余额（假设为balance）
        balance = 8  # 假设余额为8，您需要替换为实际的余额获取方式

        # 创建“预约”按钮，并根据余额状态添加相应的功能
        if balance > 5:
            reserve_button_text = "预约"
            reserve_button_command = lambda info=vehicle_info: self.show_reservation_message(info)
        else:
            reserve_button_text = "账户余额不足"
            reserve_button_command = None

        reserve_button = ttk.Button(card_frame, text=reserve_button_text, command=reserve_button_command)
        reserve_button.grid(row=5, column=0, padx=10, pady=5)

    def show_reservation_message(self, vehicle_info):
        # 显示预约消息，检查余额并弹出相应消息
        if self.check_balance(vehicle_info):
            messagebox.showinfo("预约成功", "您的车辆已开锁！")
            self.controller.show_frame(EndOrderPage, vehicle_info)
        else:
            messagebox.showwarning("余额不足", "账户余额不足，请及时充值。")

    def check_balance(self, vehicle_info):
        # 模拟检查账户余额是否足够，假设账户余额在 vehicle_info 中以 "balance" 键存储
        balance = vehicle_info.get("balance", 0)  # 默认为0，如果没有余额信息的话
        # 根据实际情况替换此处的逻辑
        return True  # 假设余额充足



    def create_vehicle_cards(self):
        # 模拟获取车辆信息
        self.vehicle_info_list = [
            {"name": "车辆1", "number": "V001", "type": "Ebike", "battery": "80%", "rental_price": "$10/hour"},
            {"name": "车辆2", "number": "V002", "type": "E-scooter", "battery": "65%", "rental_price": "$8/hour"},
            {"name": "车辆3", "number": "V003", "type": "Ebike", "battery": "90%", "rental_price": "$12/hour"},
            {"name": "车辆4", "number": "V004", "type": "Ebike", "battery": "75%", "rental_price": "$11/hour"},
            {"name": "车辆5", "number": "V005", "type": "E-scooter", "battery": "70%", "rental_price": "$9/hour"},
            {"name": "车辆6", "number": "V006", "type": "Ebike", "battery": "85%", "rental_price": "$11/hour"},
            {"name": "车辆6", "number": "V006", "type": "Ebike", "battery": "85%", "rental_price": "$11/hour"},
            {"name": "车辆6", "number": "V006", "type": "Ebike", "battery": "85%", "rental_price": "$11/hour"},
            {"name": "车辆6", "number": "V006", "type": "Ebike", "battery": "85%", "rental_price": "$11/hour"},
            {"name": "车辆6", "number": "V006", "type": "Ebike", "battery": "85%", "rental_price": "$11/hour"},
            {"name": "车辆6", "number": "V006", "type": "Ebike", "battery": "85%", "rental_price": "$11/hour"},
        ]

        # 根据选定的车辆类型筛选车辆信息
        if self.selected_vehicle_type:
            self.vehicle_info_list = [vehicle for vehicle in self.vehicle_info_list if
                                       vehicle['type'] == self.selected_vehicle_type]

        # 计算当前页的起始索引和结束索引
        start_index = (self.current_page - 1) * self.vehicles_per_page
        end_index = start_index + self.vehicles_per_page

        # 清空车辆信息区域
        for widget in self.cards_container.grid_slaves():
            widget.grid_forget()

        # 创建当前页的车辆卡片
        current_row = 3
        current_column = 0
        for i, vehicle_info in enumerate(self.vehicle_info_list[start_index:end_index]):
            self.create_vehicle_card(vehicle_info, row=current_row, column=current_column)
            current_column += 1
            if current_column >= 2:
                current_row += 1
                current_column = 0

    
class EndOrderPage(tk.Frame):
    def __init__(self, parent, controller):
        # 初始化车辆详情页面
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.report_frame = None

        self.vehicle_info = None

        # 创建车辆详情页面标签
        label = tk.Label(self, text="订单进行中")
        label.pack()  # 默认垂直居中显示

        # 创建图片的缩略图
        image = Image.open("../../Desktop/WechatIMG3255.jpg")
        image.thumbnail((100, 100))  # 调整图像大小
        photo = ImageTk.PhotoImage(image)

        image_label = tk.Label(self, image=photo)
        image_label.image = photo
        image_label.pack()  # 默认垂直居中显示

        # 创建车辆信息标签
        self.vehicle_info_label = tk.Label(self, text="")
        self.vehicle_info_label.pack()  # 默认垂直居中显示

        # 创建返回按钮，使用 controller 的 show_frame 方法返回到前一页
        #return_button = ttk.Button(self, text="返回", command=lambda: controller.show_frame(ReservationPage))
        #return_button.pack()  # 默认垂直居中显示

        # 创建中央容器，用于保持内容居中
        center_frame = tk.Frame(self)
        center_frame.pack(expand=True, fill=tk.BOTH)  # 使用pack布局并扩展以填充整个中央区域

        # 创建按钮容器
        button_frame = tk.Frame(center_frame)
        button_frame.pack()

        # 创建还车按钮
        pay_button = ttk.Button(button_frame, text="还车", command=self.confirm_payment)
        pay_button.pack(side=tk.LEFT, padx=10)  # 左对齐并添加间距

        # 创建report订单按钮
        report_button = ttk.Button(button_frame, text="报错", command=self.report_order)
        report_button.pack(side=tk.LEFT, padx=10)  # 左对齐并添加间距

    def set_vehicle_info(self, vehicle_info):
        self.vehicle_info = vehicle_info
        self.vehicle_info_label.config(text=f"车辆编号: {vehicle_info['number']}\n车牌号: {vehicle_info['type']}\n电量: {vehicle_info['battery']}")



    
    def confirm_payment(self):
    # 弹出确认预定的消息框，进入订单开始
        result = messagebox.askquestion("确认还车", "您确定要还车吗？")
        

        if result == "yes":
        # 用户确认支付，跳转到PaymentPage
            self.controller.show_frame(PaymentPage)
    
    def pay_order(self):
        # 在这里添加支付订单的逻辑，例如显示支付进度页面
        self.controller.show_frame(PaymentPage)

    def report_order(self):
        # 处理报错按钮的点击事件
        report_frame = tk.Frame(self)
        report_frame.pack()  # 默认垂直居中显示

        # 添加多选功能的文本显示
        report_label = ttk.Label(report_frame, text="请选择问题类型:")
        report_label.pack()  # 默认垂直居中显示

        # 创建多选框
        problem_var1 = tk.BooleanVar()
        problem_var2 = tk.BooleanVar()
        problem_var3 = tk.BooleanVar()

        problem_check1 = ttk.Checkbutton(report_frame, text="问题类型1", variable=problem_var1)
        problem_check2 = ttk.Checkbutton(report_frame, text="问题类型2", variable=problem_var2)
        problem_check3 = ttk.Checkbutton(report_frame, text="问题类型3", variable=problem_var3)

        problem_check1.pack()
        problem_check2.pack()
        problem_check3.pack()

        # 创建确定按钮
        confirm_button = ttk.Button(report_frame, text="确定",
                                    command=lambda: self.confirm_report(problem_var1, problem_var2, problem_var3, report_frame))
        confirm_button.pack()

    def confirm_report(self, problem_var1, problem_var2, problem_var3, report_frame):
        # 处理报错确认按钮的点击事件
        selected_problems = []

        if problem_var1.get():
            selected_problems.append("问题类型1")
        if problem_var2.get():
            selected_problems.append("问题类型2")
        if problem_var3.get():
            selected_problems.append("问题类型3")

        if selected_problems:
            # 显示选中的问题类型
            report_message = "您选择的问题类型：" + ", ".join(selected_problems)
            # 跳转到支付页面
            self.controller.show_frame(PaymentPage)
        else:
            report_message = "您未选择任何问题类型。"

        # 弹出消息框显示选中的问题类型
        messagebox.showinfo("报错信息", report_message)  # 使用messagebox模块显示消息框

        # 清空问题选择并隐藏报错部分
        problem_var1.set(False)
        problem_var2.set(False)
        problem_var3.set(False)
        report_frame.pack_forget()  # 隐藏报错部分
        


    
class PaymentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="支付订单", font=("Arial", 18))
        label.grid(row=0, column=1, padx=10, pady=10)

        # 车辆信息区域
        vehicle_info_label = tk.Label(self, text="车辆信息", font=("Arial", 18))
        vehicle_info_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.vehicle_info = None
        self.vehicle_number_label = tk.Label(self, text="车辆编号: ", font=("Arial", 12))
        self.vehicle_number_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.vehicle_type_label = tk.Label(self, text="车辆类型: ", font=("Arial", 12))
        self.vehicle_type_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.vehicle_battery_label = tk.Label(self, text="电量: ", font=("Arial", 12))
        self.vehicle_battery_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.vehicle_duration_label = tk.Label(self, text="使用总时长: ", font=("Arial", 12))
        self.vehicle_duration_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        # 订单信息区域
        order_info_label = tk.Label(self, text="订单信息", font=("Arial", 18))
        order_info_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")


        self.start_time_label = tk.Label(self, text="订单开始时间: ", font=("Arial", 12))
        self.start_time_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")

        self.end_time_label = tk.Label(self, text="订单结束时间: ", font=("Arial", 12))
        self.end_time_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")

        self.total_amount_label = tk.Label(self, text="订单总金额: ", font=("Arial", 12))
        self.total_amount_label.grid(row=9, column=0, padx=10, pady=5, sticky="w")

        # 车辆照片
        self.vehicle_image_label = tk.Label(self)
        self.vehicle_image_label.grid(row=2, column=1, padx=10, pady=5, rowspan=5, columnspan=2)

        # 确认支付按钮
        confirm_button = ttk.Button(self, text="支付订单", command=self.confirm_payment)
        confirm_button.grid(row=10, column=1, padx=10, pady=10)
  
       

    def set_payment_info(self, vehicle_info, start_time, end_time, total_amount, duration):
        # 设置订单完成页面的信息
        self.vehicle_info = vehicle_info
        self.vehicle_number_label.config(text=f"车辆编号: {vehicle_info['number']}")
        self.vehicle_type_label.config(text=f"车辆类型: {vehicle_info['type']}")
        self.vehicle_battery_label.config(text=f"电量: {vehicle_info['battery']}")
        self.vehicle_duration_label.config(text=f"使用总时长: {duration} 小时")

        self.start_time_label.config(text=f"订单开始时间: {start_time}")
        self.end_time_label.config(text=f"订单结束时间: {end_time}")
        self.total_amount_label.config(text=f"订单总金额: {total_amount}")

        # 显示车辆照片
        self.display_vehicle_image(vehicle_info['image_path'])

    def display_vehicle_image(self, image_path):
        # 显示车辆照片
        try:
            image = Image.open("../../Desktop/WechatIMG3255.jpg")
            image.thumbnail((200, 200))  # 调整图像大小
            photo = ImageTk.PhotoImage(image)

            self.vehicle_image_label.config(image=photo)
            self.vehicle_image_label.image = photo
        except Exception as e:
            print(f"Error displaying image: {e}")

    def confirm_payment(self):
        result = messagebox.askquestion("确认支付", "您确定要支付吗？")
            

        if result == "yes":
            # 用户确认支付，跳转到EndPayPage
           self.controller.show_frame(EndPayPage)

        
class EndPayPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="完成订单", font=("Arial", 18))
        label.grid(row=0, column=1, padx=10, pady=10)

        # 车辆信息区域
        vehicle_info_label = tk.Label(self, text="车辆信息", font=("Arial", 18))
        vehicle_info_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.vehicle_info = None
        self.vehicle_number_label = tk.Label(self, text="车辆编号: ", font=("Arial", 12))
        self.vehicle_number_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.vehicle_type_label = tk.Label(self, text="车辆类型: ", font=("Arial", 12))
        self.vehicle_type_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.vehicle_battery_label = tk.Label(self, text="电量: ", font=("Arial", 12))
        self.vehicle_battery_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.vehicle_duration_label = tk.Label(self, text="使用总时长: ", font=("Arial", 12))
        self.vehicle_duration_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        # 订单信息区域
        order_info_label = tk.Label(self, text="订单信息", font=("Arial", 18))
        order_info_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")


        self.start_time_label = tk.Label(self, text="订单开始时间: ", font=("Arial", 12))
        self.start_time_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")

        self.end_time_label = tk.Label(self, text="订单结束时间: ", font=("Arial", 12))
        self.end_time_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")

        self.total_amount_label = tk.Label(self, text="订单总金额: ", font=("Arial", 12))
        self.total_amount_label.grid(row=9, column=0, padx=10, pady=5, sticky="w")

        # 车辆照片
        self.vehicle_image_label = tk.Label(self)
        self.vehicle_image_label.grid(row=11, column=1, padx=10, pady=5, rowspan=5, columnspan=2)

        # 确认支付按钮
        confirm_button = ttk.Button(self, text="确认订单", command=self.confirm_payment)
        confirm_button.grid(row=10, column=1, padx=10, pady=10)

    def set_payment_info(self, vehicle_info, start_time, end_time, total_amount, duration):
        # 设置订单完成页面的信息
        self.vehicle_info = vehicle_info
        self.vehicle_number_label.config(text=f"车辆编号: {vehicle_info['number']}")
        self.vehicle_type_label.config(text=f"车辆类型: {vehicle_info['type']}")
        self.vehicle_battery_label.config(text=f"电量: {vehicle_info['battery']}")
        self.vehicle_duration_label.config(text=f"使用总时长: {duration} 小时")

        self.start_time_label.config(text=f"订单开始时间: {start_time}")
        self.end_time_label.config(text=f"订单结束时间: {end_time}")
        self.total_amount_label.config(text=f"订单总金额: {total_amount}")

        # 显示车辆照片
        self.display_vehicle_image(vehicle_info['image_path'])

    def display_vehicle_image(self, image_path='WechatIMG3255.jpg'):
        # 显示车辆照片
        try:
            image = Image.open("WechatIMG3255.jpg")
            image.thumbnail((200, 200))  # 调整图像大小
            photo = ImageTk.PhotoImage(image)

            self.vehicle_image_label.config(image=photo)
            self.vehicle_image_label.image = photo
        except Exception as e:
            print(f"Error displaying image: {e}")

    def confirm_payment(self):
        # 在这里添加确认支付的逻辑，例如处理支付请求
        # 确认支付后可以显示支付成功的信息，更新订单状态等
        # 完成支付后，可以跳转到其他页面，例如主页或订单历史页面
        # 暂时只是跳转到主页
        self.controller.show_frame(MainPage)
        


if __name__ == "__main__":
    app = AppManager()
    app.mainloop()

