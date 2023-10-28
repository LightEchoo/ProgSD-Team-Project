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
import CommonFunction
import SqlFunction
import csv

#Todo: 订单展示
#Todo: 支付订单
#Todo: 更新repair
#Todo: 个人订单展示
#Todo: 租车订单跳转

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
        self.entry_username.insert(0, "Enter mobile number")
        self.entry_username.bind("<FocusIn>", lambda event: self.entry_username.delete(0, tk.END))
        self.entry_username.pack(pady=20)

        # 密码输入框
        self.entry_password = ttk.Entry(center_frame)  # 注意：这里改了变量名，避免和用户名输入框重复
        self.entry_password.insert(0, "enter password")
        self.entry_password.bind("<FocusIn>", lambda event: self.entry_password.delete(0, tk.END))
        self.entry_password.pack(pady=20)

        # 底部图标
        bottom_frame = ttk.Frame(center_frame)
        bottom_frame.pack(pady=20)

        btn_icon1 = ttk.Button(bottom_frame, text="register", command=lambda: controller.show_frame(RegisterPage))
        btn_icon1.grid(row=0, column=0, padx=10)

        # 修改登录按钮，使用 functools.partial 包装 login 方法并传递 controller 参数
        from functools import partial
        btn_login = ttk.Button(bottom_frame, text="Log in", command=partial(self.user_login, controller))
        btn_login.grid(row=0, column=1, padx=10)

    def user_login(self, controller):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # 检查用户名和密码是否为空
        if not username or not password:
            self.error_label.config(text="Empty entry", fg="red")
        else:
            login_result = BE_Function.login(username, password)

            if login_result == 0:
                file = open("user.csv", "w")
                file.write(str(username))
                file.close()
                controller.show_frame(MainPage)
            elif login_result == 1 or login_result == 2:
                self.error_label.config(text="No a customer", fg="red")
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
        self.entry_username.insert(0, "enter user name")
        self.entry_username.bind("<FocusIn>", lambda event: self.entry_username.delete(0, tk.END))
        self.entry_username.pack(pady=20)

        # 密码输入框
        self.entry_password = ttk.Entry(center_frame)  # 注意：这里改了变量名，避免和用户名输入框重复
        self.entry_password.insert(0, "enter password")
        self.entry_password.bind("<FocusIn>", lambda event: self.entry_password.delete(0, tk.END))
        self.entry_password.pack(pady=20)

        # 底部图标
        bottom_frame = ttk.Frame(center_frame)
        bottom_frame.pack(pady=20)

        btn_icon1 = ttk.Button(bottom_frame, text="reture", command=lambda: controller.show_frame(LoginPage))
        btn_icon1.grid(row=0, column=0, padx=10)

        # 修改登录按钮，使用 functools.partial 包装 login 方法并传递 controller 参数
        from functools import partial
        btn_login = ttk.Button(bottom_frame, text="register", command=partial(self.user_register, controller))
        btn_login.grid(row=0, column=1, padx=10)

    def user_register(self, controller):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print("get:",username,password)

        # 检查用户名和密码是否为空
        if not username or not password:
            self.error_label.config(text="Empty entry", fg="red")
        else:
            register_result = BE_Function.register(username, password)
            # print("register:", register_result)

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
        return_button = ttk.Button(self, text="return", command=lambda: controller.show_frame(MainPage))
        return_button.grid(row=0, column=0, padx=10, pady=10)


