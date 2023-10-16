import sqlite3
import SqlFunction
from tkinter import *

#### 用于 Customer_FE 用户界面的函数

def register(label_name, user_name, password):
    '''
    Customer 首次注册的函数。包含以下逻辑：
        1. 根据输入的 user_name 查询是否存在已有用户
        2. 若存在，则返回 “用户已存在”
        3. 若不存在，则创建新用户，并输入对应的密码
        4. 函数无返回值，会自动在页面展示对应的信息
    '''

    user_info = SqlFunction.get_one_user_info(user_name)

    if user_info == "None":
        registering = SqlFunction.create_user(user_name, password)
        if registering:
            msg = Label(label_name, text="registering successful")
            msg.place(x=20, y=150)
        else:
            msg = Label(label_name, text="registering failed")
            msg.place(x=20, y=150)

    else:
        msg = Label(label_name, text="User is exist")
        msg.place(x=20, y=150)

def filter_car(filter, index):
    '''
    Customer 在页面筛选可用车辆的函数。包含以下逻辑：
        1. 根据 filter 选择筛选条件
        2. 根据 index 选择筛选内容
        2. 函数返回值为二维列表，包括匹配上的所有车辆的所有信息
    '''

    connect = SqlFunction.connect_to_database()
    cursor = connect.cursor()

    try:
        if filter == "state":
            cursor.execute("SELECT * FROM tb_Cars WHERE CarState = ?", (index,))
        elif filter == "type":
            cursor.execute("SELECT * FROM tb_Cars WHERE CarType = ?", (index,))
        elif filter == "location":
            cursor.execute("SELECT * FROM tb_Cars WHERE CarLocation = ?", (index,))
        else:
            cursor.execute("SELECT * FROM tb_Cars")

        filtered_cars = cursor.fetchall()
        connect.close()
        return filtered_cars
    except sqlite3.Error as e:
        print("Error in Filter:", str(e))
        connect.close()
        return []

def rent_start(order_id, car_id, user_name, order_start_time, car_start_location):
    '''
    Customer 租车函数（创建新订单）。包含以下逻辑：
        1. 根据输入的信息查询是否符合租车资格
            i. 若未缴纳租金，则提示 “需要先缴纳租金”
            ii. 若未完成已有订单，则提示 “需要先完成订单”
            iii. 若车辆状态不是 “avaliable”，则提示 “该车辆不可租用”
        2. 若可以租用，则在 tb_Orders 表中创建新订单
        3. 同时，将 car_id 对应的车辆 CarState 改为 “inrent”
        4. 函数返回值为 boolean
    '''
    connect = SqlFunction.connect_to_database()
    cursor = connect.cursor()

    # 检查租车资格
    user_info = SqlFunction.get_one_user_info(user_name)
    car_info = SqlFunction.get_one_car_info(car_id)

    if user_info[3] != 0:
        connect.close()
        return "Haven't paid deposit"

    existing_orders = SqlFunction.get_one_user_orders(user_name)
    for order in existing_orders:
        if order[6] != "end":
            connect.close()
            return "Haven't finished exist order"

    if car_info[6] != "avaliable":
        connect.close()
        return "This is unavaliable"

    try:
        # 创建新订单
        cursor.execute(
            "INSERT INTO tb_Order (OrderID, CarID, UserName, OrderStartTime, OrderState, CarStartLocation) VALUES (?, ?, ?, ?, ?, ?)",
            (order_id, car_id, user_name, order_start_time, 'ongoing', car_start_location))
        connect.commit()
        SqlFunction.update_car_state(car_id, "inrent")
        connect.close()
        return True

    except sqlite3.Error as e:
        print("Error in Create Order:", str(e))
        connect.rollback()
        connect.close()
        return False
