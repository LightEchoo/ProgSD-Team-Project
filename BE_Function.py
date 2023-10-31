import sqlite3
import SqlFunction
from tkinter import *
import CommonFunction
from datetime import datetime, timedelta

#### 用于 Customer_FE 用户界面的函数 ####

def register(user_name, password):
    '''
    Customer 首次注册的函数。包含以下逻辑：
        1. 根据输入的 user_name 查询是否存在已有用户
        2. 若存在，则返回 “用户已存在”
        3. 若不存在，则创建新用户，并输入对应的密码
        4. 函数无返回值，会自动在页面展示对应的信息
    '''

    user_info = SqlFunction.get_one_user_info(user_name)
    #print(user_info)

    if user_info == None:
        registering = SqlFunction.create_user(user_name, password)
        if registering:
            return "RegisterSuccessful"
        else:
            return "RegisterFalse"
    else:
        return "ExistFalse"

def login(user_name, password):
    '''
    Customer 登录函数。包含以下逻辑：
        1. 根据输入的 user_name，pwd 查询是否存在已有用户，判断用户密码是否正确
        2. 若正确，则返回 True 并跳转下一个界面
        3. 若用户不存在，则返回用户不存在
        4. 若密码错误，则返回密码错误
    '''

    user_info = SqlFunction.get_one_user_info(user_name)

    if user_info == None:
        return "NoUserFalse"
    else:
        if user_info[1] == password:
            if user_info[2] == "customer":
                return 0
            elif user_info[2] == "operator":
                return 1
            elif user_info[2] == "manager":
                return 2
        else:
            return "LoginFalse"

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
        if len(filtered_cars) == 0:
            return "None"
            connect.close()
        else:
            '''
            array = []
            for car in filtered_cars:
                array.append(car)
            '''
            connect.close()
            return filtered_cars

    except sqlite3.Error as e:
        print("Error in Filter:", str(e))
        connect.close()
        return []

def save_loaction(user_name, location):
    '''
    将用户当前地址存到 tb_Users 当前用户的 location 字段中：
    1. 若存储成功，返回 “Successful”
    2. 若失败，则返回 “SaveError”
    '''
    if SqlFunction.update_user_location(user_name, location):
        return "Successful"
    else:
        return "SaveError"

def rent_start(car_id, user_name):
    '''
    Customer 租车函数（创建新订单）。包含以下逻辑：
        1. 根据输入的信息查询是否符合租车资格
            i. 若未缴纳租金，则提示 “需要先缴纳租金”
            ii. 若未完成已有订单，则提示 “需要先完成订单”
            iii. 若车辆状态不是 “avaliable”，则提示 “该车辆不可租用”
        2. 若可以租用，则在 tb_Orders 表中创建新订单
        3. 同时，将 car_id 对应的车辆 CarState 改为 “inrent”
        4. 函数返回值为 String 字段
    '''
    connect = SqlFunction.connect_to_database()

    # 检查租车资格
    user_info = SqlFunction.get_one_user_info(user_name)
    car_info = SqlFunction.get_one_car_info(car_id)
    #print(user_info)
    #print(car_info)

    if user_info[3] != 0:
        connect.close()
        return "DepositError"

    existing_orders = SqlFunction.get_one_user_orders(user_name)
    for order in existing_orders:
        if order[6] == "ongoing":
            connect.close()
            return "OngoingError"
        elif order[6] == "due":
            connect.close()
            return "PayError"

    if str(car_info[6]) != 'available':
        connect.close()
        return "UnavaliableError"

    try:
        order_id = SqlFunction.generate_new_order_id()
        order_start_time = CommonFunction.get_current_time()

        SqlFunction.create_new_order(order_id, car_id, user_name, order_start_time, user_info[5])
        SqlFunction.update_car_state(car_id, "inrent")

        connect.close()
        return order_id, order_start_time

    except sqlite3.Error as e:
        print("Error in Create Order:", str(e))
        return "RentError"