class AccountPage(tk.Frame):
    def __init__(self, parent, controller):
        # 初始化个人账户页面
        tk.Frame.__init__(self, parent)

        self.controller = controller  # 保存controller作为实例属性

        # 初始化当前行为历史记录的起始行
        self.current_row = 4

        # 创建个人账户页面标签
        label = tk.Label(self, text="AccountPage")
        label.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        # 创建退出账户按钮
        logout_button = ttk.Button(self, text="EXIT", command=self.logout)
        logout_button.grid(row=0, column=5, padx=10, pady=10)

        # 创建用户信息卡片
        user_info = {"username": "username", "account_balance": "$1000"}
        self.create_user_info_card(user_info)

        # 创建历史订单记录卡片
        history_data = [
            {"order_number": "001", "order_status": "completed", "vehicle_number": "12345", "payment_amount": "$10",
             "usage_time": "1小时"},
            {"order_number": "002", "order_status": "Cancelled", "vehicle_number": "54321", "payment_amount": "$5",
             "usage_time": "30分钟"},
        ]

        for order_info in history_data:
            self.create_history_card(order_info)

        # 创建返回按钮
        return_button = ttk.Button(self, text="return", command=lambda: controller.show_frame(MainPage))
        return_button.grid(row=self.current_row + 1, column=0, padx=10, pady=10, columnspan=3)

    def logout(self):
        # 添加退出账户逻辑，返回到登录页面
        self.controller.show_frame(LoginPage)



    def create_user_info_card(self, user_info):
        # 创建用户信息卡片的 Frame
        user_info_frame = tk.Frame(self, bd=2, relief="solid")
        user_info_frame.grid(row=2, column=2, padx=10, pady=10, columnspan=3, sticky="n")

        # 显示用户信息
        username_label = tk.Label(user_info_frame, text=f"username: {user_info['username']}", font=("Arial", 12))
        username_label.grid(row=0, column=0, padx=10, pady=5, columnspan=3)

        balance_label = tk.Label(user_info_frame, text=f"balance: {user_info['account_balance']}")
        balance_label.grid(row=1, column=0, padx=10, pady=5, columnspan=3)

    def create_history_card(self, order_info):
        # 创建历史订单记录卡片的 Frame
        history_frame = tk.Frame(self, bd=2, relief="solid")
        history_frame.grid(row=self.current_row, column=0, padx=10, pady=10, columnspan=3)

        # 更新下一个历史记录的行号
        self.current_row += 2

        # 创建历史记录标签
        label = tk.Label(history_frame, text="history")
        label.grid(row=0, column=0, padx=10, pady=10)

        # 显示历史订单信息
        order_label = tk.Label(history_frame, text=f"order_number: {order_info['order_number']}", font=("Arial", 12))
        order_label.grid(row=0, column=0, padx=10, pady=5)

        status_label = tk.Label(history_frame, text=f"order_status: {order_info['order_status']}")
        status_label.grid(row=1, column=0, padx=10, pady=5)

        vehicle_label = tk.Label(history_frame, text=f"vehicle_number: {order_info['vehicle_number']}")
        vehicle_label.grid(row=2, column=0, padx=10, pady=5)

        amount_label = tk.Label(history_frame, text=f"payment_amount: {order_info['payment_amount']}")
        amount_label.grid(row=3, column=0, padx=10, pady=5)

        time_label = tk.Label(history_frame, text=f"usage_time: {order_info['usage_time']}")
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

        # 添加页面类到字典中
        for F in (LoginPage, MainPage, AccountPage, ReservationPage, EndOrderPage, PaymentPage, RegisterPage, EndPayPage):
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



