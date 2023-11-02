import random
import sqlite3
import string
from datetime import datetime, timedelta

import pandas as pd

# 车辆类型
VEHICLE_TYPE = ['ebike', 'escooter']
# 车辆状态
VEHICLE_STATE_L = ['available', 'inrent', 'lowpower', 'repair']

# 地点位置list
LOCATIONS = ["IKEA", "Hospital", "UofG", "Square", "City Center"]

REPAIR_TYPE = ['None', 'seat post', 'frames', 'tire', 'battery']

ORDER_STATE = ['ongoing', 'due', 'end']

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

USER_TEST_DATA = {
    'UserName': ['manager', 'operator', 'user', 'user1'],
    'UserPassword': ['000', '000', '000', '000'],
    'UserType': ['manager', 'operator', 'customer', 'customer'],
    'UserDebt': [0, 0, 0, 7],
    'UserDeposit': [0, 0, 0, 0],
    'UserLocation': ['None', 'None', 'Hospital', 'UofG']
}

NUM_USER_SAMPLES, NUM_CARS_SAMPLES, NUM_ORDER_SAMPLES = 100, 100, 1000

ORDER_TEST_DATA = {
    'OrderID': [NUM_ORDER_SAMPLES - 4, NUM_ORDER_SAMPLES - 3, NUM_ORDER_SAMPLES - 2, NUM_ORDER_SAMPLES - 1,
                NUM_ORDER_SAMPLES],
    'CarID': [1, 21, 53, 6, 77],
    'UserName': ['user1', 'user', 'user', 'user', 'user'],
    'OrderStartTime': ['2023-07-14 19:04:32', '2020-06-19 08:17:02', '2022-05-01 00:12:19', '2021-10-25 15:44:05',
                       '2022-03-17 04:09:49'],
    'OrderEndTime': ['2023-07-14 21:04:32', '2020-06-19 11:17:02', '2022-05-01 02:12:19', '2021-10-25 16:44:05',
                     '2022-03-17 06:09:49'],
    'OrderPrice': [14, 21, 14, 7, 14],
    'OrderState': ['due', 'end', 'end', 'end', 'end'],
    'CarStartLocation': ['IKEA', 'Hospital', 'UofG', 'Square', 'City Center'],
    'CarEndLocation': ['Hospital', 'UofG', 'Square', 'City Center', 'IKEA']
}


# 创建数据库连接
def connect_to_database():
    connect = sqlite3.connect('etsp_database.db')
    return connect


def get_all_users():
    connect = connect_to_database()

    try:
        df_users = pd.read_sql_query('SELECT * from tb_Users', connect)
        connect.close()
        return df_users
    except sqlite3.Error as e:
        print("Error in Get All Users: ", str(e))
        connect.close()
        return None


def get_all_cars():
    connect = connect_to_database()

    try:
        # 使用 pandas 从 SQLite 查询数据
        df_cars = pd.read_sql_query('SELECT * from tb_Cars', connect)
        # 关闭连接
        connect.close()
        return df_cars
    except sqlite3.Error as e:
        print("Error in Get All Cars: ", str(e))
        connect.close()
        return None


def get_all_orders():
    connect = connect_to_database()

    try:
        df_orders = pd.read_sql_query('SELECT * from tb_Orders', connect)
        connect.close()
        return df_orders
    except sqlite3.Error as e:
        print("Error in Get All Orders:", str(e))
        connect.close()
        return None


def test_data_initialization():
    num_user_samples, num_cars_samples, num_order_samples = NUM_USER_SAMPLES, NUM_CARS_SAMPLES, NUM_ORDER_SAMPLES

    test_user_initialization(num_user_samples)
    test_cars_data_initialization(num_cars_samples)
    test_order_data_initialization(num_cars_samples, num_order_samples)


