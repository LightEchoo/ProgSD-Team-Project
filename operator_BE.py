import sqlite3
import SqlFunction
from tkinter import *

#### 用于 Operator_FE 运营员界面的函数

def charge(label_name, car_id):
    '''
    Operator 用于给车辆充电的函数。包含以下逻辑：
        1. 根据输入的 car id，更新数据库表 tb_Car 中对应 car 的 CarPower 字段
        2. 更新成功，则返回信息 “完成充电”
        3. 更新失败，则返回信息 “充电失败”
    '''
    charging = SqlFunction.update_car_power(car_id, 100)
    if charging:
        SqlFunction.update_car_state(car_id, "avaliable")
        msg = Label(label_name, text = "Charging successful")
        msg.place(x = 20, y = 150)
    else:
        msg = Label(label_name, text = "Charging failed")
        msg.place(x = 20, y = 150)

