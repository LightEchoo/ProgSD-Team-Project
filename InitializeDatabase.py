#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 13:03:58 2023

@author: liangyuran
"""
import sqlite3

def initialize_etsp_database():
    # 创建或连接到数据库文件（如果存在则覆盖）
    connect = sqlite3.connect('estp_database.db')

    # 创建一个游标对象
    cursor = connect.cursor()

    try:
        # 删除已存在的表格（如果存在）
        cursor.execute("DROP TABLE IF EXISTS tb_Users")
        cursor.execute("DROP TABLE IF EXISTS tb_Cars")
        cursor.execute("DROP TABLE IF EXISTS tb_Order")

        # 创建tb_Users表格
        cursor.execute('''
            CREATE TABLE tb_Users (
                UserName TEXT PRIMARY KEY NOT NULL,
                UserPassword TEXT NOT NULL,
                UserType TEXT,
                UserDebt INTEGER NOT NULL DEFAULT 0,
                UserDeposit INTEGER NOT NULL DEFAULT 0,
                UserLocation TEXT)
        ''')

        # 创建tb_Cars表格
        cursor.execute('''
            CREATE TABLE tb_Cars (
                CarID INTEGER PRIMARY KEY NOT NULL,
                CarType TEXT NOT NULL,
                CarDescription TEXT,
                CarPrice INTEGER,
                CarPower INTEGER NOT NULL DEFAULT 100,
                CarJourney INTEGER,
                CarState TEXT NOT NULL DEFAULT 'available',
                RepairDetail TEXT,
                CarLocation TEXT)
        ''')

        # 创建tb_Order表格
        cursor.execute('''
            CREATE TABLE tb_Orders (
                OrderID INTEGER PRIMARY KEY NOT NULL,
                CarID INTEGER,
                UserName TEXT,
                OrderStartTime TEXT,
                OrderEndTime TEXT,
                OrderPrice INTEGER,
                OrderState TEXT NOT NULL,
                CarStartLocation TEXT,
                CarEndLocation TEXT)
        ''')

        # 提交更改并关闭连接
        connect.commit()
        connect.close()

        print("Database successfully initialized. Including 3 tables: tb_Users、tb_Cars and tb_Order.")

    except sqlite3.Error as e:
        print("Error in Initialization:", str(e))
        connect.rollback()
        connect.close()


def input_default_data():
    #在数据库中插入默认数据
    # ！！！！注意！！！！！此函数只能调用一次，否则会有主键冲突
    
    connect = sqlite3.connect('estp_database.db')
    cursor = connect.cursor()

    try:
        # 插入初始数据到tb_Users
        users_default_data = [
            ('111', '000', 'manager', 0, 0, 'G11 6QJ'),
            ('222', '000', 'operator', 0, 0, 'G11 6QJ'),
            ('abc', 'abc', 'customer', 0, 1, 'G11 6QJ')
        ]
        cursor.executemany('INSERT INTO tb_Users VALUES (?, ?, ?, ?, ?, ?)', users_default_data)

        # 插入初始数据到tb_Cars
        cars_default_data = [
            (1, 'bike', 'This is a bike', 5, 100, 20, 'available', '', 'G11 6QJ'),
            (2, 'wheel', 'This is a wheel', 2, 100, 15, 'inrent', '', 'G11 6QJ'),
            (3, 'bike', 'This is a bike', 5, 0, 20, 'lowpower', '', 'G11 6QJ'),
            (4, 'bike', 'This is a bike', 5, 50, 20, 'repair', 'body', 'G11 6QJ')

        ]
        cursor.executemany('INSERT INTO tb_Cars VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', cars_default_data)



        # 提交更改并关闭连接
        connect.commit()
        connect.close()

        print("Default data successfully inputed. Including 3 users in tb_Users, and 4 cars in tb_Cars")

    except sqlite3.Error as e:
        print("Error in Input Default Data:", str(e))
        connect.rollback()
        connect.close()
