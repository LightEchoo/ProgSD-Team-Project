#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 05:41:24 2023

@author: liangyuran
"""

import sqlite3

# 连接到数据库文件
def connect_to_database():
    connect = sqlite3.connect('estp_database.db')
    return connect

# 插入新用户
def create_user(username, password, userlocation, usertype='customer', userdebt=0, userdeposit=0):
    connect = connect_to_database()
    cursor = connect.cursor()

    try:
        cursor.execute("INSERT INTO tb_Users (UserName, UserPassword, UserLocation, UserType, UserDebt, UserDeposit) VALUES (?, ?, ?, ?, ?, ?)",
                       (username, password, userlocation, usertype, userdebt, userdeposit))
        connect.commit()
        connect.close()
        return True
    except sqlite3.Error as e:
        print("Error in Create User:", str(e))
        connect.rollback()
        connect.close()
        return False

#更新用户欠款
def update_user_debt(username, userdebt):
    connect = connect_to_database()
    cursor = connect.cursor()
    
    try:
        cursor.execute("UPDATE tb_Users SET UserDebt = ? WHERE UserName = ?", (userdebt, username))
        connect.commit()
        connect.close()
    except sqlite3.Error as e:
        print("Error in Update User Debt:", str(e))
        connect.rollback()
        connect.close()
        return False

#更新用户押金
def update_user_deposit(username, userdeposit):
    connect = connect_to_database()
    cursor = connect.cursor()
    
    try:
        cursor.execute("UPDATE tb_Users SET UserDeposit = ? WHERE UserName = ?", (userdeposit, username))
        connect.commit()
        connect.close()
    except sqlite3.Error as e:
        print("Error in Update User Deposit:", str(e))
        connect.rollback()
        connect.close()
        return False

#更新用户地址
def update_user_location(username, userlocation):
    connect = connect_to_database()
    cursor = connect.cursor()
    
    try:
        cursor.execute("UPDATE tb_Users SET UserLocation = ? WHERE UserName = ?", (userlocation, username))
        connect.commit()
        connect.close()
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
def get_one_user_info(username):
    connect = connect_to_database()
    cursor = connect.cursor()

    try:
        cursor.execute("SELECT * FROM tb_Users WHERE UserName = ?", (username,))
        user_info = cursor.fetchone()
        connect.close()
        return user_info
    except sqlite3.Error as e:
        print("Error in Get One User Info:", str(e))
        connect.close()
        return None

