import sqlite3
import pandas as pd
import random
import string
from datetime import datetime, timedelta

# 车辆状态
CAR_STATE_L = ['available', 'inrent', 'lowpower', 'repair']

# 地点位置list
LOCATIONS = ["Learning Hub", "Adam Smith Building", "Boyd Orr Building", "Main Building"]

ORDER_STATE = ['Orders in progress', 'Order Closed']

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# 创建数据库连接
def connect_to_database():
    connect = sqlite3.connect('estp_database.db')
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
    num_user_samples, num_cars_samples, num_order_samples = 100, 100, 1000
    test_user_initialization(num_user_samples)
    test_cars_data_initialization(num_cars_samples)
    test_order_data_initialization(num_cars_samples, num_order_samples)


def test_user_initialization(num_user_samples):
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
        'UserType': [random.choices(['customer', 'operator', 'manager'], weights=[96, 3, 1])[0] for _ in
                     range(num_user_samples)],
        'UserDebt': [round(random.uniform(0, 100.0), 2) for _ in range(num_user_samples)],
        'UserDeposit': [random.choice([0, 1]) for _ in range(num_user_samples)],
        'UserLocation': [random.choice(LOCATIONS) for _ in range(num_user_samples)]
    })
    # print(df_users)

    connect = connect_to_database()
    df_users.to_sql('tb_Users', connect, if_exists='replace', index=False)
    connect.close()

def test_cars_data_initialization(num_car_samples):
    car_types = [random.choice(['bike', 'wheel']) for _ in range(num_car_samples)]
    car_price = [10 if x == 'bike' else 7 for x in car_types]
    power = list(range(0, 100, 10))

    df_cars = pd.DataFrame({
        'CarID': range(1, num_car_samples + 1),
        'CarType': car_types,
        'CarDescription': ['This is a ' + car for car in car_types],
        # 'CarPrice': [round(random.uniform(7.0, 20.0), 2) for _ in range(num_car_samples)],
        'CarPrice': car_price,
        'CarPower': [random.choice(power) for _ in range(num_car_samples)],
        'CarJourney': [random.randint(0, 1000) for _ in range(num_car_samples)],
        'CarState': [random.choices(CAR_STATE_L, weights=[20, 10, 5, 2])[0] for _ in
                     range(num_car_samples)],
        'RepairDetail': [random.choices(['None', 'seat post', 'frames', 'tire', 'battery'], weights=[20, 1, 1, 1, 1])[0]
                         for _ in range(num_car_samples)],
        'CarLocation': [random.choice(LOCATIONS) for _ in range(num_car_samples)]
    })

    # print(df_cars)

    connect = connect_to_database()
    df_cars.to_sql('tb_Cars', connect, if_exists='replace', index=False)
    connect.close()

def test_order_data_initialization(num_cars_samples, num_order_samples):
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

    list_car_id = [random.randint(0, num_cars_samples-1) for _ in range(num_order_samples)]
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
        car_price = df_cars[df_cars['CarID'] == list_car_id[i]+1]['CarPrice'].iloc[0]  # get the single car price
        # print('car_price: ', car_price)
        cost = round(car_price * hours_difference, 2)
        # print('cost: ', cost)
        costs.append(cost)
    # print('costs: ', costs)


    df_orders = pd.DataFrame({
        'OrderID': range(1, num_order_samples + 1),
        'CarID': list_car_id,
        'UserName': [random.choice(df_users['UserPassword'].tolist()) for _ in range(num_order_samples)],
        'OrderStartTime': list_start_times,
        'OrderEndTime': list_end_times,
        'OrderPrice': costs,
        'OrderState': [random.choice(ORDER_STATE) for _ in range(num_order_samples)],
        'CarStartLocation': [random.choice(LOCATIONS) for _ in range(num_order_samples)],
        'CarEndLocation': [random.choice(LOCATIONS) for _ in range(num_order_samples)]
    })

    # print("df_orders: ", df_orders)

    connect = connect_to_database()
    df_orders.to_sql('tb_Orders', connect, if_exists='replace', index=False)
    connect.close()
