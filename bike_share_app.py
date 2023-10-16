#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 21:52:18 2023

@author: renpei
"""


import tkinter as tk
from ttkbootstrap import Style

style = Style()
style = Style(theme="sandstone")# 使用ttkbootstrap的"Sandstone"主题

# 创建全局变量来保存上一个页面的引用
previous_window = None

def open_responsive_window():
    # 创建主窗口
    root = tk.Tk()
    root.title("主页面")
    
    # 设置窗口的初始大小
    root.geometry("800x600")

    # 创建并加载背景图片
    background_image = tk.PhotoImage(file='')  # 请替换为你的背景图片文件路径
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)  # 使图片充满整个窗口

    # 更新窗口以确保适应屏幕大小
    root.update_idletasks()

    # 获取屏幕的宽度和高度
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 计算窗口的新大小，以使其自适应屏幕
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # 设置窗口的新位置和大小
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
   
    # 创建个人账户按钮，放在页面左上角
    account_button = tk.Button(root, text="个人账户", command=open_account_page)
    account_button.grid(row=0, column=0, padx=10, pady=10, sticky='nw')
    
  

 # 创建车辆状态筛选器标签和筛选器，放在页面右上角   
    #status_filter_label = tk.Label(root, text="车辆状态:")
   # status_filter_label.grid(row=0, column=1, padx=(10, 5), pady=5, sticky='ne')

    status_filter = tk.StringVar(root)
    status_options = ["所有状态", "可用", "租用中", "维护中"]  # 可以根据需要添加更多选项
    status_filter.set(status_options[0])  # 默认选择所有状态
    status_dropdown = tk.OptionMenu(root, status_filter, *status_options)
    status_dropdown.grid(row=0, column=3, padx=5, pady=5, sticky='ne')

    # 创建车辆类型筛选器标签和筛选器，放在页面右上角   
    #type_filter_label = tk.Label(root, text="车辆类型:")
    #type_filter_label.grid(row=0, column=3, padx=(10, 5), pady=5, sticky='nw')

    type_filter = tk.StringVar(root)
    type_options = ["所有类型", "城市自行车", "山地自行车", "电动自行车"]  # 可以根据需要添加更多选项
    type_filter.set(type_options[0])  # 默认选择所有类型
    type_dropdown = tk.OptionMenu(root, type_filter, *type_options)
    type_dropdown.grid(row=0, column=4, padx=5, pady=5, sticky='ne')


   # 创建预约车辆按钮，放在页面中心
    reservation_button = tk.Button(root, text="预约车辆", command=lambda: open_reservation_page(root))
    
    # 计算按钮的高度
    button_height = reservation_button.winfo_reqheight()
    
    # 计算按钮的垂直位置，使其居中
    pady_value = (screen_height - button_height) // 2

    # 使用 grid 来设置按钮的位置，将 columnspan 设置为适当的值以使按钮居中
    reservation_button.grid(row=0, column=0, padx=(screen_width // 2 - 100), pady=pady_value, columnspan=4, sticky='n')
    
    # 创建标题标签
    label1 = tk.Label(root, text="取车邮编:")
    label2 = tk.Label(root, text="目的地:")

    # 使用 place 来设置标题标签的位置
    label1.place(x=screen_width // 2 - 150, y=pady_value + button_height + 20)
    label2.place(x=screen_width // 2 - 150, y=pady_value + button_height + 50)

    # 创建两个文本框，放在预约按钮下方
    entry1 = tk.Entry(root)
    entry2 = tk.Entry(root)

    # 设置文本框的位置
    entry1.place(x=screen_width // 2 - 50, y=pady_value + button_height + 20)
    entry2.place(x=screen_width // 2 - 50, y=pady_value + button_height + 50)

    # 启动主循环
    root.mainloop()

def open_reservation_page(root):
    # 创建预约车辆页面
    reservation_window = tk.Tk()
    reservation_window.title("预约车辆")

    # 获取屏幕的宽度和高度
    screen_width = reservation_window.winfo_screenwidth()
    screen_height = reservation_window.winfo_screenheight()

    # 设置预约车辆页面的大小与主页面一致
    reservation_window.geometry(f"{screen_width}x{screen_height}+0+0")

    # 添加车辆详情
    vehicle_details_label = tk.Label(reservation_window, text="附近车辆:")
    vehicle_details_label.pack()

    # 车辆信息
    vehicles_info = [
        {"name": "车辆1", "plate": "ABC 123", "type": "城市自行车", "battery": "80%"},
        {"name": "车辆2", "plate": "XYZ 456", "type": "山地自行车", "battery": "60%"},
    ]

    # 添加返回按钮
    return_button = tk.Button(reservation_window, text="返回", command=lambda: return_to_previous_page(reservation_window))
    return_button.pack()

    # 创建车辆卡片
    def on_card_click(vehicle_info):
        # 保存上一个页面的引用为全局变量
        global previous_window
        previous_window = reservation_window

        # 创建车辆详情页
        vehicle_detail_window = tk.Tk()
        vehicle_detail_window.title("车辆详情")

        # 添加返回按钮
        return_button = tk.Button(vehicle_detail_window, text="返回", command=lambda: return_to_previous_page(vehicle_detail_window))
        return_button.pack()

        # 在车辆详情页显示车辆信息
        detail_label = tk.Label(vehicle_detail_window, text=f"车辆详情 - {vehicle_info['name']}", font=("Arial", 16))
        detail_label.pack()

        plate_detail_label = tk.Label(vehicle_detail_window, text=f"车牌号: {vehicle_info['plate']}")
        plate_detail_label.pack()

        type_detail_label = tk.Label(vehicle_detail_window, text=f"车辆类型: {vehicle_info['type']}")
        type_detail_label.pack()

        battery_detail_label = tk.Label(vehicle_detail_window, text=f"电量: {vehicle_info['battery']}")
        battery_detail_label.pack()
        
        # 添加开始租车按钮
        start_rental_button = tk.Button(vehicle_detail_window, text="开始租车", command=start_rental)
        start_rental_button.pack()
            

        # 启动车辆详情页的主循环
        vehicle_detail_window.mainloop()
   
   
        
   

    for vehicle_info in vehicles_info:
        create_vehicle_card(reservation_window, vehicle_info, on_card_click)

    # 启动预约车辆页面的主循环
    reservation_window.mainloop()
    
# 开始租车的函数，你可以根据需要添加相应的逻辑
def start_rental():
    # 这里可以添加租车的逻辑
    
    pass

def create_vehicle_card(parent, vehicle_info, on_card_click):
    # 创建车辆卡片的 Frame
    card_frame = tk.Frame(parent, bd=2, relief="solid")
    card_frame.pack(pady=10, padx=10, fill="x")

    # 显示车辆信息
    vehicle_label = tk.Label(card_frame, text=vehicle_info["name"], font=("Arial", 12))
    vehicle_label.pack()

    plate_label = tk.Label(card_frame, text=f"车牌号: {vehicle_info['plate']}")
    plate_label.pack()

    type_label = tk.Label(card_frame, text=f"车辆类型: {vehicle_info['type']}")
    type_label.pack()

    battery_label = tk.Label(card_frame, text=f"电量: {vehicle_info['battery']}")
    battery_label.pack()

    # 创建按钮，包含卡片 Frame，实现点击事件
    card_button = tk.Button(card_frame, text="开始租车", command=lambda: on_card_click(vehicle_info))
    card_button.pack()

   
    

def return_to_previous_page(current_window):
    # 关闭当前窗口
    current_window.destroy()

    # 将上一个页面恢复为主窗口
    global previous_window
    previous_window.deiconify()
    
    

def open_account_page():
    # 创建个人账户页面
    account_window = tk.Tk()
    account_window.title("个人账户")

    

    # 添加返回按钮
    return_button = tk.Button(account_window, text="返回", command=lambda: return_to_previous_page(account_window))
    return_button.pack()
    
    # 创建用户信息卡片
    user_info = {"username": "用户名", "account_balance": "$1000"}
    create_user_info_card(account_window, user_info)

    # 创建历史记录数据
    history_data = [
        {"order_number": "001", "order_status": "已完成", "vehicle_number": "12345", "payment_amount": "$10", "usage_time": "1小时"},
        {"order_number": "002", "order_status": "已取消", "vehicle_number": "54321", "payment_amount": "$5", "usage_time": "30分钟"},
    ]

    # 创建历史记录卡片
    for order_info in history_data:
        create_history_card(account_window, order_info)

    # 启动个人账户页面的主循环
    account_window.mainloop()
    pass

def create_user_info_card(parent, user_info):
    # 创建用户信息卡片的 Frame
    user_info_frame = tk.Frame(parent, bd=2, relief="solid")
    user_info_frame.pack(pady=10, padx=10, fill="x")

    # 显示用户信息
    username_label = tk.Label(user_info_frame, text=f"用户名: {user_info['username']}", font=("Arial", 12))
    username_label.pack()

    balance_label = tk.Label(user_info_frame, text=f"账户余额: {user_info['account_balance']}")
    balance_label.pack()

def create_history_card(parent, order_info):
    # 创建历史记录卡片的 Frame
    history_frame = tk.Frame(parent, bd=2, relief="solid")
    history_frame.pack(pady=10, padx=10, fill="x")

    # 显示历史记录信息
    order_label = tk.Label(history_frame, text=f"订单号: {order_info['order_number']}", font=("Arial", 12))
    order_label.pack()

    status_label = tk.Label(history_frame, text=f"订单状态: {order_info['order_status']}")
    status_label.pack()

    vehicle_label = tk.Label(history_frame, text=f"车辆编号: {order_info['vehicle_number']}")
    vehicle_label.pack()

    amount_label = tk.Label(history_frame, text=f"支付金额: {order_info['payment_amount']}")
    amount_label.pack()

    time_label = tk.Label(history_frame, text=f"使用时间: {order_info['usage_time']}")
    time_label.pack()


if __name__ == "__main__":
    open_responsive_window()
