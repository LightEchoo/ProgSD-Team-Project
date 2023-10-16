#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 14:00:43 2023

@author: renpei
"""


import tkinter as tk
from ttkbootstrap import Style
from tkinter import ttk
from PIL import Image, ImageTk
import time
import threading


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

        # 创建个人账户页面标签
        label = tk.Label(self, text="个人账户页面")
        label.grid(row=0, column=7, padx=10, pady=10,columnspan=3,sticky="n")

        # 创建用户信息卡片
        user_info = {"username": "用户名", "account_balance": "$1000"}
        create_user_info_card(self, user_info)
        
        

        # 创建历史订单记录卡片
        history_data = [
            {"order_number": "001", "order_status": "已完成", "vehicle_number": "12345", "payment_amount": "$10", "usage_time": "1小时"},
            {"order_number": "002", "order_status": "已取消", "vehicle_number": "54321", "payment_amount": "$5", "usage_time": "30分钟"},
        ]
        
        

        for order_info in history_data:
         create_history_card(self, order_info)

       # 创建返回按钮
        return_button = ttk.Button(self, text="返回", command=lambda: controller.show_frame(MainPage))
        return_button.grid(row=2, column=0, padx=10, pady=10,columnspan=3)
 
def create_user_info_card(parent, user_info):
    # 创建用户信息卡片的 Frame
    user_info_frame = tk.Frame(parent, bd=2, relief="solid")
    user_info_frame.grid(row=2, column=7, padx=10, pady=10,columnspan=3,sticky="n")

    # 显示用户信息
    username_label = tk.Label(user_info_frame, text=f"用户名: {user_info['username']}", font=("Arial", 12))
    username_label.grid(row=0, column=0, padx=10, pady=5,columnspan=3)

    balance_label = tk.Label(user_info_frame, text=f"账户余额: {user_info['account_balance']}")
    balance_label.grid(row=1, column=0, padx=10, pady=5,columnspan=3)

def create_history_card(parent, order_info):
    
    # 创建主页面标签
   # label = tk.Label(self, text="历史记录")
   # label.grid(row=0, column=0, padx=10, pady=10)
   
    # 创建历史订单记录卡片的 Frame
    history_frame = tk.Frame(parent, bd=2, relief="solid")
    history_frame.grid(row=4, column=0, padx=10, pady=10)

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
        # 初始化应用程序管理器
        tk.Tk.__init__(self, *args, **kwargs)

        # 设置应用程序主窗口的标题和大小
        self.title("shared e-bikes and e-scooters")
        self.geometry("700x500")

        # 使用ttkbootstrap主题
        self.style = Style(theme="morph")

        # 创建一个字典用于存储不同页面的框架
        self.frames = {}

        # 将各个页面添加到字典中
        for F in (MainPage, AccountPage, ReservationPage, EndOrderPage):
            frame = F(self, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # 显示初始页面
        self.show_frame(MainPage)

    def show_frame(self, cont, vehicle_info=None):
        # 显示指定的页面
        frame = self.frames[cont]
        if vehicle_info is not None:
            frame.set_vehicle_info(vehicle_info)
        frame.tkraise()



class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        # 初始化主页面
        tk.Frame.__init__(self, parent)
        
        # 加载背景图片
        background_image = Image.open("/Users/renpei/Desktop/WechatIMG3256.jpg")  # 替换为你的背景图片路径
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self, image=background_photo)
        background_label.image = background_photo  # 保持对图像的引用
        background_label.place(relwidth=1, relheight=1)

        # 创建主页面标签
       # label = tk.Label(self, text="")
       # label.grid(row=0, column=0, padx=10, pady=10)
            
        # 创建其他三个按钮，使用不同的按钮类型以适配主题
        button1 = ttk.Button(self, text="bike", command=self.button1_click, style="TButton.Success.TButton")
        button1.grid(row=1, column=1, padx=10, pady=10, sticky='nw')

        button2 = ttk.Button(self, text="Ebike", command=self.button1_click, style="TButton.Info.TButton")
        button2.grid(row=1, column=2, padx=10, pady=10, sticky='nw')

        button3 = ttk.Button(self, text="E-scooter", command=self.button1_click, style="TButton.Warning.TButton")
        button3.grid(row=1, column=3, padx=10, pady=10, sticky='nw')

       
        # 创建按钮样式
        style = ttk.Style()
        style.configure("TButton", foreground="white", background="blue", font=("Arial", 12))
        style.map("TButton", foreground=[("active", "blue")])

        # 创建个人账户按钮
        account_button = ttk.Button(self, text="个人账户", command=lambda: controller.show_frame(AccountPage), style="TButton")
        account_button.grid(row=0, column=0, padx=10, pady=10, sticky='nw')

        # 创建一个 Frame 包含文本和筛选器
        filter_frame = tk.Frame(self)
        filter_frame.grid(row=0, column=2, columnspan=3, padx=(10, 5), pady=10, sticky='ne')

        # 创建车辆状态筛选器文本
        status_filter_label = tk.Label(filter_frame, text="车辆状态")
        status_filter_label.grid(row=0, column=3, padx=(0, 5), pady=5)

        status_filter = tk.StringVar(self)
        status_options = ["所有状态", "可用", "租用中", "维护中"]
        status_filter.set(status_options[0])

        # 使用ttkbootstrap的样式
        status_dropdown = ttk.Combobox(filter_frame, textvariable=status_filter, values=status_options, style="TCombobox")
        status_dropdown.grid(row=0, column=1, padx=5, pady=5)

        # 创建一个卡片 Frame 用于包含文本框和按钮
        card_frame = tk.Frame(self, bd=2, relief="solid")
        card_frame.grid(row=2, column=2, padx=10, pady=10, sticky='w')
        
        # 创建取车邮编文本和目的地文本
        label1 = tk.Label(card_frame, text="取车邮编:")
        entry1 = tk.Entry(card_frame)
        label2 = tk.Label(card_frame, text="目的地:")
        entry2 = tk.Entry(card_frame)

        label1.grid(row=0, column=0, padx=10, pady=10)
        entry1.grid(row=0, column=1, padx=10, pady=10)
        label2.grid(row=1, column=0, padx=10, pady=10)
        entry2.grid(row=1, column=1, padx=10, pady=10)

        # 创建预约车辆按钮
        reservation_button = ttk.Button(card_frame, text="预约车辆", command=lambda: controller.show_frame(ReservationPage))
        reservation_button.grid(row=4, column=2, columnspan=3, padx=10, pady=10, sticky='w')
        
        # 设置行和列的权重，使其自适应
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # 创建按钮，点击按钮进入地图页面
        map_button = ttk.Button(self, text="查看地图", command=lambda: controller.show_frame(MapPage))
        map_button.grid(row=1, column=4, padx=10, pady=10, sticky='nw')
        


    def button1_click(self):
        # 处理按钮1的点击事件
        pass
    


       
        
class ReservationPage(tk.Frame):
    def __init__(self, parent, controller):
        # 初始化预约车辆页面
        tk.Frame.__init__(self, parent)
        self.vehicle_info = None
        self.controller = controller
        
        # 创建车辆详情页面标签
        label = tk.Label(self, text="附近车辆")
        label.grid(row=0, column=0, padx=10, pady=10)

       # 创建车辆信息区域
        self.create_vehicle_cards()
               
        # 创建返回按钮
        return_button = ttk.Button(self, text="返回", command=lambda: controller.show_frame(MainPage))
        return_button.grid(row=0, column=3, padx=10, pady=10)

            
    def create_vehicle_card(self, vehicle_info, row, column):
    # 创建车辆卡片，显示车辆信息
      card_frame = tk.Frame(self, bd=2, relief="solid")
      card_frame.grid(row=row, column=column, padx=10, pady=10)


      number_label = tk.Label(card_frame, text=f"车辆编号: {vehicle_info['number']}")
      number_label.grid(row=1, column=0, padx=10, pady=5)

      type_label = tk.Label(card_frame, text=f"车辆类型: {vehicle_info['type']}")
      type_label.grid(row=2, column=0, padx=10, pady=5)

      battery_label = tk.Label(card_frame, text=f"电量: {vehicle_info['battery']}")
      battery_label.grid(row=3, column=0, padx=10, pady=5)

      rental_label = tk.Label(card_frame, text=f"租金: {vehicle_info['rental_price']} ")
      rental_label.grid(row=4, column=0, padx=10, pady=5)

      reserve_button = ttk.Button(card_frame, text="预约", command=lambda info=vehicle_info: self.controller.show_frame(EndOrderPage, info))
      reserve_button.grid(row=5, column=0, padx=10, pady=5)

# 在你的create_vehicle_cards函数中，更新循环以指定行。
    def create_vehicle_cards(self):
    # 模拟或获取车辆信息
      vehicle_info_list = [
        {"name": "车辆1", "number": "V001", "type": "电动车", "battery": "80%", "rental_price": "$10/hour"},
        {"name": "车辆2", "number": "V002", "type": "摩托车", "battery": "65%", "rental_price": "$8/hour"},
        {"name": "车辆2", "number": "V002", "type": "摩托车", "battery": "65%", "rental_price": "$8/hour"},
        {"name": "车辆2", "number": "V002", "type": "摩托车", "battery": "65%", "rental_price": "$8/hour"},
        {"name": "车辆2", "number": "V002", "type": "摩托车", "battery": "65%", "rental_price": "$8/hour"},
    ]
      
    # 定义每行最大列数
      max_columns_per_row = 4
      current_row = 2
      current_column = 0

    # 使用指定的行创建车辆卡片
      for i, vehicle_info in enumerate(vehicle_info_list):
         self.create_vehicle_card(vehicle_info, row=current_row, column=current_column)
         
         # 更新当前列和行
         current_column += 1
         if current_column >= max_columns_per_row:
            current_row += 1
            current_column = 0
    
class EndOrderPage(tk.Frame):
    def __init__(self, parent, controller):
        # 初始化车辆详情页面
        tk.Frame.__init__(self, parent)
        self.vehicle_info = None

        # 创建车辆详情页面标签
        label = tk.Label(self, text="车辆详情页面")
        label.grid(row=0, column=1, padx=10, pady=10)

        # 创建车辆信息标签
        self.vehicle_info_label = tk.Label(self, text="")
        self.vehicle_info_label.grid(row=1, column=0, padx=10, pady=10)

        # 创建返回按钮，使用 controller 的 show_frame 方法返回到前一页
        return_button = ttk.Button(self, text="返回", command=lambda: controller.show_frame(ReservationPage))
        return_button.grid(row=2, column=0, padx=10, pady=10)

        # 创建支付订单按钮
        pay_button = ttk.Button(self, text="支付订单", command=self.show_payment_progress)
        pay_button.grid(row=3, column=0, padx=10, pady=10)

        # 创建图片的缩略图
        image = Image.open("/Users/renpei/Desktop/WechatIMG3255.jpg")  # 请替换为实际图像的文件路径
        image.thumbnail((100, 100))  # 调整图像大小
        photo = ImageTk.PhotoImage(image)

        image_label = tk.Label(self, image=photo)
        image_label.image = photo
        image_label.grid(row=4, column=0, padx=10, pady=10)

        # 创建文本框，显示订单信息
        order_info_text = tk.Text(self, height=6, width=40)
        order_info_text.insert(tk.END, "订单信息:\n订单编号: 12345\n总金额: $50\n")
        order_info_text.grid(row=5, column=0, padx=10, pady=10)

    def set_vehicle_info(self, vehicle_info):
        self.vehicle_info = vehicle_info
        self.vehicle_info_label.config(text=f"车辆编号: {vehicle_info['number']}\n车牌号: {vehicle_info['type']}\n类型: {vehicle_info['battery']}")

    def show_payment_progress(self):
        # 创建支付中的 GIF 图像
        payment_image = Image.open("/Users/renpei/Desktop/Blocks-1s-200px.gif")  # 请替换为实际的 GIF 文件路径
        payment_photo = ImageTk.PhotoImage(payment_image)

        payment_label = tk.Label(self, image=payment_photo)
        payment_label.image = payment_photo
        payment_label.grid(row=4, column=0, padx=10, pady=10)

        # 使用线程进行后台支付操作
        def perform_payment():
            # 模拟支付操作（实际中应根据需求编写）
            time.sleep(3)

            # 显示支付完成信息
            self.show_payment_completion()

        payment_thread = threading.Thread(target=perform_payment)
        payment_thread.start()

        def show_payment_completion(self):
        # 更新支付中的 GIF 图像为支付完成的信息
         payment_label.config(image=None)  # 移除 GIF 图像
         payment_label.config(text="支付完成")  # 显示支付完成文本

    def pay_order(self):
        # 处理支付订单的逻辑，可以根据实际需求编写
        self.show_payment_progress()
        
    
        pass


if __name__ == "__main__":
    app = AppManager()
    app.mainloop()

