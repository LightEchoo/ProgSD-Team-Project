import sqlite3
import SqlFunction
from tkinter import *
from datetime import datetime, timedelta
import math
import random

#### 通用函数，如获取地址、获取时间等 ####

#获取现在的时间，返回值为 datetime 类型，
def get_current_time():
    time = datetime.now()
    time = time.strftime("%Y-%m-%d %H:%M:%S")
    return time

#解析 string 格式的时间元素
def able_calculate_time(str_time):
    obj_time = datetime.strptime(str_time, "%Y-%m-%d %H:%M:%S")
    return obj_time

#获取 date 格式的时间，并按照进一制计算总小时数
def time_to_hours(str_time):
    '''
    str_time = str(str_time)
    hours, minutes, seconds = map(int, str_time.split(':'))
    hours += math.ceil(minutes / 60) + math.ceil(seconds / 3600)
    return hours
    '''
    format = "%Y-%m-%d %H:%M:%S"
    obj_time = datetime.strptime(str_time, format)

    # 从datetime对象中提取天数、小时、分钟和秒
    days = obj_time.day
    hours = obj_time.hour
    minutes = obj_time.minute
    seconds = obj_time.second

    total_hours = days * 24 + hours + math.ceil(minutes / 60) + math.ceil(seconds / 3600)
    return total_hours

#生成一个随机地址，返回值为 String 类型，postcode 格式
def generate_end_location():
    locations = ["IKEA", "Hospital", "UofG", "Square", "City Center"]
    return random.choice(locations)