def test_user_initialization(num_user_samples):
    """
    用户初始化测试用例
    :param num_user_samples:
    :return:
    """
    # 用户测试用例
    users_test_data = pd.DataFrame(USER_TEST_DATA)
    num_user_samples = num_user_samples - len(users_test_data)

    # print(users_test_data)

    def generate_usernames(num_usernames):
        # 列表中的名字可以根据需要更改或增加
        names = ['Alex', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jasmine']

        # 后缀数字
        suffixes = [str(i) for i in range(100)]

        usernames = []

        # 生成指定数量的用户名
        for _ in range(num_usernames):
            name = random.choice(names)
            suffix = random.choice(suffixes)
            usernames.append(name + suffix)

        return usernames

    def generate_passwords(num_passwords=100, length=8):
        """
        Generate a list of random passwords.

        :param num_passwords: Number of passwords to generate. Default is 100.
        :param length: Length of each password. Default is 8.
        :return: List of random passwords.
        """
        # 所有可用的字符，数字和特殊字符
        characters = string.ascii_letters + string.digits + string.punctuation

        passwords = []

        for _ in range(num_passwords):
            password = ''.join(random.choice(characters) for _ in range(length))
            passwords.append(password)

        return passwords

    list_username = generate_usernames(num_user_samples)
    list_user_password = generate_passwords(num_user_samples, 10)

    df_users = pd.DataFrame({
        'UserName': list_username,
        'UserPassword': list_user_password,
        # 'UserType': [random.choices(['customer', 'operator', 'manager'], weights=[96, 3, 1])[0] for _ in
        #              range(num_user_samples)],
        'UserType': ['customer' for _ in range(num_user_samples)],
        # 'UserDebt': [round(random.uniform(0, 100.0), 2) for _ in range(num_user_samples)],
        'UserDebt': [0 for _ in range(num_user_samples)],
        'UserDeposit': [random.choice([0, 1]) for _ in range(num_user_samples)],
        'UserLocation': [random.choice(LOCATIONS) for _ in range(num_user_samples)]
    })
    # print(df_users)

    df_users = pd.concat([users_test_data, df_users], ignore_index=True)
    # print(df_users)

    connect = connect_to_database()
    df_users.to_sql('tb_Users', connect, if_exists='replace', index=False)
    # print('success df_users')
    connect.close()


def test_cars_data_initialization(num_car_samples):
    car_types = [random.choice(VEHICLE_TYPE) for _ in range(num_car_samples)]
    car_price = [10 if x == 'bike' else 7 for x in car_types]
    # power = list(range(0, 100, 10))
    #
    # car_states = []
    # repair_details = []
    #
    # # 只有CarState是repair情况时RepairDetail才有可能是非None的值
    # for _ in range(num_car_samples):
    #     car_state = random.choices(VEHICLE_STATE_L, weights=[20, 10, 5, 2])[0]
    #     car_states.append(car_state)
    #
    #     if car_state == 'repair':
    #         repair_detail = random.choices(REPAIR_TYPE, weights=[0, 1, 1, 1, 1])[0]  # 注意None的权重设为0
    #     else:
    #         repair_detail = 'None'
    #
    #     repair_details.append(repair_detail)

    car_power = []
    car_states = []
    repair_details = []

    for _ in range(num_car_samples):
        # 生成CarPower值
        power_value = random.choice(range(0, 100, 10))
        car_power.append(power_value)

        # 根据CarPower设置CarState,如果CarState<20,则Carstate设置为lowpower
        if power_value < 20:
            car_state = 'lowpower'
        else:
            car_state = random.choices(VEHICLE_STATE_L, weights=[20, 10, 0, 2], k=1)[0]
            # car_state = random.choices(['available', 'inrent', 'repair'], weights=[20, 10, 2], k=1)[0]

        car_states.append(car_state)

        # 只有CarState是repair情况时RepairDetail才有可能是非None的值
        if car_state == 'repair':
            repair_detail = random.choices(REPAIR_TYPE, weights=[0, 1, 1, 1, 1])[0]
        else:
            repair_detail = 'None'

        repair_details.append(repair_detail)

    df_cars = pd.DataFrame({
        'CarID': range(1, num_car_samples + 1),
        'CarType': car_types,
        'CarDescription': ['This is a ' + car for car in car_types],
        # 'CarPrice': [round(random.uniform(7.0, 20.0), 2) for _ in range(num_car_samples)],
        'CarPrice': car_price,
        # 'CarPower': [random.choice(power) for _ in range(num_car_samples)],
        'CarPower': car_power,
        'CarJourney': [random.randint(0, 1000) for _ in range(num_car_samples)],
        # 'CarState': [random.choices(VEHICLE_STATE_L, weights=[20, 10, 5, 2])[0] for _ in
        #              range(num_car_samples)],
        # 'RepairDetail': [random.choices(REPAIR_TYPE, weights=[20, 1, 1, 1, 1])[0]
        #                  for _ in range(num_car_samples)],
        'CarState': car_states,
        'RepairDetail': repair_details,
        'CarLocation': [random.choice(LOCATIONS) for _ in range(num_car_samples)]
    })

    # print(df_cars)

    connect = connect_to_database()
    df_cars.to_sql('tb_Cars', connect, if_exists='replace', index=False)
    connect.close()


def test_order_data_initialization(num_cars_samples, num_order_samples):
    orders_test_data = pd.DataFrame(ORDER_TEST_DATA)
    num_order_samples = num_order_samples - len(orders_test_data)

    def generate_random_datetimes(num_datetimes, start_year=2020, end_year=2023):
        """
        Generate a list of random datetimes in the format "%Y-%m-%d %H:%M:%S".

        :param num_datetimes: Number of datetimes to generate. Default is 100.
        :param start_year: Start year for the range of random dates. Default is 2000.
        :param end_year: End year for the range of random dates. Default is 2023.
        :return: List of random datetimes in the format "%Y-%m-%d %H:%M:%S".
        """
        start_date = datetime(start_year, 1, 1)
        end_date = datetime(end_year, 12, 31, 23, 59, 59)

        # 计算日期之间的差异，以秒为单位
        time_difference_seconds = int((end_date - start_date).total_seconds())

        random_datetimes = []

        for _ in range(num_datetimes):
            random_seconds = random.randint(0, time_difference_seconds)
            random_datetime = start_date + timedelta(seconds=random_seconds)
            random_datetimes.append(random_datetime.strftime("%Y-%m-%d %H:%M:%S"))

        return random_datetimes

    def add_random_hours(datetime_original_strs, min_hours=1, max_hours=4):
        """
        Add random hours to a list of datetime strings.

        :param datetime_original_strs: List of datetime strings in the format "%Y-%m-%d %H:%M:%S".
        :param min_hours: Minimum hours to add. Default is 1.
        :param max_hours: Maximum hours to add. Default is 4.
        :return: List of modified datetime strings.
        """
        new_datetimes = []
        for dt_str in datetime_original_strs:
            dt_obj = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
            added_hours = random.randint(min_hours, max_hours)
            new_dt_obj = dt_obj + timedelta(hours=added_hours)
            new_datetimes.append(new_dt_obj.strftime("%Y-%m-%d %H:%M:%S"))

        return new_datetimes

    def time_difference_in_hours(dates1, dates2):
        """
        Calculate the time difference in hours between two lists of datetime strings.

        :param dates1: List of datetime strings in the format "%Y-%m-%d %H:%M:%S".
        :param dates2: List of datetime strings in the format "%Y-%m-%d %H:%M:%S".
        :return: List of time differences in hours.
        """
        if len(dates1) != len(dates2):
            raise ValueError("The two lists must be of the same length.")

        differences = []
        for dt_str1, dt_str2 in zip(dates1, dates2):
            try:
                dt_obj1 = datetime.strptime(dt_str1, "%Y-%m-%d %H:%M:%S")
                dt_obj2 = datetime.strptime(dt_str2, "%Y-%m-%d %H:%M:%S")
            except ValueError as e:
                print(f"Error parsing dates: {dt_str1}, {dt_str2}")
                print(e)
                continue

            delta = dt_obj2 - dt_obj1
            difference_hours = delta.total_seconds() / 3600  # Convert timedelta to hours
            differences.append(difference_hours)

        return differences

    list_car_id = [random.randint(0, num_cars_samples - 1) for _ in range(num_order_samples)]
    # n = 0
    # for i in list_car_id:
    #     print(i, end=' ')
    #     if n%10==0:
    #         print('\n')
    # #     n += 1
    # print('list_car_id: ', list_car_id)
    list_start_times = generate_random_datetimes(num_order_samples)
    list_end_times = add_random_hours(list_start_times)

    df_users = get_all_users()
    df_cars = get_all_cars()
    # print('df_cars: ', df_cars)

    costs = []
    for i in range(num_order_samples):
        # print('i:', i)
        start_time = [list_start_times[i]]
        # print('start_time: ', start_time)
        end_time = [list_end_times[i]]
        # print('end_time: ', end_time)
        hours_difference = time_difference_in_hours(start_time, end_time)[0]  # extract the single value from the list
        # print('hours_difference: ', hours_difference)
        # print('df_cars[\'CarID\'] == list_car_id[i+1]:', df_cars['CarID'] == list_car_id[i-1])
        # print('df_cars[df_cars[\'CarID\'] == list_car_id[i+1]]:', df_cars[df_cars['CarID'] == list_car_id[i]+1])
        # print('df_cars[df_cars[\'CarID\'] == list_car_id[i+1]][\'CarPrice\']:', df_cars[df_cars['CarID'] == list_car_id[i]+1]['CarPrice'])
        car_price = df_cars[df_cars['CarID'] == list_car_id[i] + 1]['CarPrice'].iloc[0]  # get the single car price
        # print('car_price: ', car_price)
        cost = round(car_price * hours_difference, 2)
        # print('cost: ', cost)
        costs.append(cost)
    # print('costs: ', costs)

    user_states = {}  # 用于记录每个用户的状态

    order_states = []
    user_names = []

    # 使满足条件：一个用户可以有很多已经完成只能最多有一个未付款或一个正在进行
    for _ in range(num_order_samples):
        user_name = random.choice(df_users['UserName'][len(USER_TEST_DATA):].tolist())
        user_names.append(user_name)

        # 如果用户已经有了ongoing或due状态，只能分配end状态
        if user_states.get(user_name) in ['ongoing', 'due']:
            order_states.append('end')
        else:
            # 如果用户之前没有任何状态，任意分配一个状态
            if user_name not in user_states:
                state = random.choice(ORDER_STATE)
                user_states[user_name] = state
                order_states.append(state)
            else:
                # 如果用户之前有end状态，有机会分配其他状态
                state = random.choice(ORDER_STATE)
                if state in ['ongoing', 'due'] and user_states[user_name] == 'end':
                    user_states[user_name] = state
                order_states.append(state)

    df_orders = pd.DataFrame({
        'OrderID': range(1, num_order_samples + 1),
        'CarID': list_car_id,
        'UserName': user_names,
        'OrderStartTime': list_start_times,
        'OrderEndTime': list_end_times,
        'OrderPrice': costs,
        'OrderState': order_states,
        'CarStartLocation': [random.choice(LOCATIONS) for _ in range(num_order_samples)],
        'CarEndLocation': [random.choice(LOCATIONS) for _ in range(num_order_samples)]
    })

    df_orders = pd.concat([orders_test_data, df_orders], ignore_index=True)
    # print("df_orders: ", df_orders)

    connect = connect_to_database()
    df_orders.to_sql('tb_Orders', connect, if_exists='replace', index=False)
    connect.close()


if __name__ == "__main__":
    test_data_initialization()
