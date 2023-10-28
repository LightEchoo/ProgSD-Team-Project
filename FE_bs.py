import tkinter as tk
from datetime import datetime
from pathlib import Path
from tkinter import messagebox
from tkinter import ttk

import pandas as pd
import ttkbootstrap as bs
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import BE_Function as BEF
import pdsql

IMG_PATH = Path(__file__).parent / 'images'
# 车辆类型
VEHICLE_TYPE = ['ebike', 'escooter']

# 车辆状态
VEHICLE_STATE_L = ['available', 'inrent', 'lowpower', 'repair']

LOCATIONS = ["IKEA", "Hospital", "UofG", "St George's Square", "Glasgow City Center"]

default_username = 'operator'
default_password = '000'


# page_flag = 1

def take_pd_users():
    """
    获取数据库中的用户数据
    :return: DataFrame结构的数据库中users表
    """
    return pdsql.get_all_users()


def take_pd_vehicles():
    """
    获取数据库中的交通工具数据
    :return:DataFrame结构的数据库中cars表
    """
    return pdsql.get_all_cars()


def take_pd_orders():
    """
    获取数据库中的订单数据
    :return:DataFrame结构的数据库中orders表
    """
    return pdsql.get_all_orders()


class ETSP:
    def __init__(self, root):
        """
        构造函数，初始化应用程序
        :param root: 根窗口
        """
        # Styles.apply_styles()  # 风格初始化

        self.root = root  # 传入的根窗口存储在类的属性root
        self.root.title("Electric Transportation Sharing Program")
        self.root.geometry('1600x800')
        self.current_middle_page = None  # 跟踪当前显示的页面 user/operator中部界面
        self.last_middle_page = None

        self.current_manager_middle_page = None  # manager 右侧界面
        self.last_manager_middle_page = None

        self.current_operator_page = None  # operator 车辆界面
        self.last_operator_page = None

        self.show_first_page()
        self.style = bs.Style()

        # self.font_button = tk.font.Font(family='Arial', size=20, weight='bold')
        # self.font_title = tk.font.Font(family="Arial", size=20)
        # self.font_label = tk.font.Font(family="Arial", size=16)

    def show_first_page(self):
        """
        初次显示页面
        :return: None
        """
        f_main = bs.Frame(self.root, bootstyle='dark')
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)
        top = self.frame_top(f_main, 'Welcome to Electric Transportation Sharing Program !')
        middle = self.frame_middle(f_main, 1)
        self.choice_custom_or_company_page(middle)

    def choice_custom_or_company_page(self, frame):
        self.middle_page_clear()

        choice_lab_frame = bs.LabelFrame(frame, text='Choice', bootstyle='info')
        self.current_middle_page = choice_lab_frame  # 将传入的page设置为当前页面
        choice_lab_frame.place(relx=1 / 3, rely=1 / 3, relwidth=1 / 3, relheight=1 / 3)

        b_custom = bs.Button(choice_lab_frame, text='Custom', bootstyle='info', command=self.show_custom)
        b_company = bs.Button(choice_lab_frame, text='Company', bootstyle='info',
                              command=lambda: self.login_page(frame))

        b_custom.place(relx=0.25, rely=0.4, relwidth=0.15, relheight=0.2)
        b_company.place(relx=0.6, rely=0.4, relwidth=0.15, relheight=0.2)

    def show_custom(self):
        pass  # TODO: 显示custom页面

    def frame_top(self, frame, current_page_name='electric transportation sharing', icon_file_name='bike.png'):
        """
        顶部导航栏
        :param frame: 父frame
        :param icon_file_name: 图标
        :param current_page_name: 当前页面名称
        :return: f_top
        """
        # f_top = ttk.Frame(frame, style='Custom1.TFrame')
        f_top = bs.Frame(frame, bootstyle='dark')
        f_top.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        icon = self.resize_image(icon_file_name, 120, 75)

        # l_icon = tk.Label(f_top, image=icon, borderwidth=2, relief="solid")
        l_icon = bs.Label(f_top, image=icon, bootstyle='inverse-dark')
        l_icon.image = icon  # 保持对图像的引用，以防止被垃圾回收

        # l_name = tk.Label(f_top, text=current_page_name)
        l_name = bs.Label(f_top, text=current_page_name, bootstyle='inverse-dark',
                          font=("Arial", 30), anchor='center', justify=tk.CENTER)

        l_icon.pack(side='left')
        l_name.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)

        time_label = bs.Label(f_top, font=('Arial', 20), bootstyle='inverse-dark')
        time_label.place(relx=0.8, rely=0.2, relwidth=0.1, relheight=0.6)
        self.update_time(f_top, time_label)

        return f_top

    def update_time(self, f_top, time_label):
        current_time = datetime.now().strftime('%H:%M:%S')
        time_label.config(text=current_time)
        f_top.after(1000, lambda: self.update_time(f_top, time_label))

    def frame_middle(self, frame, login_type=0):
        """
        中部主界面
        :param login_type: 登录类型，0用户，1操作员，2管理员，默认0
        :param frame: 父frame
        :return: f_middle
        """
        if login_type == 0:
            f_middle = bs.Frame(frame, bootstyle='primary')
            f_middle.place(relx=0, rely=0.1, relwidth=1, relheight=0.8)
            return f_middle

        elif login_type == 1:
            f_middle = bs.Frame(frame, bootstyle='primary')
            f_middle.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)
            return f_middle

        elif login_type == 2:
            paned_window = bs.PanedWindow(master=frame, orient=tk.HORIZONTAL)
            paned_window.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

            f_middle_left = bs.Frame(paned_window, width=250)
            f_middle_left.place(relx=0, rely=0, relwidth=0.2, relheight=1)
            f_middle_right = bs.Frame(paned_window, width=1350)
            f_middle_right.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
            paned_window.add(f_middle_left)
            paned_window.add(f_middle_right)
            return paned_window, f_middle_left, f_middle_right

    def frame_bottom(self, frame, f_middle):
        """
        底部导航栏
        :param frame: 父frame
        :return: f_bottom
        """
        f_bottom = bs.Frame(frame, bootstyle='light', )
        f_bottom.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

        f_b_l = bs.Frame(f_bottom, bootstyle='info')
        f_b_l.place(relx=0, rely=0, relwidth=1 / 3, relheight=1)
        f_b_m = bs.Frame(f_bottom, bootstyle='info')
        f_b_m.place(relx=1 / 3, rely=0, relwidth=1 / 3, relheight=1)
        f_b_r = bs.Frame(f_bottom, bootstyle='info')
        f_b_r.place(relx=2 / 3, rely=0, relwidth=1 / 3, relheight=1)

        b_vehicle = bs.Button(f_b_l, text="Vehicle", bootstyle='dark-outline',
                              command=lambda: self.user_main_page())
        b_order = bs.Button(f_b_m, text="Order", bootstyle='dark-outline')
        b_home = bs.Button(f_b_r, text="Home", bootstyle='dark-outline')

        b_vehicle.pack(fill='both', expand=True)
        b_order.pack(fill='both', expand=True)
        b_home.pack(fill='both', expand=True)

        return f_bottom

    def middle_page_clear(self):
        """
        中间页面清除
        :return: None
        """
        if self.current_middle_page is not None:  # 检查中部当前是否有页面
            self.last_middle_page = self.current_middle_page
            self.current_middle_page.place_forget()  # 如果有，删除，但保留在内存中

    def login_page(self, f_middle):
        """
        创建登录界面
        :param f_middle: 父frame，中部框架
        :return: Nome
        """
        self.middle_page_clear()

        login_lab_frame = bs.LabelFrame(f_middle, text='Login', bootstyle='info')
        self.current_middle_page = login_lab_frame  # 将传入的page设置为当前页面
        login_lab_frame.place(relx=1 / 3, rely=1 / 3, relwidth=1 / 3, relheight=1 / 3)

        # username, psw = self.login_register_frame(login_lab_frame)
        # print('username')
        # print(username, psw)

        l_username = bs.Label(login_lab_frame, text='Account: ', bootstyle='inverse-info',
                              font=("Arial", 16))
        l_username.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.2)

        e_username = bs.Entry(login_lab_frame, bootstyle='info')
        e_username.place(relx=0.4, rely=0.1, relwidth=0.4, relheight=0.2)
        e_username.insert(0, default_username)

        l_psw = bs.Label(login_lab_frame, text='Password: ', bootstyle='inverse-info',
                         font=("Arial", 16))
        l_psw.place(relx=0.1, rely=0.5, relwidth=0.2, relheight=0.2)

        e_psw = bs.Entry(login_lab_frame, bootstyle='info', show="*")
        e_psw.place(relx=0.4, rely=0.5, relwidth=0.4, relheight=0.2)
        e_psw.insert(0, default_password)

        b_login = bs.Button(login_lab_frame, text='Login', bootstyle='info-outline',
                            command=lambda: self.login_test(e_username.get(), e_psw.get()))
        b_login.place(relx=0.2, rely=0.8, relwidth=0.2, relheight=0.2)
        b_register = bs.Button(login_lab_frame, text='Register', bootstyle='info-outline',
                               command=lambda: self.register_page(f_middle))
        b_register.place(relx=0.6, rely=0.8, relwidth=0.2, relheight=0.2)

        return login_lab_frame

    def register_page(self, f_middle):
        """
        创建注册界面
        :param f_middle: 父frame，中部框架
        :return: Nome
        """
        self.middle_page_clear()

        register_lab_frame = bs.LabelFrame(f_middle, text='Login', bootstyle='info')
        self.current_middle_page = register_lab_frame  # 将传入的page设置为当前页面
        register_lab_frame.place(relx=1 / 3, rely=1 / 3, relwidth=1 / 3, relheight=1 / 3)

        l_username = bs.Label(register_lab_frame, text='Account: ', bootstyle='inverse-info',
                              font=("Arial", 16))
        l_username.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.2)

        e_username = bs.Entry(register_lab_frame, bootstyle='info')
        e_username.place(relx=0.4, rely=0.1, relwidth=0.4, relheight=0.2)

        l_psw = bs.Label(register_lab_frame, text='Password: ', bootstyle='inverse-info',
                         font=("Arial", 16))
        l_psw.place(relx=0.1, rely=0.5, relwidth=0.2, relheight=0.2)

        e_psw = bs.Entry(register_lab_frame, bootstyle='info', show="*")
        e_psw.place(relx=0.4, rely=0.5, relwidth=0.4, relheight=0.2)

        b_login = bs.Button(register_lab_frame, text='Return', bootstyle='info-outline',
                            command=lambda: self.login_page(f_middle))
        b_login.place(relx=0.2, rely=0.8, relwidth=0.2, relheight=0.2)
        b_register = bs.Button(register_lab_frame, text='Register', bootstyle='info-outline',
                               command=lambda: self.register_test(f_middle, e_username.get(), e_psw.get()))
        b_register.place(relx=0.6, rely=0.8, relwidth=0.2, relheight=0.2)

    def login_test(self, username, psw):
        """
        登录测试
        :param username: 用户名
        :param psw: 密码
        :return: None
        """
        # flag = page_flag
        flag = BEF.login(username, psw)

        if flag == 0:  # 用户界面
            self.user_main_page()
        elif flag == 1:  # 操作员界面
            self.operator_main_page()
        elif flag == 2:  # 管理员界面
            self.manager_main_page()
        elif flag == 'NoUserFalse':
            tk.messagebox.showerror("Error", "NoUserFalse")
        elif flag == 'LoginFalse':
            tk.messagebox.showerror("Error", "LoginFalse")
        else:  # 用户不存在
            tk.messagebox.showerror("Error", "The user does not exist")

    def register_test(self, f_middle, username, psw):
        """
        注册测试
        :param username: 用户名
        :param psw: 密码
        :param f_middle: 中部框架
        :return:
        """
        result = BEF.register(username, psw)  # 用户名
        if result == "RegisterSuccessful":
            tk.messagebox.showinfo("Congratulations!", "you have been successfully registered")
            self.login_page(f_middle)  # 注册成功返回登录窗口
        elif result == "RegisterFailed":
            tk.messagebox.showerror("Error!", "Database Error!")
        elif result == "ExistFalse":
            tk.messagebox.showerror("Error!", "This user is registered!")

    def user_main_page(self):
        """
        用户主界面
        :return: None
        """
        self.root.geometry("400x800")
        f_main = bs.Frame(self.root, bootstyle='dark')
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)
        top = self.frame_top(f_main)
        middle = self.frame_middle(f_main)
        self.user_place_page(middle)
        bottom = self.frame_bottom(f_main, middle)

    def user_place_page(self, f_middle):
        """
        位置选择界面
        :param f_middle: 中部框架
        :return:
        """
        self.middle_page_clear()

        choose_place_lab_frame = bs.Frame(f_middle, bootstyle='warning')
        self.current_middle_page = choose_place_lab_frame  # 将传入的page设置为当前页面
        choose_place_lab_frame.place(relx=0.1, rely=1 / 6, relwidth=0.8, relheight=2 / 3)

        l_pickup = bs.Label(choose_place_lab_frame, text='Pickup Location: ', bootstyle='inverse-danger')
        l_pickup.place(relx=0.2, rely=1 / 16, relwidth=0.6, relheight=1 / 8)
        l_return = bs.Label(choose_place_lab_frame, text='Return Location: ', bootstyle='inverse-danger')
        l_return.place(relx=0.2, rely=7 / 16, relwidth=0.6, relheight=1 / 8)

        v_pickup = tk.StringVar()  # 用户选择的出发位置
        v_return = tk.StringVar()  # 用户选择的到达位置

        c_pickup = bs.Combobox(choose_place_lab_frame, textvariable=v_pickup, values=LOCATIONS, bootstyle="info")
        c_pickup.place(relx=0.2, rely=4 / 16, relwidth=0.6, relheight=1 / 8)
        c_return = bs.Combobox(choose_place_lab_frame, textvariable=v_return, values=LOCATIONS, bootstyle='warning')
        c_return.place(relx=0.2, rely=10 / 16, relwidth=0.6, relheight=1 / 8)

        b_map = bs.Button(choose_place_lab_frame, text='Map', bootstyle='dark-outline', command=self.view_map)
        b_map.place(relx=0.2, rely=13 / 16, relwidth=0.2, relheight=1 / 8)
        b_booking = bs.Button(choose_place_lab_frame, text='Booking', bootstyle='dark-outline',
                              command=lambda: self.booking_page(f_middle))
        b_booking.place(relx=0.6, rely=13 / 16, relwidth=0.2, relheight=1 / 8)

    def view_map(self):
        """
        跳出新界面显示一个静态的地图，上面有各个位置选项的信息
        :return: None
        """
        pass

    def location_test(self):
        pass  # 用户输入信息正确检测

    def booking_page(self, f_middle):
        """
        选车页面
        :param f_middle:
        :return: None
        """
        self.location_test()

        self.middle_page_clear()

        f_main = bs.Frame(f_middle, bootstyle='info')
        self.current_middle_page = f_main
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.sort_vehicle_frame(f_main, 0)

    def resize_image(self, image_name, x, y):
        image = Image.open(IMG_PATH / image_name)
        image = image.resize((x, y), Image.Resampling.LANCZOS)
        image = ImageTk.PhotoImage(image)
        return image

    def sort_vehicle_frame(self, frame, flag):
        """
        滑动框
        :param frame:
        :return:
        """
        # 上层车辆状态筛选条件 和 根据电量/价格排序 frame
        f_condition = bs.Frame(frame, bootstyle='primary')
        f_condition.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.1)

        # 筛选：vehicle type(下拉框：all、ebike、escooter)、location(下拉框: all、LOCATIONS)、state(下拉框：all、STATE) 排序：(下拉框：剩余电量/价格)
        l_vehicle_type = bs.Label(f_condition, text='Vehicle Type:', bootstyle
        ='inverse-info', anchor='center')
        c_vehicle_type = bs.Combobox(f_condition, values=['ALL'] + VEHICLE_TYPE, bootstyle='info')
        c_vehicle_type.current(0)
        l_vehicle_location = bs.Label(f_condition, text='Pickup Location:', bootstyle='inverse-info', anchor='center')
        c_vehicle_location = bs.Combobox(f_condition, values=['ALL'] + LOCATIONS, bootstyle='info')
        c_vehicle_location.current(0)
        l_vehicle_state = bs.Label(f_condition, text='State:', bootstyle='inverse-info', anchor='center')
        c_vehicle_state = bs.Combobox(f_condition, values=['ALL'] + VEHICLE_STATE_L, bootstyle='info')
        c_vehicle_state.current(0)
        l_sort_by = bs.Label(f_condition, text='Sort By:', bootstyle='inverse-info', anchor='center')
        c_sort_by = bs.Combobox(f_condition, values=['CarPower', 'CarPrice'], bootstyle='info')
        c_sort_by.current(0)

        pd_vehicle = take_pd_vehicles()
        vehicle_no = pd_vehicle['CarID'].tolist()
        vehicle_type = pd_vehicle['CarType'].tolist()
        battery_lift = pd_vehicle['CarPower'].tolist()
        rent = pd_vehicle['CarPrice'].tolist()
        location = pd_vehicle['CarLocation'].tolist()
        state = pd_vehicle['CarState'].tolist()

        l_vehicle_type.place(relx=0.05, rely=0.25, relwidth=0.07, relheight=0.5)
        c_vehicle_type.place(relx=0.12, rely=0.25, relwidth=0.1, relheight=0.5)
        l_vehicle_location.place(relx=0.26, rely=0.25, relwidth=0.07, relheight=0.5)
        c_vehicle_location.place(relx=0.33, rely=0.25, relwidth=0.1, relheight=0.5)
        l_vehicle_state.place(relx=0.47, rely=0.25, relwidth=0.07, relheight=0.5)
        c_vehicle_state.place(relx=0.54, rely=0.25, relwidth=0.1, relheight=0.5)
        l_sort_by.place(relx=0.68, rely=0.25, relwidth=0.07, relheight=0.5)
        c_sort_by.place(relx=0.75, rely=0.25, relwidth=0.1, relheight=0.5)

        # 选车界面 frame
        f_select_vehicle = bs.Frame(frame, bootstyle='info')
        f_select_vehicle.place(relx=0.02, rely=0.12, relwidth=0.96, relheight=0.87)

        # 创建一个Canvas小部件，它用于包含可滚动的内容。
        canvas_vehicle = tk.Canvas(f_select_vehicle)
        # 将Canvas小部件放置在中部窗口中，使其在左侧占据空间，并允许其在水平和垂直方向上扩展以填满可用空间。
        canvas_vehicle.place(relx=0, rely=0, relwidth=0.99, relheight=1)

        # 设置滚动条风格
        scrollbar_style = ttk.Style()
        scrollbar_style.configure("TScrollbar",
                                  troughcolor="lightgray",
                                  borderwidth=5,
                                  lightcolor="red",
                                  darkcolor="blue",
                                  sliderlength=30)

        # 创建一个垂直滚动条（Scrollbar），使用ttk模块创建，与Canvas小部件关联，以便控制Canvas的垂直滚动。
        scrollbar = ttk.Scrollbar(f_select_vehicle, orient=tk.VERTICAL, style="TScrollbar",
                                  command=canvas_vehicle.yview)
        # 将垂直滚动条放置在主窗口的右侧，使其占据垂直空间。
        scrollbar.place(relx=0.99, rely=0, relwidth=0.01, relheight=1)
        # 配置Canvas小部件以与垂直滚动条(scrollbar)相关联，使它能够通过滚动条进行垂直滚动。
        canvas_vehicle.configure(yscrollcommand=scrollbar.set)
        # 创建一个Frame小部件，该Frame用于包含实际的滚动内容。
        f_vehicle = bs.Frame(canvas_vehicle)
        # # 将Frame小部件添加到Canvas中，并配置Frame在Canvas上的位置，以及锚点在左上角（NW表示北西）。
        canvas_vehicle.create_window((0, 0), window=f_vehicle, anchor=tk.NW)
        self.current_operator_page = f_vehicle

        def on_canvas_configure(event):  # 内置函数 配置Canvas以根据内容自动调整滚动区域
            canvas_vehicle.configure(scrollregion=canvas_vehicle.bbox("all"))

        # 绑定一个事件处理函数，当Frame的配置发生变化时，将调用on_canvas_configure函数来自动调整Canvas的滚动区域。
        f_vehicle.bind("<Configure>", on_canvas_configure)

        def on_mousewheel(event):
            canvas_vehicle.yview_scroll(-1 * (event.delta // 120), "units")

        # 绑定鼠标滚轮事件
        canvas_vehicle.bind_all("<MouseWheel>", on_mousewheel)

        # vehicle_no = range(10)
        # vehicle_type = [random.randint(0, 1) for _ in range(10)]
        # battery_lift = [random.uniform(0, 1) * 100 for _ in range(10)]
        # rent = [random.uniform(0, 1) * 10 for _ in range(10)]
        # location = [random.choice(LOCATIONS) for _ in range(10)]
        # state = [random.choice(VEHICLE_STATE_L) for _ in range(10)]

        # if flag == 0:  # user
        #     for vehicle_no, vehicle_type, battery_lift, rent in zip(vehicle_no, vehicle_type, battery_lift, rent):
        #         # print(vehicle_no, vehicle_type, battery_lift, rent)
        #         single_vehicle_bar = self.single_vehicle_bar(f_vehicle, flag, vehicle_no, vehicle_type, battery_lift,
        #                                                      rent)
        #         single_vehicle_bar.pack()
        #         space_frame = bs.Frame(f_vehicle, width=1520, height=10, bootstyle='success')
        #         space_frame.pack()
        #
        # # elif flag == 1:  # operator
        # #     for vehicle_no, vehicle_type, battery_lift, rent, location, state in zip(vehicle_no, vehicle_type,
        # #                                                                              battery_lift, rent,
        # #                                                                              location, state):
        # #         # print(vehicle_no, vehicle_type, battery_lift, rent)
        # #         single_vehicle_bar = self.single_vehicle_bar(f_vehicle, flag, vehicle_no, vehicle_type, battery_lift,
        # #                                                      rent, location, state)
        # #         single_vehicle_bar.pack()
        # #         space_frame = bs.Frame(f_vehicle, width=1520, height=10, bootstyle='success')
        # #         space_frame.pack()

        b_confirm = bs.Button(f_condition, text='Confirm', bootstyle='info',
                              command=lambda: self.data(canvas_vehicle, f_vehicle, c_vehicle_type.get(), c_vehicle_location.get(),
                                                        c_vehicle_state.get(), c_sort_by.get()))
        b_confirm.place(relx=0.89, rely=0.25, relwidth=0.06, relheight=0.5)



    def operator_page_clear(self):
        """
        中间页面清除
        :return: None
        """
        if self.current_operator_page is not None:  # 检查当前是否有页面
            self.last_operator_page = self.current_operator_page
            self.current_operator_page.place_forget()  # 如果有，删除，但保留在内存中
            print('clear')

    def data(self, canvas_vehicle, f_vehicle, choice_type, choice_location, choice_state, choice_sort_by):
        # self.operator_page_clear()
        for widget in f_vehicle.winfo_children():
            widget.destroy()
        # f_vehicle = bs.Frame(canvas_vehicle)
        # # # 将Frame小部件添加到Canvas中，并配置Frame在Canvas上的位置，以及锚点在左上角（NW表示北西）。
        # canvas_vehicle.create_window((0, 0), window=f_vehicle, anchor=tk.NW)
        # self.current_operator_page = f_vehicle

        pd_vehicle = take_pd_vehicles()
        # nonlocal pd_vehicle, vehicle_no, vehicle_type, battery_lift, rent, location, state, canvas_vehicle

        print(choice_type, choice_location, choice_state, choice_sort_by)

        # choice_type, choice_location, choice_state, choice_sort_by = 'ebike', 'Hospital', 'available', 'CarPower'
        condition = (
            ((pd_vehicle['CarType'] == choice_type) if choice_type != 'ALL' else pd_vehicle.index.isin(pd_vehicle.index)) &
            ((pd_vehicle['CarLocation'] == choice_location) if choice_location != 'ALL' else pd_vehicle.index.isin(pd_vehicle.index)) &
            ((pd_vehicle['CarState'] == choice_state) if choice_state != 'ALL' else pd_vehicle.index.isin(pd_vehicle.index))
        )
        choice_pd_vehicle = pd_vehicle.loc[condition].sort_values(by=choice_sort_by, ascending=False)[
            ['CarID', 'CarType', 'CarPower', 'CarPrice', 'CarLocation', 'CarState']]

        print(choice_pd_vehicle)

        vehicle_nos = choice_pd_vehicle['CarID'].tolist()
        vehicle_types = choice_pd_vehicle['CarType'].tolist()
        battery_lifts = choice_pd_vehicle['CarPower'].tolist()
        rents = choice_pd_vehicle['CarPrice'].tolist()
        locations = choice_pd_vehicle['CarLocation'].tolist()
        states = choice_pd_vehicle['CarState'].tolist()
        print(vehicle_nos, vehicle_types, battery_lifts, rents, locations, states)

        for vehicle_no, vehicle_type, battery_lift, rent, location, state in zip(vehicle_nos, vehicle_types,
                                                                                 battery_lifts, rents,
                                                                                 locations, states):
            print(vehicle_no, vehicle_type, battery_lift, rent)
            single_vehicle_bar = self.single_vehicle_bar(f_vehicle, 1, vehicle_no, vehicle_type, battery_lift,
                                                         rent, location, state)
            single_vehicle_bar.pack()
            space_frame = bs.Frame(f_vehicle, width=1520, height=10, bootstyle='success')
            space_frame.pack()

    # def data(self, canvas_vehicle, choice_type, choice_location, choice_state, choice_sort_by):
    #     self.operator_page_clear()
    #     canvas_vehicle.place_forget()
    #     f_vehicle = bs.Frame(canvas_vehicle)
    #
    #     # # 将Frame小部件添加到Canvas中，并配置Frame在Canvas上的位置，以及锚点在左上角（NW表示北西）。
    #     canvas_vehicle.create_window((0, 0), window=f_vehicle, anchor=tk.NW)
    #
    #     self.current_operator_page = f_vehicle
    #
    #     pd_vehicle = take_pd_vehicles()
    #     # nonlocal pd_vehicle, vehicle_no, vehicle_type, battery_lift, rent, location, state, canvas_vehicle
    #
    #     print(choice_type, choice_location, choice_state, choice_sort_by)
    #
    #     # choice_type, choice_location, choice_state, choice_sort_by = 'ebike', 'Hospital', 'available', 'CarPower'
    #     condition = (
    #         ((pd_vehicle['CarType'] == choice_type) if choice_type != 'ALL' else pd_vehicle.index.isin(pd_vehicle.index)) &
    #         ((pd_vehicle['CarLocation'] == choice_location) if choice_location != 'ALL' else pd_vehicle.index.isin(pd_vehicle.index)) &
    #         ((pd_vehicle['CarState'] == choice_state) if choice_state != 'ALL' else pd_vehicle.index.isin(pd_vehicle.index))
    #     )
    #     choice_pd_vehicle = pd_vehicle.loc[condition].sort_values(by=choice_sort_by, ascending=False)[
    #         ['CarID', 'CarType', 'CarPower', 'CarPrice', 'CarLocation', 'CarState']]
    #
    #     print(choice_pd_vehicle)
    #
    #     vehicle_nos = choice_pd_vehicle['CarID'].tolist()
    #     vehicle_types = choice_pd_vehicle['CarType'].tolist()
    #     battery_lifts = choice_pd_vehicle['CarPower'].tolist()
    #     rents = choice_pd_vehicle['CarPrice'].tolist()
    #     locations = choice_pd_vehicle['CarLocation'].tolist()
    #     states = choice_pd_vehicle['CarState'].tolist()
    #     print(vehicle_nos, vehicle_types, battery_lifts, rents, locations, states)
    #
    #     for vehicle_no, vehicle_type, battery_lift, rent, location, state in zip(vehicle_nos, vehicle_types,
    #                                                                              battery_lifts, rents,
    #                                                                              locations, states):
    #         print(vehicle_no, vehicle_type, battery_lift, rent)
    #         single_vehicle_bar = self.single_vehicle_bar(f_vehicle, 1, vehicle_no, vehicle_type, battery_lift,
    #                                                      rent, location, state)
    #         single_vehicle_bar.pack()
    #         space_frame = bs.Frame(f_vehicle, width=1520, height=10, bootstyle='success')
    #         space_frame.pack()

    def single_vehicle_bar(self, frame, flag, vehicle_no, vehicle_type, battery_lift, rent,
                           location=None, state=0):
        """
        用于展示单个车辆信息条
        :param flag: user/operator
        :param frame: 父框架
        :param vehicle_no: 车辆编号
        :param vehicle_type: 车辆类型
        :param battery_lift: 剩余电量
        :param rent: 租金
        :param location: 位置
        :param state: 车辆状态
        :return: single_frame 总框架
        """
        if flag == 0:  # user
            main_width = 360
            main_height = 100
            l_width = 100
            m_width = 200
            r_width = 60
        elif flag == 1:  # operator
            main_width = 1520
            main_height = 100
            l_width = 100
            m_width = 1100
            r_width = 320
            label_width = 80

        # style = ttk.Style()
        # style.configure('Custom11.TFrame', bg='dark', borderwidth=5, relief='groove')

        single_frame = bs.Frame(frame, width=main_width, height=main_height, style='primary',
                                padding=((2, 5)))  # 主框架
        # single_frame = tk.Frame(frame, relief='groove', bd=1)
        # single_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        frame_image = bs.Frame(single_frame, width=l_width, height=main_height, padding=((2, 2)))  # 最左侧图像框架
        frame_image.place(x=0, y=0)
        if vehicle_type == 'ebike':
            image_file_name = 'ebike.png'
        else:
            image_file_name = 'escooter.png'
        vehicle = self.resize_image(image_file_name, 100, 100)
        l_icon = bs.Label(frame_image, image=vehicle, bootstyle='info')
        l_icon.image = vehicle  # 保持对图像的引用，以防止被垃圾回收
        # l_icon.pack(side='left')
        l_icon.place(relx=0, rely=0, relwidth=1, relheight=1, bordermode='outside')

        frame_info = bs.Frame(single_frame, width=m_width, height=main_height, bootstyle='primary',
                              padding=((2, 2)))  # 中部信息框架
        frame_info.place(x=0 + l_width, y=0)

        padx_label, pady_label = 5, 5
        v_vehicle_no = tk.StringVar()  # 车辆编号
        # print("车辆编号："+str(vehicle_no))
        v_vehicle_no.set('Vehicle No.' + str(vehicle_no))
        # print(v_vehicle_no.get())
        # l_vehicle_no = bs.Label(frame_info, textvariable=v_vehicle_no, bootstyle='inverse-info')
        l_vehicle_no = tk.Label(frame_info, textvariable=v_vehicle_no, padx=padx_label, pady=pady_label)

        v_vehicle_type = bs.StringVar()  # 车辆类型
        # if vehicle_type == 0:
        #     v_vehicle_type.set("Vehicle type: electric bicycle")
        # elif vehicle_type == 1:
        #     v_vehicle_type.set("Vehicle type: electric scooter")
        v_vehicle_type.set("Vehicle type: electric scooter" + str(vehicle_type))
        # l_vehicle_type = bs.Label(frame_info, textvariable=v_vehicle_type, bootstyle='inverse-info')
        l_vehicle_type = tk.Label(frame_info, textvariable=v_vehicle_type, padx=padx_label, pady=pady_label)

        v_battery_life = bs.StringVar()  # 剩余电量
        battery_lift = round(battery_lift, 2)
        v_battery_life.set("Battery life:" + str(battery_lift) + "%")
        # l_battery_life = bs.Label(frame_info, textvariable=v_battery_life, bootstyle='inverse-info')
        l_battery_life = tk.Label(frame_info, textvariable=v_battery_life, padx=padx_label, pady=pady_label)

        v_rent = bs.StringVar()  # 租金
        rent = round(rent, 2)
        v_rent.set("Rental cost £" + str(rent) + "%/h")
        # l_rent = bs.Label(frame_info, textvariable=v_rent, bootstyle='inverse-info')
        l_rent = tk.Label(frame_info, textvariable=v_rent, padx=padx_label, pady=pady_label)

        if flag == 0:  # user
            l_vehicle_no.pack()
            l_vehicle_type.pack()
            l_battery_life.pack()
            l_rent.pack()
        elif flag == 1:  # operator

            v_location = bs.StringVar()  # 位置
            v_location.set("Location: " + str(location))
            # l_location = bs.Label(frame_info, textvariable=v_location, bootstyle='inverse-info')
            l_location = tk.Label(frame_info, textvariable=v_location, padx=padx_label, pady=pady_label)

            v_state = bs.StringVar()  # 状态
            v_state.set("State: " + str(state))
            # l_state = bs.Label(frame_info, textvariable=v_state, bootstyle='inverse-info')
            l_state = tk.Label(frame_info, textvariable=v_state, padx=padx_label, pady=pady_label)

            bg1 = '#36a1b7'
            l_vehicle_no.config(bg=bg1, fg='white', width=label_width)
            l_vehicle_type.config(bg=bg1, fg='white', width=label_width)
            l_battery_life.config(bg=bg1, fg='white', width=label_width)
            l_rent.config(bg=bg1, fg='white', width=label_width)
            l_location.config(bg=bg1, fg='white', width=label_width)
            l_state.config(bg=bg1, fg='white', width=label_width)

            # padx, pady = 5,5
            # l_vehicle_no.grid(row=0, column=0, sticky=tk.W + tk.E, padx=padx, pady=pady)
            # l_vehicle_type.grid(row=1, column=0, sticky=tk.W + tk.E, padx=padx, pady=pady)
            # l_battery_life.grid(row=2, column=0, sticky=tk.W + tk.E, padx=padx, pady=pady)
            # l_rent.grid(row=0, column=1, sticky=tk.W + tk.E, padx=padx, pady=pady)
            # l_location.grid(row=1, column=1, sticky=tk.W + tk.E, padx=padx, pady=pady)
            # l_state.grid(row=2, column=1, sticky=tk.W + tk.E, padx=padx, pady=pady)

            l_vehicle_no.place(relx=0.07, rely=0.025, relwidth=0.4, relheight=0.2)
            l_vehicle_type.place(relx=0.07, rely=0.325, relwidth=0.4, relheight=0.2)
            l_battery_life.place(relx=0.07, rely=0.625, relwidth=0.4, relheight=0.2)
            l_rent.place(relx=0.53, rely=0.025, relwidth=0.4, relheight=0.2)
            l_location.place(relx=0.53, rely=0.325, relwidth=0.4, relheight=0.2)
            l_state.place(relx=0.53, rely=0.625, relwidth=0.4, relheight=0.2)

            # frame_info.columnconfigure(0, weight=1)
            # frame_info.columnconfigure(1, weight=1)

        frame_book = bs.Frame(single_frame, width=r_width, height=main_height, bootstyle='primary')  # 右侧预定按钮框架
        frame_book.place(x=0 + l_width + m_width, y=0)
        # frame_book = tk.Frame(single_frame)  # 右侧预定按钮框架
        # frame_book.place(relx=300/360, rely=0, relwidth=60/360, relheight=1)

        if flag == 0:
            b_booking = bs.Button(frame_book, text="Book", bootstyle='info')
            b_booking.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.3)

        elif flag == 1:  # 管理员按钮
            b_booking = bs.Button(frame_book, text="Charge", bootstyle='info')
            b_booking.place(relx=0.025, rely=0.25, relwidth=0.3, relheight=0.4)
            b_booking = bs.Button(frame_book, text="Repair", bootstyle='info')
            b_booking.place(relx=0.35, rely=0.25, relwidth=0.3, relheight=0.4)
            b_booking = bs.Button(frame_book, text="Move", bootstyle='info')
            b_booking.place(relx=0.675, rely=0.25, relwidth=0.3, relheight=0.4)

        return single_frame

    def user_vehicle_page(self):
        pass

    def user_order_page(self):
        pass

    def user_home_page(self):
        pass

    def operator_main_page(self):
        self.root.geometry('1600x800')
        f_main = bs.Frame(self.root)
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)
        top = self.frame_top(f_main, 'Operator')
        middle = self.frame_middle(f_main, 1)
        self.operator_sort_page(middle)

    def operator_sort_page(self, f_middle):
        self.middle_page_clear()

        choose_vehicle_frame = bs.Frame(f_middle, bootstyle='success')
        self.current_middle_page = choose_vehicle_frame
        choose_vehicle_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.sort_vehicle_frame(choose_vehicle_frame, 1)

    def operator_charge_page(self):
        pass

    def operator_repair_page(self):
        pass

    def operator_move_page(self):
        pass

    def manager_main_page(self):

        f_main = bs.Frame(self.root, bootstyle='light')
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)
        f_top = self.frame_top(f_main, 'Manager System')
        paned_window, f_middle_left, f_middle_right = self.frame_middle(f_main, 2)

        self.current_manager_middle_page = f_middle_right

        self.style.configure('Treeview', font=('Arial', 10))

        tree = bs.Treeview(f_middle_left, bootstyle='info')
        tree.place(relwidth=1, relheight=1)
        tree.heading("#0", text="Operating Mode", anchor=tk.W)

        tree.insert('', tk.END, text='User Management', iid=0, open=True)
        tree.insert('', tk.END, text='Operator Management', iid=1, open=True)
        tree.insert('', tk.END, text='Vehicle Management', iid=2, open=True)
        tree.insert('', tk.END, text='Order Management', iid=3, open=True)

        tree.insert(0, tk.END, text='User List', iid=4)
        tree.insert(0, tk.END, text='Information Visualization', iid=5)

        tree.insert(1, tk.END, text='Operator List', iid=6)

        tree.insert(2, tk.END, text='Vehicle List', iid=7)
        tree.insert(2, tk.END, text='Information Visualization', iid=8)

        tree.insert(3, tk.END, text='Order List', iid=9)

        MANAGE_PAGE = {0: self.user_management,
                       1: self.operator_management,
                       2: self.vehicle_management,
                       3: self.order_management,
                       4: self.user_list,
                       5: self.user_visualization,
                       6: self.operator_list,
                       7: self.vehicle_list,
                       8: self.vehicle_visualization,
                       9: self.order_list}

        def on_item_selected(event):
            item = tree.selection()[0]
            iid = int(item)  # 将iid转换为整数
            if iid in MANAGE_PAGE:
                func = MANAGE_PAGE[iid]
                func(f_middle_right)  # 调用相应的函数

        tree.bind("<ButtonRelease-1>", on_item_selected)

    def manager_middle_page_clear(self):
        """
        管理员中间页面清除
        :return: None
        """
        if self.current_manager_middle_page is not None:  # 检查中部当前是否有页面
            self.last_manager_middle_page = self.current_manager_middle_page
            self.current_manager_middle_page.place_forget()  # 如果有，删除，但保留在内存中

    def user_management(self, frame):
        self.manager_middle_page_clear()
        f_main = bs.Frame(frame, bootstyle='warning')
        self.current_manager_middle_page = f_main
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)
        l = bs.Label(f_main, text='user_management')
        l.pack()

    def user_list(self, frame):
        self.manager_middle_page_clear()
        f_main = bs.Frame(frame, bootstyle='warning')
        self.current_manager_middle_page = f_main
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)
        l = bs.Label(f_main, text='user_list')
        l.pack()

    def user_visualization(self, frame):
        self.manager_middle_page_clear()
        f_main = bs.Frame(frame, bootstyle='warning')
        self.current_manager_middle_page = f_main
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)
        l = bs.Label(f_main, text='user_visualization')
        l.pack()

    def operator_management(self, frame):
        self.manager_middle_page_clear()
        f_main = bs.Frame(frame, bootstyle='warning')
        self.current_manager_middle_page = f_main
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)
        l = bs.Label(f_main, text='operator_management')
        l.pack()

    def operator_list(self, frame):
        self.manager_middle_page_clear()
        f_main = bs.Frame(frame, bootstyle='warning')
        self.current_manager_middle_page = f_main
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)
        l = bs.Label(f_main, text='operator_list')
        l.pack()

    def vehicle_management(self, frame):
        self.manager_middle_page_clear()
        f_main = bs.Frame(frame, bootstyle='warning')
        self.current_manager_middle_page = f_main
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)
        l = bs.Label(f_main, text='vehicle_management')
        l.pack()

    def vehicle_list(self, frame):
        self.manager_middle_page_clear()
        f_main = bs.Frame(frame, bootstyle='warning')
        self.current_manager_middle_page = f_main
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.style.configure('Treeview', rowheight=25)

        f_top = bs.Frame(f_main, bootstyle='primary')  # 上层功能区
        f_top.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        pd_vehicles = take_pd_vehicles()
        l_sort = bs.Label(f_top, text='Sort:', anchor='center', bootstyle='inverse-info')
        c_sort = bs.Combobox(f_top, values=pd_vehicles.columns.tolist(), bootstyle='info')

        b_ascending = bs.Button(f_top, text='Ascending', bootstyle='info',
                                command=lambda: self.vehicle_bottom_Treeview(f_bottom, c_sort.get(), True))
        b_deascending = bs.Button(f_top, text='Deascending', bootstyle='info',
                                  command=lambda: self.vehicle_bottom_Treeview(f_bottom, c_sort.get(), False))

        l_sort.place(relx=0.4, rely=0.3, relwidth=0.1, relheight=0.4)
        c_sort.place(relx=0.55, rely=0.3, relwidth=0.1, relheight=0.4)
        b_ascending.place(relx=0.7, rely=0.3, relwidth=0.1, relheight=0.4)
        b_deascending.place(relx=0.85, rely=0.3, relwidth=0.1, relheight=0.4)

        def on_combobox_select(event):
            selected_value = c_sort.get()

        f_bottom = bs.Frame(f_main)  # 下层显示区
        f_bottom.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

        self.vehicle_bottom_Treeview(f_bottom, 'CarID')

    def vehicle_bottom_Treeview(self, frame, sort_column, sort_type=True):
        """
        Treeview排序显示
        :param f_bottom: 父框架
        :param sort_column: 排序列
        :param sort_type: 排序方式 True升序 False降序
        :return:
        """

        f_main = bs.Frame(frame)
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)

        pd_vehicles = take_pd_vehicles()
        vehicle_headers = pd_vehicles.columns.tolist()  # 表头
        tree = bs.Treeview(f_main, columns=vehicle_headers, show='headings', bootstyle='info')
        tree.pack(side=tk.LEFT, fill="both", expand=True)
        for header in vehicle_headers:  # 设置表头属性
            tree.heading(header, text=header)
            tree.column(header, stretch=tk.YES, anchor='center')

        pd_vehicles = take_pd_vehicles()
        vehicle_data = pd_vehicles.sort_values(by=sort_column, ascending=sort_type).values.tolist()  # 数值
        for data in vehicle_data:  # 插入数值
            tree.insert('', 'end', values=data)
        self.adjust_column_width(tree, vehicle_headers)  # 调整列宽度自适应

        # 配置交替行颜色的树状视图
        for index, child in enumerate(tree.get_children()):
            if index % 2 == 0:
                tree.item(child, tags=('evenrow',))
            else:
                tree.item(child, tags=('oddrow',))

        tree.tag_configure('evenrow', background='white')
        tree.tag_configure('oddrow', background='lightgray')

        # 创建垂直滚动条
        vsb = bs.Scrollbar(f_main, orient="vertical", command=tree.yview, bootstyle="info-round")
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)

    def adjust_column_width(self, tree, columns):  # 调整列宽度自适应
        for col in columns:
            col_width = tk.font.Font().measure(col)  # 初始化为列名宽度
            for item in tree.get_children():
                # 每个项的宽度
                item_width = tk.font.Font().measure(tree.item(item, 'values')[columns.index(col)])
                if item_width > col_width:
                    col_width = item_width
            # 设置列宽度
            tree.column(col, width=col_width)

    def vehicle_visualization(self, frame):
        self.manager_middle_page_clear()
        f_main = bs.Frame(frame)
        self.current_manager_middle_page = f_main
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)

        f_top = bs.Frame(f_main, bootstyle='primary')  # 上层功能区
        f_top.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        l_start = bs.Label(f_top, text='Start:', anchor='center', bootstyle='inverse-info')
        l_end = bs.Label(f_top, text='End:', anchor='center', bootstyle='inverse-info')
        d_start = bs.DateEntry(f_top, width=12, bootstyle='info')  # 起始时间选择
        d_end = bs.DateEntry(f_top, width=12, bootstyle='info')  # 起始时间选择
        b_vehicle_info = bs.Button(f_top, text='Vehicle Info', bootstyle='info',
                                   command=lambda: self.vehicle_info(f_bottom))
        b_confirm = bs.Button(f_top, text='Confirm', bootstyle='info',
                              command=lambda: self.vehicle_confirm(f_bottom, d_start.entry.get(), d_end.entry.get()))

        l_start.place(relx=0.05, rely=0.3, relwidth=0.1, relheight=0.4)
        d_start.place(relx=0.15, rely=0.3, relwidth=0.2, relheight=0.4)
        l_end.place(relx=0.4, rely=0.3, relwidth=0.1, relheight=0.4)
        d_end.place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.4)
        b_vehicle_info.place(relx=0.733, rely=0.3, relwidth=0.1, relheight=0.4)
        b_confirm.place(relx=0.863, rely=0.3, relwidth=0.1, relheight=0.4)

        f_bottom = bs.Frame(f_main)  # 下层显示区
        f_bottom.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

        self.vehicle_info(f_bottom)

        # 子图赋值

    def vehicle_info(self, f_bottom):
        fig, axes = plt.subplots(2, 3, figsize=(8, 6))
        self.vehicle_power_bar(f_bottom, axes[0][0])
        self.vehicle_journey_bar(f_bottom, axes[0][1])
        self.vehicle_type_price_pie(f_bottom, axes[0][2])
        self.vehicle_state_pie(f_bottom, axes[1][0])
        self.vehicle_location_pie(f_bottom, axes[1][1])
        axes[1][2].axis('off')
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=f_bottom)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(relx=0, rely=0, relwidth=1, relheight=1)

    def vehicle_power_bar(self, frame, ax):
        f_main = bs.Frame(frame)
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)

        pd_vehicles = take_pd_vehicles()
        # 数据操作
        df_vehicles_power = pd_vehicles['CarPower'].value_counts().to_frame('Amount').reset_index()
        bars = df_vehicles_power.plot(kind='bar', x='CarPower', y='Amount', ax=ax, legend=False)
        ax.set_title('Vehicle Power Bar Chart')
        ax.set_ylabel('Amount')

        # 添加数据
        for bar in bars.patches:
            ax.annotate(format(bar.get_height(), '.0f'),
                        (bar.get_x() + bar.get_width() / 2,
                         bar.get_height()), ha='center', va='center',
                        size=10, xytext=(0, 8),
                        textcoords='offset points')

    def vehicle_journey_bar(self, frame, ax):
        f_main = bs.Frame(frame)
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)

        pd_vehicles = take_pd_vehicles()
        df_vehicles_journey = pd_vehicles['CarJourney'].copy()

        bins = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
        labels = ['0-100', '100-200', '200-300', '300-400', '400-500', '500-600', '600-700', '700-800', '800-900',
                  '900-1000']
        df_vehicles_journey_bins = pd.cut(df_vehicles_journey, bins=bins, labels=labels)

        # 数据操作
        df_vehicles_journey_bins = df_vehicles_journey_bins.value_counts().to_frame('Amount').reset_index()
        df_vehicles_journey_bins.columns = ['CarJourney', 'Amount']

        bars = df_vehicles_journey_bins.plot(kind='bar', x='CarJourney', y='Amount', ax=ax, legend=False)
        ax.set_title('Vehicle Journey Bar Chart')
        ax.set_ylabel('Amount')

        for bar in bars.patches:
            ax.annotate(format(bar.get_height(), '.0f'),
                        (bar.get_x() + bar.get_width() / 2,
                         bar.get_height()), ha='center', va='center',
                        size=10, xytext=(0, 8),
                        textcoords='offset points')

    def vehicle_type_price_pie(self, frame, ax):
        f_main = bs.Frame(frame)
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)

        pd_vehicles = take_pd_vehicles()
        df_vehicles_type_price = pd_vehicles['CarType'].value_counts().to_frame('Amount').reset_index()
        df_vehicles_type_price['CarType'] = df_vehicles_type_price['CarType'].replace(
            {'bike': 'Bike:£10/h', 'wheel': 'Wheel:£8/h'})
        df_vehicles_type_price.columns = ['CarType/Price', 'Amount']
        df_vehicles_type_price.set_index('CarType/Price')['Amount'].plot(kind='pie', ax=ax)
        ax.set_title('Vehicle CarType/Price Pie Chart')
        ax.set_ylabel('')
        ax.get_yaxis().set_visible(False)

        # 显示饼图上的百分比
        df_vehicles_type_price.set_index('CarType/Price')['Amount'].plot(
            kind='pie', ax=ax, autopct='%1.1f%%')

    def vehicle_state_pie(self, frame, ax):
        f_main = bs.Frame(frame)
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)

        pd_vehicles = take_pd_vehicles()
        df_vehicles_state = pd_vehicles['CarState'].value_counts().to_frame('Amount').reset_index()
        df_vehicles_state.set_index('CarState')['Amount'].plot(kind='pie', ax=ax)
        ax.set_title('Vehicle State Pie Chart')
        ax.set_ylabel('')
        ax.get_yaxis().set_visible(False)

        # 显示饼图上的百分比
        df_vehicles_state.set_index('CarState')['Amount'].plot(
            kind='pie', ax=ax, autopct='%1.1f%%')

    def vehicle_location_pie(self, frame, ax):
        f_main = bs.Frame(frame)
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)

        pd_vehicles = take_pd_vehicles()
        df_vehicles_location = pd_vehicles['CarLocation'].value_counts().to_frame('Amount').reset_index()
        df_vehicles_location.set_index('CarLocation')['Amount'].plot(kind='pie', ax=ax)
        ax.set_title('Vehicle Current Location Pie Chart')
        ax.set_ylabel('')
        ax.get_yaxis().set_visible(False)

        # 显示饼图上的百分比
        df_vehicles_location.set_index('CarLocation')['Amount'].plot(
            kind='pie', ax=ax, autopct='%1.1f%%')

    def vehicle_confirm(self, f_bottom, start_date, end_date):
        pd_orders = take_pd_orders()
        pd_orders['OrderStartTime'] = pd.to_datetime(pd_orders['OrderStartTime'])
        pd_orders['OrderEndTime'] = pd.to_datetime(pd_orders['OrderEndTime'])

        pd_location = \
            pd_orders[
                (pd_orders['OrderStartTime'] >= start_date) & (pd_orders['OrderEndTime'] <= end_date)][
                ['CarStartLocation', 'CarEndLocation']].reset_index(drop=True)

        # print(pd_location)

        fig, axes = plt.subplots(1, 2, figsize=(8, 6))
        self.start_and_end_route(f_bottom, axes[0], pd_location)
        self.start_to_end_route(f_bottom, axes[1], pd_location)
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=f_bottom)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(relx=0, rely=0, relwidth=1, relheight=1)

    def start_and_end_route(self, frame, ax, data):
        f_main = bs.Frame(frame)
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)

        # 对每一列进行值计数
        start_counts = data['CarStartLocation'].value_counts()
        end_counts = data['CarEndLocation'].value_counts()

        start_and_end_count = pd.concat([start_counts, end_counts], axis=1,
                                        keys=['StartLocation', 'EndLocation']).fillna(0)
        start_and_end_count.plot(kind='bar', stacked=False, ax=ax)
        ax.set_title('Order Start and End Location')
        ax.set_ylabel('Amount')

        # 添加数据
        for p in ax.patches:
            ax.annotate(str(int(p.get_height())),
                        (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center',
                        xytext=(0, 9),
                        textcoords='offset points')

    def start_to_end_route(self, frame, ax, data):
        f_main = bs.Frame(frame)
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)

        # 生成新列，用于显示路线
        data['Route'] = data['CarStartLocation'] + '->' + data['CarEndLocation']

        # 统计每个路线的数量
        start_to_end_count = data['Route'].value_counts()

        # 取值最高的前15个
        start_to_end_count = start_to_end_count.nlargest(15)

        # 对所选取的数据进行排序以确保从最小到最大的顺序绘制
        start_to_end_count = start_to_end_count.sort_values()

        start_to_end_count.plot(kind='barh', ax=ax, x='Count', y='Route', legend=False)
        ax.set_title('Order Start to End Location')

        # 在每个条形上标注数值
        for i, v in enumerate(start_to_end_count):
            ax.text(v + 0.1, i, str(v), color='black', va='center')

    def order_management(self, frame):
        self.manager_middle_page_clear()
        f_main = bs.Frame(frame, bootstyle='warning')
        self.current_manager_middle_page = f_main
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)
        l = bs.Label(f_main, text='order_management')
        l.pack()

    def order_list(self, frame):
        self.manager_middle_page_clear()
        f_main = bs.Frame(frame, bootstyle='warning')
        self.current_manager_middle_page = f_main

        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)
        l = bs.Label(f_main, text='order_list')
        l.pack()


def main():
    root = tk.Tk()  # 创建Tkinter根窗口
    app = ETSP(root)  # 创建实例
    root.mainloop()  # 保持程序运行
    exit()


if __name__ == "__main__":
    main()