class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        # 初始化主页面
        tk.Frame.__init__(self, parent)

        # Frame 1: 个人账户
        frame1 = tk.Frame(self)
        frame1.grid(row=0, column=0, padx=10, pady=10, sticky='nw')

        account_button = ttk.Button(frame1, text="AccountPage", command=lambda: controller.show_frame(AccountPage),
                                    style="TButton")
        account_button.grid(row=0, column=0, padx=10, pady=10, sticky='nw')

        # 创建按钮，点击按钮进入地图页面
        map_button = ttk.Button(frame1, text="map", command=lambda: controller.show_frame(MapPage))
        map_button.grid(row=0, column=6, padx=10, pady=10)

        # 中央容器，用于保持内容居中
        center_frame = tk.Frame(self)
        center_frame.place(relx=0.4, rely=0.4, anchor=tk.CENTER)

        # 应用图标和标题
        lbl_title = tk.Label(center_frame, text="Search your vehicle", font=("Arial", 24))
        lbl_title.pack(pady=10)

        # 创建单选按钮及其对应的`StringVar`
        self.selected_option = tk.StringVar()

        option_radio1 = ttk.Radiobutton(center_frame, text="IKEA", variable=self.selected_option, value="IKEA",
                                        compound="left")
        option_radio2 = ttk.Radiobutton(center_frame, text="UofG", variable=self.selected_option, value="UofG",
                                        compound="left")
        option_radio3 = ttk.Radiobutton(center_frame, text="Hospital", variable=self.selected_option, value="Hospital",
                                        compound="left")
        option_radio4 = ttk.Radiobutton(center_frame, text="Glasgow City Center", variable=self.selected_option,
                                        value="Glasgow City Center", compound="left")

        option_radio1.pack(pady=10, anchor="w")
        option_radio2.pack(pady=10, anchor="w")
        option_radio3.pack(pady=10, anchor="w")
        option_radio4.pack(pady=10, anchor="w")

        # 创建预约车辆按钮
        reservation_button = ttk.Button(center_frame, text="reserve",
                                        command=lambda: controller.show_frame(ReservationPage))
        reservation_button.pack(pady=10)

        # 创建按钮，点击按钮进入地图页面
        map_button = ttk.Button(center_frame, text="map", command=lambda: controller.show_frame(MapPage))
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
        return_button = ttk.Button(self, text="return", command=lambda: controller.show_frame(MainPage))
        return_button.grid(row=0, column=1, padx=10, pady=10)

        # 创建按钮样式
        style = ttk.Style()
        style.configure("TButton", foreground="white", background="blue", font=("Arial", 12))
        style.map("TButton", foreground=[("active", "blue")])

        # Frame 2: 按钮区域
        frame2 = tk.Frame(self)
        frame2.grid(row=0, column=0, padx=10, pady=10)

        button1 = ttk.Button(frame2, text="escooter", command=lambda: self.filter_vehicle_type("escooter"),
                             style="TButton.Success.TButton")
        button1.grid(row=0, column=0, padx=10, pady=10, sticky='nw')

        button2 = ttk.Button(frame2, text="ebike", command=lambda: self.filter_vehicle_type("ebike"),
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

        number_label = tk.Label(card_frame, text=f"card_number: {vehicle_info[0]}")
        number_label.grid(row=1, column=0, padx=10, pady=5)

        type_label = tk.Label(card_frame, text=f"car_type: {vehicle_info[1]}")
        type_label.grid(row=2, column=0, padx=10, pady=5)

        battery_label = tk.Label(card_frame, text=f"battery: {vehicle_info[4]}")
        battery_label.grid(row=3, column=0, padx=10, pady=5)

        rental_label = tk.Label(card_frame, text=f"rental: {vehicle_info[3]} ")
        rental_label.grid(row=4, column=0, padx=10, pady=5)

        # 创建“预约”按钮，并根据余额状态添加相应的功能
        '''if balance == 1:
            reserve_button_text = "预约"
        else:
            reserve_button_text = "无押金"
            reserve_button_command = None'''

        reserve_button_command = lambda info=vehicle_info: self.show_reservation_message(info)
        reserve_button = ttk.Button(card_frame, text="reserve", command=reserve_button_command)
        reserve_button.grid(row=5, column=0, padx=10, pady=5)

    def show_reservation_message(self, vehicle_info):
        # 显示预约消息，检查押金并弹出相应消息
        file = open("user.csv", "r")
        login_user = list(file)
        user_info = SqlFunction.get_one_user_info(login_user[0])
        file.close()
        car_location = "Main Building"
        print(user_info)

        rent_result = BE_Function.rent_start(vehicle_info[0], user_info[0], car_location)
        #TODO
        print(rent_result)

        if rent_result == "DepositError":
            # 若未付押金，则需要用户先交押金
            messagebox.showwarning("Insufficient deposit",
                                   "The account deposit is insufficient, please recharge in time")
            # TODO： 跳转支付页面 self.controller.show_frame(PaidPage, vehicle_info)
        elif rent_result == "ExistError":
            # 若存在未完成的订单，则需要用户先结束订单
            messagebox.showwarning("Order not completed",
                                   "There is an uncompleted order, please complete the order first")
            # TODO： 跳转支付页面 self.controller.show_frame(PaidPage, vehicle_info)
        elif rent_result == "UnavaliableError":
            # 若车辆不可用，则换一辆车
            messagebox.showwarning("车辆不可用", "当前车辆不可用，请重新选择。")
            # TODO： 跳转支付页面 self.controller.show_frame(PaidPage, vehicle_info)
        elif rent_result == "RentError":
            # 若租用失败，则重新租用
            messagebox.showwarning("Rental failed", "Rental failed, please try again.")
            # TODO： 跳转支付页面 self.controller.show_frame(PaidPage, vehicle_info)
        else:
            # 租用成功，返回值为 order_id
            messagebox.showinfo("Rental successful", "Your vehicle is unlocked！")
            self.controller.show_frame(EndOrderPage, vehicle_info)


    '''def check_balance(self, vehicle_info):
        # TODO: 获取全局变量 current_user，查询个人账户押金状态
        user_info = SqlFunction.get_one_user_info("abc")
        balance = user_info[4]
        if balance == 1:
            return True
        else:
            return True'''

    def create_vehicle_cards(self):
        # 模拟获取车辆信息
        '''self.vehicle_info_list = [
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
        ]'''

        # 数据格式：(1, 'ebike', 'This is a ebike', 5, 100, 20, 'avaliable', '', 'Learning Hub')
        self.vehicle_info_list = SqlFunction.get_all_cars()

        self.vehicle_info_list = [vehicle for vehicle in self.vehicle_info_list if
                                  vehicle[6] == "available"]

        # 根据选定的车辆类型筛选车辆信息
        if self.selected_vehicle_type:
            self.vehicle_info_list = [vehicle for vehicle in self.vehicle_info_list if
                                      vehicle[1] == self.selected_vehicle_type]

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
        label = tk.Label(self, text="Order in progress")
        label.pack()  # 默认垂直居中显示

        # 创建图片的缩略图
        image = Image.open("images/WechatIMG3255.jpg")
        image.thumbnail((100, 100))  # 调整图像大小
        photo = ImageTk.PhotoImage(image)

        image_label = tk.Label(self, image=photo)
        image_label.image = photo
        image_label.pack()  # 默认垂直居中显示

        # 创建车辆信息标签
        self.vehicle_info_label = tk.Label(self, text="")
        self.vehicle_info_label.pack()  # 默认垂直居中显示

        # TODO: 创建返回按钮，使用 controller 的 show_frame 方法返回到前一页
        # return_button = ttk.Button(self, text="return", command=lambda: controller.show_frame(ReservationPage))
        # return_button.pack()  # 默认垂直居中显示

        # 创建中央容器，用于保持内容居中
        center_frame = tk.Frame(self)
        center_frame.pack(expand=True, fill=tk.BOTH)  # 使用pack布局并扩展以填充整个中央区域

        # 创建按钮容器
        button_frame = tk.Frame(center_frame)
        button_frame.pack()

        # 创建还车按钮
        pay_button = ttk.Button(button_frame, text="return car", command=self.confirm_payment)
        pay_button.pack(side=tk.LEFT, padx=10)  # 左对齐并添加间距

        # 创建report订单按钮
        report_button = ttk.Button(button_frame, text="report", command=self.report_order)
        report_button.pack(side=tk.LEFT, padx=10)  # 左对齐并添加间距

    def set_vehicle_info(self, vehicle_info):
        self.vehicle_info = vehicle_info
        self.vehicle_info_label.config(text=f"vehicle number: {vehicle_info[0]}\n Power: {vehicle_info[4]}")
        '''number_plate: {vehicle_info['type']}\n'''

    def confirm_payment(self):
        login_user = BE_Function.get_login_user()
        order = SqlFunction.get_user_specific_order(login_user[0], "ongoing")
        result = messagebox.askquestion("确认还车", "您确定要还车吗？")
        print(order)

        if result == "yes":
            # 用户确认支付，跳转到PaymentPage
            confirm_result = BE_Function.return_car(order[0])
            print(confirm_result)
            if confirm_result == "Successful":
                self.controller.show_frame(PaymentPage)
            else:
                messagebox.showwarning("归还失败", "归还失败，请重试。")

    def pay_order(self):
        # 在这里添加支付订单的逻辑，例如显示支付进度页面
        self.controller.show_frame(PaymentPage)

    def report_order(self):
        # 处理报错按钮的点击事件
        report_frame = tk.Frame(self)
        report_frame.pack()  # 默认垂直居中显示

        # 添加多选功能的文本显示
        report_label = ttk.Label(report_frame, text="Please select question type:")
        report_label.pack()  # 默认垂直居中显示

        # 定义一个Tkinter整数变量用于存储选择
        selected_problem_var = tk.IntVar()

        # 创建单选按钮
        problem_radio1 = ttk.Radiobutton(report_frame, text="seat post", variable=selected_problem_var, value=1)
        problem_radio2 = ttk.Radiobutton(report_frame, text="frames", variable=selected_problem_var, value=2)
        problem_radio3 = ttk.Radiobutton(report_frame, text="tire", variable=selected_problem_var, value=3)
        problem_radio4 = ttk.Radiobutton(report_frame, text="battery", variable=selected_problem_var, value=3)

        # 放置单选按钮
        problem_radio1.pack()
        problem_radio2.pack()
        problem_radio3.pack()
        problem_radio4.pack()

        # 创建确定按钮
        # 注意这里将命令函数改为self.confirm_report(selected_problem_var, report_frame)
        confirm_button = ttk.Button(report_frame, text="Sure",
                                    command=lambda: self.confirm_report(selected_problem_var, report_frame))
        confirm_button.pack()


def confirm_report(self, problem_var1, problem_var2, problem_var3, problem_var4, report_frame):
    # 处理报错确认按钮的点击事件
    selected_problems = []

    if problem_var1.get():
        selected_problems.append("seat post")
    if problem_var2.get():
        selected_problems.append("frames")
    if problem_var3.get():
        selected_problems.append("tire")
    if problem_var4.get():
        selected_problems.append("battery")

    if selected_problems:
        # 显示选中的问题类型
        report_message = "Question type you selected：" + ", ".join(selected_problems)
        # 跳转到支付页面
        self.controller.show_frame(PaymentPage)
    else:
        report_message = "You have not selected any question type"

    # 弹出消息框显示选中的问题类型
    messagebox.showinfo("Error message", report_message)  # 使用messagebox模块显示消息框

    # 清空问题选择并隐藏报错部分
    problem_var1.set(False)
    problem_var2.set(False)
    problem_var3.set(False)
    report_frame.pack_forget()  # 隐藏报错部分


    
class PaymentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Pay order", font=("Arial", 18))
        label.grid(row=0, column=1, padx=10, pady=10)

        # 车辆信息区域
        vehicle_info_label = tk.Label(self, text=" vehicle_info", font=("Arial", 18))
        vehicle_info_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.vehicle_info = None
        self.vehicle_number_label = tk.Label(self, text="vehicle_number: ", font=("Arial", 12))
        self.vehicle_number_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.vehicle_type_label = tk.Label(self, text="vehicle_type: ", font=("Arial", 12))
        self.vehicle_type_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.vehicle_battery_label = tk.Label(self, text="battery: ", font=("Arial", 12))
        self.vehicle_battery_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.vehicle_duration_label = tk.Label(self, text="vehicle_duration: ", font=("Arial", 12))
        self.vehicle_duration_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        # 订单信息区域
        order_info_label = tk.Label(self, text="order_info", font=("Arial", 18))
        order_info_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")

        self.start_time_label = tk.Label(self, text="order_start_time: ", font=("Arial", 12))
        self.start_time_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")

        self.end_time_label = tk.Label(self, text="order_end_time: ", font=("Arial", 12))
        self.end_time_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")

        self.total_amount_label = tk.Label(self, text="total_amount: ", font=("Arial", 12))
        self.total_amount_label.grid(row=9, column=0, padx=10, pady=5, sticky="w")

        # 车辆照片
        self.vehicle_image_label = tk.Label(self)
        self.vehicle_image_label.grid(row=2, column=1, padx=10, pady=5, rowspan=5, columnspan=2)

        # 确认支付按钮
        confirm_button = ttk.Button(self, text="confirm payment", command=self.confirm_payment)
        confirm_button.grid(row=10, column=1, padx=10, pady=10)

    def set_payment_info(self, vehicle_info, start_time, end_time, total_amount, duration):
        # 设置订单完成页面的信息
        # order 格式：(1001, 1, 'user', '2023-10-28 20:44:19', '2023-10-28 20:44:26', 0.0, 'due', 'Main Building', 'Main Building')
        login_user = BE_Function.get_login_user()
        order = SqlFunction.get_user_specific_order(login_user[0], "due")
        car_info = SqlFunction.get_one_car_info(order[1])
        print(login_user)
        print(order)
        print(car_info)

        self.vehicle_info = car_info
        self.vehicle_number_label.config(text=f"车辆编号: {vehicle_info[0]}")
        self.vehicle_type_label.config(text=f"车辆类型: {vehicle_info[1]}")
        self.vehicle_battery_label.config(text=f"电量: {vehicle_info[4]}")
        #self.vehicle_duration_label.config(text=f"使用总时长: {order[5]} 小时")

        self.start_time_label.config(text=f"订单开始时间: {order[3]}")
        self.end_time_label.config(text=f"订单结束时间: {order[4]}")
        self.total_amount_label.config(text=f"订单总金额: {order[5]}")

        # TODO: 显示车辆照片
        # self.display_vehicle_image(vehicle_info['image_path'])

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
        login_user = BE_Function.get_login_user()
        order = SqlFunction.get_user_specific_order(login_user[0], "due")

        result = messagebox.askquestion("确认支付", "您确定要支付吗？")


        if result == "yes":
            # 用户确认支付，跳转到EndPayPage
            BE_Function.pay_order(order[0])
            self.controller.show_frame(EndPayPage)

        
class EndPayPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Complete order", font=("Arial", 18))
        label.grid(row=0, column=1, padx=10, pady=10)

        # 车辆信息区域
        vehicle_info_label = tk.Label(self, text="vehicle_info", font=("Arial", 18))
        vehicle_info_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.vehicle_info = None
        self.vehicle_number_label = tk.Label(self, text="vehicle_number: ", font=("Arial", 12))
        self.vehicle_number_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.vehicle_type_label = tk.Label(self, text="vehicle_type: ", font=("Arial", 12))
        self.vehicle_type_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.vehicle_battery_label = tk.Label(self, text="battery: ", font=("Arial", 12))
        self.vehicle_battery_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.vehicle_duration_label = tk.Label(self, text="vehicle_duration: ", font=("Arial", 12))
        self.vehicle_duration_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        # 订单信息区域
        order_info_label = tk.Label(self, text=" order_info", font=("Arial", 18))
        order_info_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")

        self.start_time_label = tk.Label(self, text="order_start_time: ", font=("Arial", 12))
        self.start_time_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")

        self.end_time_label = tk.Label(self, text="order_end_time: ", font=("Arial", 12))
        self.end_time_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")

        self.total_amount_label = tk.Label(self, text="total_amount: ", font=("Arial", 12))
        self.total_amount_label.grid(row=9, column=0, padx=10, pady=5, sticky="w")

        # 车辆照片
        self.vehicle_image_label = tk.Label(self)
        self.vehicle_image_label.grid(row=11, column=1, padx=10, pady=5, rowspan=5, columnspan=2)

        # 确认支付按钮
        confirm_button = ttk.Button(self, text="confirm_payment", command=self.confirm_payment)
        confirm_button.grid(row=10, column=1, padx=10, pady=10)

    def set_payment_info(self, vehicle_info, start_time, end_time, total_amount, duration):
        # 设置订单完成页面的信息
        self.vehicle_info = vehicle_info
        self.vehicle_number_label.config(text=f"vehicle_number: {vehicle_info['number']}")
        self.vehicle_type_label.config(text=f"vehicle_type: {vehicle_info['type']}")
        self.vehicle_battery_label.config(text=f"battery: {vehicle_info['battery']}")
        self.vehicle_duration_label.config(text=f"vehicle_duration: {duration} hour")

        self.start_time_label.config(text=f"order_start_time: {start_time}")
        self.end_time_label.config(text=f"order_end_time: {end_time}")
        self.total_amount_label.config(text=f"total_amount: {total_amount}")

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