def return_car(order_id):
    '''
    Customer 还车函数。包含以下逻辑：
    1. 根据对应的order_id获取订单信息，包括 car_id，user_id，order_start_time
    2. 修改 order_id 对应的 OrderState 为 “due”，OrderEndTime 为 order_end_time, CarEndLocation 为 car_end_location
    3. 按照 order 信息中的 order_start_time 和参数中的 order_end_time 计算时长 hour
    4. 根据 car_id 获取 CarPower 和 CarPrice，按照 CarPower - hour*10 的方式计算 left_power，不满 1h 按 1h 计算，left_power 最小为 0
    5. 根据 CarPrice * hour 获取 OrderPrice
    5. 更新 car_id 对应车辆的 CarPower 为 left_power
    6. 若 left_power < 20，更新 car_id 对应车辆的 CarState 为 “lowpower”
    7. 函数返回值为 boolean
    '''
    order_end_time = CommonFunction.get_current_time()
    car_end_location = CommonFunction.generate_end_location()
    try:
        order_info = SqlFunction.get_one_order_info(order_id)

        if order_info is None:
            return False

        user_id = order_info[2]
        car_id = order_info[1]
        order_start_time = order_info[3]

        car_info = SqlFunction.get_one_car_info(car_id)
        car_price = car_info[3]

        start_time = datetime.strptime(order_start_time, "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(order_end_time, "%Y-%m-%d %H:%M:%S")
        hour = (end_time - start_time).seconds // 3600

        order_price = int(hour * car_price)
        SqlFunction.end_one_order(order_id, order_price, order_end_time, car_end_location)

        car_power = car_info[4]
        left_power = max(car_power - hour * 10, 0)

        SqlFunction.update_car_power(car_id,left_power)
        SqlFunction.update_user_debt(user_id, order_price)

        if left_power < 20:
            SqlFunction.update_car_state(car_id, "lowpower")

        return "Successful"

    except sqlite3.Error as e:
        print("Error Return Car:", str(e))
        return "ReturnError"

def repair(order_id, repair_detail):
    '''
    Customer 报修函数。包含以下逻辑：
    1. 根据对应的order_id获取订单信息，包括 car_id，user_id，order_start_time
    2. 修改 order_id 对应的 OrderState 为 “due”，OrderEndTime 为 order_end_time, CarEndLocation 为 car_end_location
    3. 根据 car_id  更新对应车辆的 CarState 为 “repair”，RepairDetail 为 repair_detail
    4. 函数返回值为 boolean
    '''
    order_end_time = CommonFunction.get_current_time()
    car_end_location = CommonFunction.generate_end_location()

    try:
        order_info = SqlFunction.get_one_order_info(order_id)

        if order_info is None:
            return "OrderError"

        car_id = order_info[1]
        user_id = order_info[2]
        order_start_time = order_info[3]

        car_info = SqlFunction.get_one_car_info(car_id)
        car_price = car_info[3]

        start_time = datetime.strptime(order_start_time, "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(order_end_time, "%Y-%m-%d %H:%M:%S")
        hour = (end_time - start_time).seconds // 3600
        order_price = int(hour * car_price)

        SqlFunction.end_one_order(order_id, order_price, order_end_time, car_end_location)
        SqlFunction.update_car_state(car_id, "repair")
        SqlFunction.update_car_repair_detail(car_id, repair_detail)
        SqlFunction.update_user_debt(user_id, order_price)
        return "Successful"

    except sqlite3.Error as e:
        print("Error Repair:", str(e))
        return "ReportError"

def pay_order(order_id):
    '''
    1. 根据输入的 order_id 查询对应的订单
    2. 修改状态 OrderState 为 “end”
    3. 函数返回值为 boolean
    '''
    try:
        order_info = SqlFunction.get_one_order_info(order_id)
        SqlFunction.pay_one_order(order_id)
        SqlFunction.update_user_debt(order_info[3], 0)

    except sqlite3.Error as e:
        print("Error Pay Car:", str(e))
        return False


#### 用于 Operator_F›E 运营员界面的函数 ####
def opt_update_car(update_action, car_id, car_location = "Main Building"):
    '''
    Operator 用于更新车辆状态的方法。包含以下逻辑：
        1. 充电：根据 id 更新电量 & 状态
        2. 修复：根据 id 更新状态
        3. 移车：根据 id 更新位置
        4. 返回值为 boolean
    '''
    try:
        car_info = SqlFunction.get_one_car_info(car_id)
        if car_info:

            #充电
            if update_action == "charge":
                if car_info[6] == "repair":
                    return "RepairFalse"
                elif car_info[6] == "inrent":
                    return "RentFalse"
                else:
                    charging = SqlFunction.update_car_power(car_id, 100)

                    if charging:
                        SqlFunction.update_car_state(car_id, "avaliable")
                        return "ChargeSuccess"
                    else:
                        return "ChargeFalse"

            #报修
            elif update_action == "repair":
                if car_info[6] == "repair":
                    repairing = SqlFunction.update_car_state(car_id, "avaliavle")
                    if repairing == True:
                        return "RepairSuccess"
                    else:
                        return "RepairFailed"
                elif car_info[6] == "inrent":
                    return "RentFalse"
                else:
                    return "NoRepairFalse"

            #移车
            elif update_action == "move":
                if car_info[6] == "inrent":
                    return "RentFalse"
                else:
                    SqlFunction.update_car_location(car_id, car_location)
                    return "MoveSuccess"

            else:
                return False

        else:
            return "CarFalse"

    except sqlite3.Error as e:
        print("Error Update Car:", str(e))
        return False

'''def get_login_user():
    file = open("user.csv", "r")
    login_user = [line.strip() for line in file.readlines()]
    file.close()
    user_info = SqlFunction.get_one_user_info(login_user[0])
    return user_info

def get_location():
    file = open("user.csv", "r")
    global_info = list(file)
    file.close()
    if len(global_info) > 1:
        return global_info[-1]
    else:
        return "NoLocation"'''