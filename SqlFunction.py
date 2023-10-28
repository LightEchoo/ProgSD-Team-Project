#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 05:41:24 2023

@author: liangyuran
"""

import sqlite3

import InitializeDatabase


# 连接到数据库文件
def connect_to_database():
    connect = sqlite3.connect('etsp_database.db')
    return connect

# 插入新用户，用户注册
def create_user(user_name, password):
    connect = connect_to_database()
    cursor = connect.cursor()

    user_type = "customer"
    user_debt = int(0)
    user_deposit = int(0)
    user_location = ""

    try:
        cursor.execute("INSERT INTO tb_Users (UserName, UserPassword, UserType, UserDebt, UserDeposit, UserLocation) VALUES (?, ?, ?, ?, ?, ?)",
                       (user_name, password, user_type, user_debt, user_deposit, user_location))
        connect.commit()
        connect.close()
        return True
    except sqlite3.Error as e:
        print("Error in Create User:", str(e))
        connect.rollback()
        connect.close()
        return False

#更新用户欠款
def update_user_debt(user_name, user_debt):
    connect = connect_to_database()
    cursor = connect.cursor()
    
    try:
        cursor.execute("UPDATE tb_Users SET UserDebt = ? WHERE UserName = ?", (user_debt, user_name))
        connect.commit()
        connect.close()
        return True
    except sqlite3.Error as e:
        print("Error in Update User Debt:", str(e))
        connect.rollback()
        connect.close()
        return False

#更新用户押金
def update_user_deposit(user_name, user_deposit):
    connect = connect_to_database()
    cursor = connect.cursor()
    
    try:
        cursor.execute("UPDATE tb_Users SET UserDeposit = ? WHERE UserName = ?", (user_name, user_deposit))
        connect.commit()
        connect.close()
        return True
    except sqlite3.Error as e:
        print("Error in Update User Deposit:", str(e))
        connect.rollback()
        connect.close()
        return False

#更新用户地址
def update_user_location(user_name, user_location):
    connect = connect_to_database()
    cursor = connect.cursor()
    
    try:
        cursor.execute("UPDATE tb_Users SET UserLocation = ? WHERE UserName = ?", (user_location, user_name))
        connect.commit()
        connect.close()
        return True
    except sqlite3.Error as e:
        print("Error in Update User Location:", str(e))
        connect.rollback()
        connect.close()
        return False

#查询所有用户
def get_all_users():
    connect = connect_to_database()
    cursor = connect.cursor()

    try:
        cursor.execute("SELECT * FROM tb_Users")
        users_info = cursor.fetchall()
        connect.close()
        return users_info
    except sqlite3.Error as e:
        print("Error in Get All Users:", str(e))
        connect.close()
        return []
    
# 查询单个用户信息
def get_one_user_info(user_name):
    connect = connect_to_database()
    cursor = connect.cursor()

    try:
        cursor.execute("SELECT * FROM tb_Users WHERE UserName = ?", (user_name,))
        user_info = cursor.fetchone()
        connect.close()
        return user_info
    except sqlite3.Error as e:
        print("Error in Get One User Info:", str(e))
        connect.close()
        return "None"

'''def get_one_user_type(user_name):
    connect = connect_to_database()
    cursor = connect.cursor()

    try:
        cursor.execute("SELECT UserType FROM tb_Users WHERE UserName = ?", (user_name,))
        user_type = cursor.fetchone()
        connect.close()
        return user_type
    except sqlite3.Error as e:
        print("Error in Get One User Info:", str(e))
        connect.close()
        return "None"'''

# 查看用户的所有订单
def get_one_user_orders(user_name):
    connect = connect_to_database()
    cursor = connect.cursor()

    try:
        cursor.execute("SELECT * FROM tb_Orders WHERE UserName = ?", (user_name,))
        user_orders = cursor.fetchall()
        connect.close()
        return user_orders
    except sqlite3.Error as e:
        print("查询用户订单时发生错误:", str(e))
        connect.close()
        return []

def get_user_specific_order(user_name, data_state):
    connect = connect_to_database()
    cursor = connect.cursor()

    try:
        cursor.execute("SELECT * FROM tb_Orders WHERE UserName = ? AND OrderState = ?", (user_name, data_state))
        order = cursor.fetchone()
        connect.close()
        return order
    except sqlite3.Error as e:
        print("查询用户某类订单时发生错误:", str(e))
        connect.close()
        return []

#更新车辆电量
def update_car_power(car_id, car_power):
    connect = connect_to_database()
    cursor = connect.cursor()

    try:
        cursor.execute("UPDATE tb_Cars SET CarPower = ? WHERE CarId = ?", (car_power, car_id))
        connect.commit()
        connect.close()
        return True
    except sqlite3.Error as e:
        print("Error in Update Car Power:", str(e))
        connect.rollback()
        connect.close()
        return False

#更新车辆状态
def update_car_state(car_id, car_state):
    connect = connect_to_database()
    cursor = connect.cursor()

    try:
        cursor.execute("UPDATE tb_Cars SET CarState = ? WHERE CarId = ?", (car_state, car_id))
        connect.commit()
        connect.close()
        return True
    except sqlite3.Error as e:
        print("Error in Update Car State:", str(e))
        connect.rollback()
        connect.close()
        return False

#更新车辆保修信息
def update_car_repair_detail(car_id, repair_detail):
    connect = connect_to_database()
    cursor = connect.cursor()

    try:
        cursor.execute("UPDATE tb_Cars SET RepairDetail = ? WHERE CarId = ?", (repair_detail, car_id))
        connect.commit()
        connect.close()
        return True
    except sqlite3.Error as e:
        print("Error in Update Car Repair Detail:", str(e))
        connect.rollback()
        connect.close()
        return False

#更新车辆位置
def update_car_location(car_id, car_location):
    connect = connect_to_database()
    cursor = connect.cursor()

    try:
        cursor.execute("UPDATE tb_Cars SET CarLocation = ? WHERE CarId = ?", (car_location, car_id))
        connect.commit()
        connect.close()
        return True
    except sqlite3.Error as e:
        print("Error in Update Car Location:", str(e))
        connect.rollback()
        connect.close()
        return False

#查询所有车辆信息
def get_all_cars():
    connect = connect_to_database()
    cursor = connect.cursor()

    try:
        cursor.execute("SELECT * FROM tb_Cars")
        users_info = cursor.fetchall()
        connect.close()
        return users_info
    except sqlite3.Error as e:
        print("Error in Get All Cars:", str(e))
        connect.close()
        return []

# 查询单个车辆信息
def get_one_car_info(car_id):
    connect = connect_to_database()
    cursor = connect.cursor()

    try:
        cursor.execute("SELECT * FROM tb_Cars WHERE CarId = ?", (car_id,))
        car_info = cursor.fetchone()
        connect.close()
        return car_info
    except sqlite3.Error as e:
        print("Error in Get One Car Info:", str(e))
        connect.close()
        return None

#创建订单
def create_new_order(order_id, car_id, user_name, order_start_time, car_start_location):
    connect = connect_to_database()
    cursor = connect.cursor()

    try:
        cursor.execute("INSERT INTO tb_Orders (OrderId, CarId, UserName, OrderStartTime, OrderState, CarStartLocation) VALUES (?, ?, ?, ?, ?, ?)",
                       (order_id, car_id, user_name, order_start_time, 'ongoing', car_start_location))
        connect.commit()
        connect.close()
        return True
    except sqlite3.Error as e:
        print("Error in Create Order:", str(e))
        connect.rollback()
        connect.close()
        return False

#查询订单信息
def get_one_order_info(order_id):
    connect = connect_to_database()
    cursor = connect.cursor()

    try:
        cursor.execute("SELECT * FROM tb_Orders WHERE OrderId = ?", (order_id,))
        order_info = cursor.fetchone()
        connect.close()
        return order_info
    except sqlite3.Error as e:
        print("Error in Get One Order Info:", str(e))
        connect.close()
        return None

def get_all_orders():
    connect = connect_to_database()
    cursor = connect.cursor()

    try:
        cursor.execute("SELECT * FROM tb_Orders")
        users_info = cursor.fetchall()
        connect.close()
        return users_info
    except sqlite3.Error as e:
        print("Error in Get All Orders:", str(e))
        connect.close()
        return []

#结束订单
def end_one_order(order_id, order_price, order_end_time, car_end_location):
    connect = connect_to_database()
    cursor = connect.cursor()

    try:
        cursor.execute("UPDATE tb_Orders SET OrderEndTime = ?, OrderPrice = ?, OrderState = ?, CarEndLocation = ? WHERE OrderId = ?", (order_end_time, order_price, 'due', car_end_location, order_id))
        connect.commit()
        connect.close()
        return True

    except sqlite3.Error as e:
        print("Error in End order:", str(e))
        connect.rollback()
        connect.close()
        return False

def pay_one_order(order_id):
    connect = connect_to_database()
    cursor = connect.cursor()

    try:
        order_info = get_one_order_info(order_id)

        if order_info:
            # 修改订单状态为 "end"
            cursor.execute("UPDATE tb_Orders SET OrderState = 'end' WHERE OrderID = ?", (order_id,))
            connect.commit()
            connect.close()
            return True
        else:
            connect.close()
            return False

    except sqlite3.Error as e:
        print("Error in pay_order:", str(e))
        connect.rollback()
        connect.close()
        return False

#生成一个新的 OrderID
def generate_new_order_id():
    connect = connect_to_database()
    cursor = connect.cursor()

    cursor.execute("SELECT MAX(OrderID) FROM tb_Orders")
    max_order_id = cursor.fetchone()[0]

    if max_order_id is not None:
        new_order_id = max_order_id + 1
    else:
        new_order_id = 1

    connect.close()
    return new_order_id

