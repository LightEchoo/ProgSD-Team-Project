import random
import tkinter as tk
from datetime import datetime
from pathlib import Path
from tkinter import messagebox

import pandas as pd
import ttkbootstrap as bs
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import BE_Function as BEF
import SqlFunction as SQF
import pdsql

IMG_PATH = Path(__file__).parent / 'images'
# 车辆类型
VEHICLE_TYPE = ['ebike', 'escooter']

# 车辆状态
VEHICLE_STATE_L = ['available', 'inrent', 'lowpower', 'repair']

LOCATIONS = ["IKEA", "Hospital", "UofG", "Square", "City Center"]

default_username = 'user'
default_password = '000'

ttkbootstrap_themes = [
    "morph",
    "cosmo",
    "flatly",
    "journal",
    "litera",
    "lumen",
    "minty",
    "pulse",
    "sandstone",
    "united",
    "yeti",
    "simplex",
    "cerculean",

    "solar",
    "superhero",
    "darkly",
    "cyborg",
    "vapor"
]


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

        self.father_middle_frame = None
        self.current_middle_frame = None
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

        self.style = bs.Style(theme=ttkbootstrap_themes[0])

        # self.font_button = tk.font.Font(family='Arial', size=20, weight='bold')
        # self.font_title = tk.font.Font(family="Arial", size=20)
        # self.font_label = tk.font.Font(family="Arial", size=16)
        self.user_info = None
        self.middle_frame = None

    def show_first_page(self):
        """
        初次显示页面
        """
        # self.root.geometry('1600x800')

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 1600
        window_height = 800

        # 计算 x 和 y 坐标
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # 设置窗口的尺寸和位置
        self.root.geometry(f'{window_width}x{window_height}+{x}+{y}')

        f_main = bs.Frame(self.root, bootstyle='dark')
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)
        top = self.frame_top(f_main, 'Welcome to Electric Transportation Sharing Program !')
        middle = self.frame_middle(f_main, 0)
        self.login_page(middle)
        # self.choice_custom_or_company_page(middle)

    def choice_custom_or_company_page(self, frame):
        """
        创建customer or company页面
        :param frame: 主框架
        :return: None
        """
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
        """
        调用FE_user 创建Customer界面
        :return: None
        """
        self.user_main_page()
        # self.icon = None
        # self.vehicle = None
        # app = FE_User.AppManager()
        # app.mainloop()

    def random_style_choice(self):
        random_choice = random.randint(0, len(ttkbootstrap_themes) - 1)
        self.style = bs.Style(theme=ttkbootstrap_themes[random_choice])

    def frame_top(self, frame, current_page_name='electric transportation sharing', flag=1, icon_file_name='bike.png'):
        """
        顶部导航栏
        customer 会去掉logo
        :param flag: customer: 0; operator/manager: 1
        :param frame: 父frame
        :param icon_file_name: 图标
        :param current_page_name: 当前页面名称
        :return: f_top
        """
        if flag == 0:  # customer

            f_top = bs.Frame(frame, bootstyle='dark')
            f_top.place(relx=0, rely=0, relwidth=1, relheight=0.1)

            # b_back = bs.Button(f_top, text='Back', bootstyle='dark-outline', command=self.test)
            b_back = bs.Button(f_top, text='Back', bootstyle='dark-outline', command=self.show_first_page)
            b_back.place(relx=0.02, rely=0.3, relwidth=0.13, relheight=0.4)

            b_style = bs.Button(f_top, text='Click me!', bootstyle='dark-outline', command=self.random_style_choice)
            b_style.place(relx=0.16, rely=0.3, relwidth=0.2, relheight=0.4)

            # l_name = tk.Label(f_top, text=current_page_name)
            l_name = bs.Label(f_top, text=current_page_name, bootstyle='inverse-dark',
                              font=("Arial", 30), anchor='center', justify=tk.CENTER)
            l_name.place(relx=0.35, rely=0.2, relwidth=0.4, relheight=0.6)

            time_label = bs.Label(f_top, font=('Arial', 20), bootstyle='inverse-dark')
            time_label.place(relx=0.7, rely=0.2, relwidth=0.3, relheight=0.6)
            self.update_time(f_top, time_label)

        elif flag == 1:  # operator
            # f_top = ttk.Frame(frame, style='Custom1.TFrame')
            f_top = bs.Frame(frame, bootstyle='dark')
            f_top.place(relx=0, rely=0, relwidth=1, relheight=0.1)

            icon = self.resize_image(icon_file_name, 120, 75)

            # l_icon = tk.Label(f_top, image=icon, borderwidth=2, relief="solid")
            l_icon = bs.Label(f_top, image=icon, bootstyle='inverse-dark')
            l_icon.image = icon  # 保持对图像的引用，以防止被垃圾回收
            l_icon.pack(side='left')

            # TODO: 返回按钮，图片显示
            # def on_press():
            #     b_back_icon.config(image=pressed_image)  # 按钮被按下时的图片
            #     b_back_icon.image = pressed_image
            #
            # def on_release(event):
            #     b_back_icon.config(image=normal_image)  # 按钮释放后恢复原始图片
            #     b_back_icon.image = normal_image
            #
            # # 加载两种状态的图片
            # normal_image = self.resize_image('back-button-white.png', 50, 50)  # 平常状态的图片
            # pressed_image = self.resize_image('back-button-reverse-white.png', 50, 50)  # 按下状态的图片
            #
            # b_back_icon = bs.Button(f_top, text='Return', image=normal_image, bootstyle='dark')
            # b_back_icon.image = pressed_image  # 保持对图像的引用，以防止被垃圾回收
            # b_back_icon.pack(side='left')
            #
            # # 绑定鼠标按钮释放事件
            # b_back_icon.bind('<ButtonRelease-1>', on_release)

            b_back = bs.Button(f_top, text='Back to login', bootstyle='dark-outline', command=self.show_first_page)
            b_back.place(relx=0.1, rely=0.3, relwidth=0.08, relheight=0.4)

            # l_name = tk.Label(f_top, text=current_page_name)
            l_name = bs.Label(f_top, text=current_page_name, bootstyle='inverse-dark',
                              font=("Arial", 30), anchor='center', justify=tk.CENTER)
            l_name.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)

            b_style = bs.Button(f_top, text='Click me!', bootstyle='dark-outline', command=self.random_style_choice)
            b_style.place(relx=0.82, rely=0.3, relwidth=0.06, relheight=0.4)

            time_label = bs.Label(f_top, font=('Arial', 20), bootstyle='inverse-dark')
            time_label.place(relx=0.91, rely=0.2, relwidth=0.08, relheight=0.6)
            self.update_time(f_top, time_label)

        return f_top

    def update_time(self, f_top, time_label):
        """
        更新当前时间
        :param f_top: 父框架
        :param time_label:  用于显示时间的Label
        :return:
        """
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
        b_order = bs.Button(f_b_m, text="Order", bootstyle='dark-outline', command=lambda: self.user_order_page())
        b_home = bs.Button(f_b_r, text="Home", bootstyle='dark-outline', command=lambda: self.user_account_page())
        # b_order = bs.Button(f_b_m, text="Order", bootstyle='dark-outline')
        # b_home = bs.Button(f_b_r, text="Home", bootstyle='dark-outline')

        b_vehicle.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)
        b_order.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)
        b_home.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)

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
                              font=("Arial", 16), anchor='center')
        l_username.place(relx=0.15, rely=0.15, relwidth=0.2, relheight=0.2)

        e_username = bs.Entry(login_lab_frame, bootstyle='info')
        e_username.place(relx=0.45, rely=0.15, relwidth=0.4, relheight=0.2)
        e_username.insert(0, default_username)

        l_psw = bs.Label(login_lab_frame, text='Password: ', bootstyle='inverse-info',
                         font=("Arial", 16), anchor='center')
        l_psw.place(relx=0.15, rely=0.5, relwidth=0.2, relheight=0.2)

        e_psw = bs.Entry(login_lab_frame, bootstyle='info', show="*")
        e_psw.place(relx=0.45, rely=0.5, relwidth=0.4, relheight=0.2)
        e_psw.insert(0, default_password)

        b_login = bs.Button(login_lab_frame, text='Login', bootstyle='info-outline',
                            command=lambda: self.login_test(e_username.get(), e_psw.get()))
        b_login.place(relx=0.2, rely=0.8, relwidth=0.2, relheight=0.15)
        b_register = bs.Button(login_lab_frame, text='Register', bootstyle='info-outline',
                               command=lambda: self.register_page(f_middle))
        b_register.place(relx=0.6, rely=0.8, relwidth=0.2, relheight=0.15)

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
                              font=("Arial", 16), anchor='center')
        l_username.place(relx=0.15, rely=0.15, relwidth=0.2, relheight=0.2)

        e_username = bs.Entry(register_lab_frame, bootstyle='info')
        e_username.place(relx=0.45, rely=0.15, relwidth=0.4, relheight=0.2)

        l_psw = bs.Label(register_lab_frame, text='Password: ', bootstyle='inverse-info',
                         font=("Arial", 16), anchor='center')
        l_psw.place(relx=0.15, rely=0.5, relwidth=0.2, relheight=0.2)

        e_psw = bs.Entry(register_lab_frame, bootstyle='info', show="*")
        e_psw.place(relx=0.45, rely=0.5, relwidth=0.4, relheight=0.2)

        b_login = bs.Button(register_lab_frame, text='Return', bootstyle='info-outline',
                            command=lambda: self.login_page(f_middle))
        b_login.place(relx=0.2, rely=0.8, relwidth=0.2, relheight=0.15)
        b_register = bs.Button(register_lab_frame, text='Register', bootstyle='info-outline',
                               command=lambda: self.register_test(f_middle, e_username.get(), e_psw.get()))
        b_register.place(relx=0.6, rely=0.8, relwidth=0.2, relheight=0.15)

    def login_test(self, username, psw):
        """
        登录测试
        :param username: 用户名
        :param psw: 密码
        :return: None
        """
        # flag = page_flag
        flag = BEF.login(username, psw)

        # FFF查找
        if flag == 0:  # 用户界面
            self.user_main_page()
            self.user_info = SQF.get_one_user_info(username)
            # print(self.user_info)
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
        用户主界面框架
        :return: None
        """
        # print('user_main_page')
        # 获取屏幕尺寸和窗口尺寸
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 400
        window_height = 800

        # 计算 x 和 y 坐标
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # 设置窗口的尺寸和位置
        self.root.geometry(f'{window_width}x{window_height}+{x}+{y}')

        f_main = bs.Frame(self.root, bootstyle='dark')
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)
        top = self.frame_top(f_main, 'User!', 0)
        middle = self.frame_middle(f_main)
        self.user_place_page(middle)
        bottom = self.frame_bottom(f_main, middle)

    def user_order_page(self):
        # print('user_order_page')
        f_main = bs.Frame(self.root, bootstyle='dark')
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)
        top = self.frame_top(f_main, 'Order!', 0)
        middle = self.frame_middle(f_main)
        self.user_order(middle)
        bottom = self.frame_bottom(f_main, middle)

    def user_order(self, frame):
        print(self.user_info[0])
        list_order = SQF.get_one_user_orders(self.user_info[0])
        # TODO: 返回值不充足，只有最后一个订单
        print(list_order)

        # 选车界面 frame
        f_order = bs.Frame(frame, bootstyle='primary')
        f_order.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

        # 创建一个Canvas小部件，它用于包含可滚动的内容。
        canvas_vehicle = tk.Canvas(f_order)
        # 将Canvas小部件放置在中部窗口中，使其在左侧占据空间，并允许其在水平和垂直方向上扩展以填满可用空间。
        canvas_vehicle.place(relx=0, rely=0, relwidth=0.99, relheight=1)

        # 设置滚动条风格
        # scrollbar_style = ttk.Style()
        # scrollbar_style.configure("TScrollbar",
        #                           troughcolor="lightgray",
        #                           borderwidth=5,
        #                           lightcolor="red",
        #                           darkcolor="blue",
        #                           sliderlength=30)

        # 创建一个垂直滚动条（Scrollbar），使用ttk模块创建，与Canvas小部件关联，以便控制Canvas的垂直滚动。
        scrollbar = bs.Scrollbar(f_order, orient=tk.VERTICAL,
                                 command=canvas_vehicle.yview, bootstyle='primary')
        # 将垂直滚动条放置在主窗口的右侧，使其占据垂直空间。
        scrollbar.place(relx=0.99, rely=0, relwidth=0.01, relheight=1)
        # 配置Canvas小部件以与垂直滚动条(scrollbar)相关联，使它能够通过滚动条进行垂直滚动。
        canvas_vehicle.configure(yscrollcommand=scrollbar.set)
        # 创建一个Frame小部件，该Frame用于包含实际的滚动内容。
        f_vehicle = bs.Frame(canvas_vehicle, bootstyle='info', width=2000, height=1000)
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

        # l_test = tk.Label(f_vehicle, text='Order No.\n')
        # l_test.pack()

        # for list in list_order:
        for _ in range(10):
            single_order_bar = self.single_order_bar(f_vehicle)
            single_order_bar.pack()
            space_frame = bs.Frame(f_vehicle, width=380, height=10, bootstyle='primary')
            space_frame.pack()
        frame_fill = bs.Frame(f_vehicle, width=380, height=700, bootstyle='primary')
        frame_fill.pack()

    def single_order_bar(self, frame,
                         list=[61, 11, 'Alex17', '2022-04-29 20:20:07', '2022-04-29 21:20:07', 7, 'ongoing', 'IKEA',
                               'Square']):
        single_order_frame = bs.Frame(frame, width=380, height=200, bootstyle='primary')  # 主框架
        list = [61, 11, 'Alex17', '2022-04-29 20:20:07', '2022-04-29 21:20:07', 7, 'ongoing', 'IKEA',
                'Square']
        # OrderID; UserName, OrderState; CarID, OrderPrice; OrderStartTime, OrderEndTime; CarStartLocation, CarEndLocation;

        # OrderID
        v_order_id = tk.StringVar()
        v_order_id.set('Order\nNo.' + str(list[0]))
        l_order_id = tk.Label(single_order_frame, textvariable=v_order_id)

        # UserName
        v_user_name = tk.StringVar()
        v_user_name.set('UserName:\n' + str(list[2]))
        l_user_name = tk.Label(single_order_frame, textvariable=v_user_name)

        # OrderState
        v_order_state = tk.StringVar()
        v_order_state.set('Order State:\n' + str(list[6]))
        l_order_state = tk.Label(single_order_frame, textvariable=v_order_state)

        # CarID
        v_car_id = tk.StringVar()
        v_car_id.set('Car ID:\n' + str(list[1]))
        l_car_id = tk.Label(single_order_frame, textvariable=v_car_id)

        # OrderPrice
        v_order_price = tk.StringVar()
        v_order_price.set('Order Price(£):\n' + str(list[5]))
        l_order_price = tk.Label(single_order_frame, textvariable=v_order_price)

        # OrderStartTime
        v_order_start_time = tk.StringVar()
        v_order_start_time.set('Order Start Time:\n' + str(list[3]))
        l_order_start_time = tk.Label(single_order_frame, textvariable=v_order_start_time)

        # OrderEndTime
        v_order_end_time = tk.StringVar()
        v_order_end_time.set('Order End Time:\n' + str(list[4]))
        l_order_end_time = tk.Label(single_order_frame, textvariable=v_order_end_time)

        # CarStartLocation
        v_car_start_location = tk.StringVar()
        v_car_start_location.set('Car Start Location:\n' + str(list[7]))
        l_car_start_location = tk.Label(single_order_frame, textvariable=v_car_start_location)

        # CarEndLocation
        v_car_end_location = tk.StringVar()
        v_car_end_location.set('Car End Location:\n' + str(list[8]))
        l_car_end_location = tk.Label(single_order_frame, textvariable=v_car_end_location)

        l_order_id.place(relx=0, rely=0, relwidth=0.1, relheight=1)
        l_user_name.place(relx=0.1, rely=0, relwidth=0.3, relheight=0.25)
        l_order_state.place(relx=0.1, rely=0.25, relwidth=0.3, relheight=0.25)
        l_car_id.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.25)
        l_order_price.place(relx=0.1, rely=0.75, relwidth=0.3, relheight=0.25)
        l_order_start_time.place(relx=0.4, rely=0, relwidth=0.6, relheight=0.25)
        l_order_end_time.place(relx=0.4, rely=0.25, relwidth=0.6, relheight=0.25)
        l_car_start_location.place(relx=0.4, rely=0.5, relwidth=0.6, relheight=0.25)
        l_car_end_location.place(relx=0.4, rely=0.75, relwidth=0.6, relheight=0.25)

        return single_order_frame

        # bg1 = '#36a1b7'
        # l_vehicle_no_value.config(bg=bg1, fg='white')
        # l_rent_value.config(bg=bg1, fg='white')
        # l_battery_life_value.config(bg=bg1, fg='white')
        # l_vehicle_type_value.config(bg=bg1, fg='white')
        # l_location_value.config(bg=bg1, fg='white')
        # l_state_value.config(bg=bg1, fg='white')

    def user_account_page(self):
        # print('user_account_page')
        f_main = bs.Frame(self.root, bootstyle='info')
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)
        top = self.frame_top(f_main, 'Home!', 0)
        middle = self.frame_middle(f_main)
        self.account_page(middle)
        bottom = self.frame_bottom(f_main, middle)

    def account_page(self, f_middle):
        """
        user account界面
        :return:
        """
        f_main = bs.Frame(f_middle, bootstyle='primary')
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)

        images_path_list = ['user_image_0.png', 'user_image_1.png']
        # print(images_path_list)
        # print(images_path_list[random.randint(0, 1)])
        user_image = self.resize_image(images_path_list[random.randint(0, 1)], 150, 200)
        # print(user_image)

        label = bs.Label(f_main, image=user_image, bootstyle='primary')
        label.image = user_image  # 保持对图像的引用，以防止被垃圾回收
        label.place(relx=5 / 16, rely=0.1, relwidth=3 / 8, relheight=0.32)
        # label.pack(side='top')

        v_username = tk.StringVar()  # 用户选择的用户名
        v_username.set('Username: ' + str(self.user_info[0]))
        l_username = tk.Label(f_main, textvariable=v_username)
        l_username.place(relx=0.2, rely=0.55, relwidth=0.6, relheight=0.1)

        v_user_debt = tk.StringVar()  # 用户欠费
        v_user_debt.set('User Debt: ' + str(self.user_info[3]))
        l_user_debt = tk.Label(f_main, textvariable=v_user_debt)
        l_user_debt.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.1)

        b_pay = bs.Button(f_main, text='Pay', bootstyle='primary-outline',
                          command=lambda: self.pay_in_account(self.user_info[3]))
        b_pay.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.05)

    def pay_in_account(self, debt, ):
        if debt == 0:
            tk.messagebox.showerror("Error", "You don't need to pay!")
        else:
            tk.messagebox.showinfo("Congratulations!", "You have paid!")
            # TODO: 更改数据库状态

    def user_place_page(self, f_middle):
        """
        用户主界面-位置选择界面
        :param f_middle: 中部框架
        :return:
        """
        self.middle_page_clear()

        choose_place_lab_frame = bs.Frame(f_middle, bootstyle='info')
        self.current_middle_page = choose_place_lab_frame  # 将传入的page设置为当前页面
        choose_place_lab_frame.place(relx=0.1, rely=1 / 3, relwidth=0.8, relheight=1 / 3)

        l_pickup = bs.Label(choose_place_lab_frame, text='Pickup Location: ', bootstyle='inverse-info')
        l_pickup.place(relx=0.2, rely=4 / 16, relwidth=0.6, relheight=1 / 8)
        # l_return = bs.Label(choose_place_lab_frame, text='Return Location: ', bootstyle='inverse-danger')
        # l_return.place(relx=0.2, rely=7 / 16, relwidth=0.6, relheight=1 / 8)

        v_pickup = tk.StringVar()  # 用户选择的出发位置
        # v_return = tk.StringVar()  # 用户选择的到达位置

        c_pickup = bs.Combobox(choose_place_lab_frame, textvariable=v_pickup, values=LOCATIONS, bootstyle="info")
        c_pickup.place(relx=0.2, rely=6 / 16, relwidth=0.6, relheight=1 / 8)
        # c_return = bs.Combobox(choose_place_lab_frame, textvariable=v_return, values=LOCATIONS, bootstyle='success')
        # c_return.place(relx=0.2, rely=10 / 16, relwidth=0.6, relheight=1 / 8)

        b_map = bs.Button(choose_place_lab_frame, text='Map', bootstyle='primary-outline', command=self.view_map)
        b_map.place(relx=0.2, rely=12 / 16, relwidth=0.2, relheight=2 / 10)
        b_booking = bs.Button(choose_place_lab_frame, text='Booking', bootstyle='primary-outline',
                              command=lambda: self.booking_page(f_middle, c_pickup.get()))
        b_booking.place(relx=0.6, rely=12 / 16, relwidth=0.2, relheight=2 / 10)

    def view_map(self):
        """
        跳出新界面显示一个静态的地图，上面有各个位置选项的信息
        :return: None
        """
        scale = 5
        new_window = self.create_new_window(256 * scale, 146 * scale)

        map_image = self.resize_image('map.png', 256 * scale, 146 * scale)

        label = bs.Label(new_window, image=map_image, bootstyle='inverse-dark')
        label.image = map_image  # 保持对图像的引用，以防止被垃圾回收
        label.pack()

    def booking_page(self, f_middle, location):
        """
        选车页面
        :param f_middle: 父框架
        :param location: 用户选择的location
        :return: None
        """
        if location == '':
            tk.messagebox.showerror("Error", "Please select a location!")
            return None

        result = BEF.save_loaction(self.user_info[0], location)
        print("location: ", location)
        if result == 'Successful':
            self.middle_page_clear()

            f_main = bs.Frame(f_middle, bootstyle='info')
            self.current_middle_frame = f_main
            # self.father_middle_frame = f_middle
            # self.middle_frame = f_main
            f_main.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.sort_vehicle_frame(f_main, 0, location)
        elif result == 'SaveError':
            tk.messagebox.showerror("Error", "Database Error!")

    def test(self):
        if self.middle_frame.winfo_viewable():
            self.middle_frame.place_forget()
        else:
            self.middle_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def resize_image(self, image_name, width, height):
        """
        重新修改图片大小并返回可以被label接受的ImageTk.PhotoImage对象
        :param image_name:
        :param width: new width
        :param height: new height
        :return:
        """
        image = Image.open(IMG_PATH / image_name)
        image = image.resize((width, height), Image.Resampling.LANCZOS)
        image = ImageTk.PhotoImage(image)
        return image

    def sort_vehicle_frame(self, frame, flag=1, location=None):
        """
        用于显示筛选过后的车辆列表的界面
        customer: 可以根据车辆类型、车辆位置进行筛选，默认通过剩余电量进行逆序排序
        operator: 可以根据车辆类型、车辆位置、车辆状态进行筛选，可以选择车辆剩余电量或车辆价格进行排序
        :param flag: 0 - customer, 1 - operator
        :param frame: 父框架
        :return:
        """
        if flag == 0:  # customer
            # 上层车辆类型\状态筛选条件frame
            f_condition = bs.Frame(frame, bootstyle='primary')
            f_condition.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.1)

            # 筛选：vehicle type(下拉框：all、ebike、escooter)
            l_vehicle_type = bs.Label(f_condition, text='Type', bootstyle
            ='inverse-info', anchor='center')
            c_vehicle_type = bs.Combobox(f_condition, values=['ALL'] + VEHICLE_TYPE, bootstyle='info')
            c_vehicle_type.current(0)

            # location(下拉框: all、LOCATIONS)
            l_vehicle_location = bs.Label(f_condition, text='Start', bootstyle='inverse-info',
                                          anchor='center')
            c_vehicle_location = bs.Combobox(f_condition, values=['ALL'] + LOCATIONS, bootstyle='info')
            if location == '':
                c_vehicle_location.current(0)
            else:
                c_vehicle_location.current(LOCATIONS.index(location) + 1)

            l_vehicle_type.place(relx=0.04, rely=0.25, relwidth=0.15, relheight=0.5)
            c_vehicle_type.place(relx=0.19, rely=0.25, relwidth=0.2, relheight=0.5)
            l_vehicle_location.place(relx=0.44, rely=0.25, relwidth=0.15, relheight=0.5)
            c_vehicle_location.place(relx=0.59, rely=0.25, relwidth=0.2, relheight=0.5)

        elif flag == 1:  # operator
            # 上层车辆车辆类型\状态筛选 和 根据电量/价格排序 frame
            f_condition = bs.Frame(frame, bootstyle='primary')
            f_condition.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.1)

            # 筛选：vehicle type(下拉框：all、ebike、escooter)、location(下拉框: all、LOCATIONS)、state(下拉框：all、STATE) 排序：(下拉框：剩余电量/价格)
            l_vehicle_type = bs.Label(f_condition, text='Vehicle Type:', bootstyle
            ='inverse-info', anchor='center')
            c_vehicle_type = bs.Combobox(f_condition, values=['ALL'] + VEHICLE_TYPE, bootstyle='info')
            c_vehicle_type.current(1)
            l_vehicle_location = bs.Label(f_condition, text='Pickup Location:', bootstyle='inverse-info',
                                          anchor='center')
            c_vehicle_location = bs.Combobox(f_condition, values=['ALL'] + LOCATIONS, bootstyle='info')
            c_vehicle_location.current(1)
            l_vehicle_state = bs.Label(f_condition, text='State:', bootstyle='inverse-info', anchor='center')
            c_vehicle_state = bs.Combobox(f_condition, values=['ALL'] + VEHICLE_STATE_L, bootstyle='info')
            c_vehicle_state.current(1)
            l_sort_by = bs.Label(f_condition, text='Sort By:', bootstyle='inverse-info', anchor='center')
            c_sort_by = bs.Combobox(f_condition, values=['CarPower', 'CarPrice'], bootstyle='info')
            c_sort_by.current(0)

            # pd_vehicle = take_pd_vehicles()
            # vehicle_no = pd_vehicle['CarID'].tolist()
            # vehicle_type = pd_vehicle['CarType'].tolist()
            # battery_lift = pd_vehicle['CarPower'].tolist()
            # rent = pd_vehicle['CarPrice'].tolist()
            # location = pd_vehicle['CarLocation'].tolist()
            # state = pd_vehicle['CarState'].tolist()

            l_vehicle_type.place(relx=0.05, rely=0.25, relwidth=0.07, relheight=0.5)
            c_vehicle_type.place(relx=0.12, rely=0.25, relwidth=0.1, relheight=0.5)
            l_vehicle_location.place(relx=0.26, rely=0.25, relwidth=0.07, relheight=0.5)
            c_vehicle_location.place(relx=0.33, rely=0.25, relwidth=0.1, relheight=0.5)
            l_vehicle_state.place(relx=0.47, rely=0.25, relwidth=0.07, relheight=0.5)
            c_vehicle_state.place(relx=0.54, rely=0.25, relwidth=0.1, relheight=0.5)
            l_sort_by.place(relx=0.68, rely=0.25, relwidth=0.07, relheight=0.5)
            c_sort_by.place(relx=0.75, rely=0.25, relwidth=0.1, relheight=0.5)

        # 选车界面 frame
        f_select_vehicle = bs.Frame(frame, bootstyle='primary')
        f_select_vehicle.place(relx=0.02, rely=0.12, relwidth=0.96, relheight=0.87)

        # 创建一个Canvas小部件，它用于包含可滚动的内容。
        canvas_vehicle = tk.Canvas(f_select_vehicle)
        # 将Canvas小部件放置在中部窗口中，使其在左侧占据空间，并允许其在水平和垂直方向上扩展以填满可用空间。
        canvas_vehicle.place(relx=0, rely=0, relwidth=0.99, relheight=1)

        # 设置滚动条风格
        # scrollbar_style = ttk.Style()
        # scrollbar_style.configure("TScrollbar",
        #                           troughcolor="lightgray",
        #                           borderwidth=5,
        #                           lightcolor="red",
        #                           darkcolor="blue",
        #                           sliderlength=30)

        # 创建一个垂直滚动条（Scrollbar），使用ttk模块创建，与Canvas小部件关联，以便控制Canvas的垂直滚动。
        scrollbar = bs.Scrollbar(f_select_vehicle, orient=tk.VERTICAL,
                                 command=canvas_vehicle.yview, bootstyle='primary')
        # 将垂直滚动条放置在主窗口的右侧，使其占据垂直空间。
        scrollbar.place(relx=0.99, rely=0, relwidth=0.01, relheight=1)
        # 配置Canvas小部件以与垂直滚动条(scrollbar)相关联，使它能够通过滚动条进行垂直滚动。
        canvas_vehicle.configure(yscrollcommand=scrollbar.set)
        # 创建一个Frame小部件，该Frame用于包含实际的滚动内容。
        f_vehicle = bs.Frame(canvas_vehicle, bootstyle='info', width=2000, height=1000)
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

        # test values
        # vehicle_no = range(10)
        # vehicle_type = [random.randint(0, 1) for _ in range(10)]
        # battery_lift = [random.uniform(0, 1) * 100 for _ in range(10)]
        # rent = [random.uniform(0, 1) * 10 for _ in range(10)]
        # location = [random.choice(LOCATIONS) for _ in range(10)]
        # state = [random.choice(VEHICLE_STATE_L) for _ in range(10)]

        if flag == 0:  # customer
            b_confirm = bs.Button(f_condition, text='Do', bootstyle='info',
                                  command=lambda: self.data(flag, f_vehicle, c_vehicle_type.get(),
                                                            c_vehicle_location.get()))
            b_confirm.place(relx=0.82, rely=0.25, relwidth=0.14, relheight=0.5)
            self.data(flag, f_vehicle, c_vehicle_type.get(), c_vehicle_location.get())

        elif flag == 1:  # operator
            b_confirm = bs.Button(f_condition, text='Confirm', bootstyle='info',
                                  command=lambda: self.data(flag, f_vehicle, c_vehicle_type.get(),
                                                            c_vehicle_location.get(),
                                                            c_vehicle_state.get(), c_sort_by.get()))
            b_confirm.place(relx=0.89, rely=0.25, relwidth=0.06, relheight=0.5)
            self.data(flag, f_vehicle, c_vehicle_type.get(), c_vehicle_location.get(), c_vehicle_state.get(),
                      c_sort_by.get())

    def operator_page_clear(self):
        """
        中间页面清除
        :return: None
        """
        if self.current_operator_page is not None:  # 检查当前是否有页面
            self.last_operator_page = self.current_operator_page
            self.current_operator_page.place_forget()  # 如果有，删除，但保留在内存中
            print('clear')

    def destroy_frame(self, frame):
        """
        摧毁传入的框架
        :param frame:
        :return:
        """
        for widget in frame.winfo_children():
            widget.destroy()

    def data(self, flag, f_vehicle, choice_type, choice_location, choice_state='available', choice_sort_by='CarPower'):
        """
        进行信息展示操作
        :param flag:
        :param f_vehicle:
        :param choice_type:
        :param choice_location:
        :param choice_state:
        :param choice_sort_by:
        :return:
        """
        if flag == 0:  # user
            single_width = 380
        elif flag == 1:  # operator
            single_width = 1520
        info = [f_vehicle, choice_type, choice_location, choice_state, choice_sort_by]
        # self.operator_page_clear()
        self.destroy_frame(f_vehicle)
        # f_vehicle = bs.Frame(canvas_vehicle)
        # # # 将Frame小部件添加到Canvas中，并配置Frame在Canvas上的位置，以及锚点在左上角（NW表示北西）。
        # canvas_vehicle.create_window((0, 0), window=f_vehicle, anchor=tk.NW)
        # self.current_operator_page = f_vehicle

        pd_vehicle = take_pd_vehicles()
        # nonlocal pd_vehicle, vehicle_no, vehicle_type, battery_lift, rent, location, state, canvas_vehicle

        # print(choice_type, choice_location, choice_state, choice_sort_by)

        # choice_type, choice_location, choice_state, choice_sort_by = 'ebike', 'Hospital', 'available', 'CarPower'
        condition = (
                ((pd_vehicle['CarType'] == choice_type) if choice_type != 'ALL' else pd_vehicle.index.isin(
                    pd_vehicle.index)) &
                ((pd_vehicle['CarLocation'] == choice_location) if choice_location != 'ALL' else pd_vehicle.index.isin(
                    pd_vehicle.index)) &
                ((pd_vehicle['CarState'] == choice_state) if choice_state != 'ALL' else pd_vehicle.index.isin(
                    pd_vehicle.index))
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
        # print(vehicle_nos, vehicle_types, battery_lifts, rents, locations, states)

        for vehicle_no, vehicle_type, battery_lift, rent, location, state in zip(vehicle_nos, vehicle_types,
                                                                                 battery_lifts, rents,
                                                                                 locations, states):
            # print(vehicle_no, vehicle_type, battery_lift, rent)
            single_vehicle_bar = self.single_vehicle_bar(info, f_vehicle, flag, vehicle_no, vehicle_type, battery_lift,
                                                         rent, location, state)
            single_vehicle_bar.pack()
            space_frame = bs.Frame(f_vehicle, width=single_width, height=10, bootstyle='info')
            # print(f_vehicle.winfo_height())
            space_frame.pack()
            # print(f_vehicle.winfo_height())
        # if f_vehicle.winfo_height() < 1000:
        frame_fill = bs.Frame(f_vehicle, width=single_width, height=700, bootstyle='info')
        frame_fill.pack()

    def single_vehicle_bar(self, info, frame, flag, vehicle_no, vehicle_type, battery_lift, rent,
                           location=None, state=0, ):
        """
        用于展示单个车辆信息条
        :param info: 用于按钮更新
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
            main_width = 380
            main_height = 100
            l_width = 100
            m_width = 200
            r_width = 80

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

            frame_info = bs.Frame(single_frame, width=m_width, height=main_height, bootstyle='primary')  # 中部信息框架
            frame_info.place(x=0 + l_width, y=0)

            padx_label, pady_label = 5, 5

            # 车辆编号
            v_vehicle_no = tk.StringVar()
            # # print("车辆编号："+str(vehicle_no))
            v_vehicle_no.set('No.' + str(vehicle_no))
            # print(v_vehicle_no.get())
            # l_vehicle_no = bs.Label(frame_info, textvariable=v_vehicle_no, bootstyle='inverse-info')
            # l_vehicle_no = tk.Label(frame_info, text='Vehicle No.: ', padx=padx_label, pady=pady_label)
            l_vehicle_no_value = tk.Label(frame_info, textvariable=v_vehicle_no, padx=padx_label, pady=pady_label)
            # l_vehicle_no_value.configure(bg="SystemTransparent")

            # TODO: 换成Floodgauge显示
            # v_vehicle_no = tk.IntVar()
            # v_vehicle_no.set(int(vehicle_no))
            # v_vehicle_no = str(vehicle_no)
            # l_vehicle_no_value = bs.Floodgauge(
            #     frame_info,
            #     bootstyle='info',
            #     mode='determinate',
            #     maximum=100,
            #     value=vehicle_no,
            #     mask=v_vehicle_no,
            # )
            # update_floodgauge(vehicle_no)
            #
            # def update_floodgauge(vehicle_no):
            #     l_vehicle_no_value.configure(mask=str(vehicle_no))

            v_rent = bs.StringVar()  # 租金
            rent = round(rent, 2)
            v_rent.set('£' + str(rent) + '/h')
            # l_rent = bs.Label(frame_info, textvariable=v_rent, bootstyle='inverse-info')
            # l_rent = tk.Label(frame_info, text='Rental cost (£/h): ', padx=padx_label, pady=pady_label)
            l_rent_value = tk.Label(frame_info, textvariable=v_rent, padx=padx_label, pady=pady_label)

            v_battery_life = bs.StringVar()  # 剩余电量
            battery_lift = round(battery_lift, 2)
            v_battery_life.set(str(battery_lift) + '%')
            # l_battery_life = bs.Label(frame_info, textvariable=v_battery_life, bootstyle='inverse-info')
            # l_battery_life = tk.Label(frame_info, text='Battery life: ', padx=padx_label, pady=pady_label)
            l_battery_life_value = tk.Label(frame_info, textvariable=v_battery_life, padx=padx_label, pady=pady_label)

            v_vehicle_type = bs.StringVar()  # 车辆类型
            # if vehicle_type == 0:
            #     v_vehicle_type.set("Vehicle type: electric bicycle")
            # elif vehicle_type == 1:
            #     v_vehicle_type.set("Vehicle type: electric scooter")
            v_vehicle_type.set(str(vehicle_type))
            # l_vehicle_type = bs.Label(frame_info, textvariable=v_vehicle_type, bootstyle='inverse-info')
            # l_vehicle_type = tk.Label(frame_info, text='Vehicle type: ', padx=padx_label, pady=pady_label)
            l_vehicle_type_value = tk.Label(frame_info, textvariable=v_vehicle_type, padx=padx_label, pady=pady_label)

            v_location = bs.StringVar()  # 位置
            v_location.set(str(location))
            # l_location = bs.Label(frame_info, textvariable=v_location, bootstyle='inverse-info')
            # l_location = tk.Label(frame_info, text='Location: ', padx=padx_label, pady=pady_label)
            l_location_value = tk.Label(frame_info, textvariable=v_location, padx=padx_label, pady=pady_label)

            v_state = bs.StringVar()  # 状态
            v_state.set(str(state))
            # l_state = bs.Label(frame_info, textvariable=v_state, bootstyle='inverse-info')
            # l_state = tk.Label(frame_info, text='State: ', padx=padx_label, pady=pady_label)
            l_state_value = tk.Label(frame_info, textvariable=v_state, padx=padx_label, pady=pady_label)

            bg1 = '#36a1b7'
            l_vehicle_no_value.config(bg=bg1, fg='white')
            l_rent_value.config(bg=bg1, fg='white')
            l_battery_life_value.config(bg=bg1, fg='white')
            l_vehicle_type_value.config(bg=bg1, fg='white')
            l_location_value.config(bg=bg1, fg='white')
            l_state_value.config(bg=bg1, fg='white')

            l_vehicle_no_value.place(relx=0.07, rely=0.05, relwidth=0.3, relheight=0.2)
            l_rent_value.place(relx=0.07, rely=0.65, relwidth=0.3, relheight=0.2)
            l_battery_life_value.place(relx=0.07, rely=0.35, relwidth=0.3, relheight=0.2)
            l_vehicle_type_value.place(relx=0.43, rely=0.05, relwidth=0.5, relheight=0.2)
            l_location_value.place(relx=0.43, rely=0.35, relwidth=0.5, relheight=0.2)
            l_state_value.place(relx=0.43, rely=0.65, relwidth=0.5, relheight=0.2)

            # frame_info.columnconfigure(0, weight=1)
            # frame_info.columnconfigure(1, weight=1)

            frame_book = bs.Frame(single_frame, width=r_width, height=main_height, bootstyle='primary')  # 右侧预定按钮框架
            frame_book.place(x=0 + l_width + m_width, y=0)

            b_booking = bs.Button(frame_book, text="Book", bootstyle='info',
                                  command=lambda: self.booking(vehicle_no, info))
            b_booking.place(relx=0, rely=0.25, relwidth=0.9, relheight=0.4)

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
                                    padding=((0, 5)))  # 主框架
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

            padx_label, pady_label = 0, 5

            # 车辆编号
            v_vehicle_no = tk.StringVar()
            # # print("车辆编号："+str(vehicle_no))
            v_vehicle_no.set(str(vehicle_no))
            # print(v_vehicle_no.get())
            # l_vehicle_no = bs.Label(frame_info, textvariable=v_vehicle_no, bootstyle='inverse-info')
            l_vehicle_no = tk.Label(frame_info, text='Vehicle No.: ', padx=padx_label, pady=pady_label)
            l_vehicle_no_value = tk.Label(frame_info, textvariable=v_vehicle_no, padx=padx_label, pady=pady_label)
            # l_vehicle_no_value.configure(bg="SystemTransparent")

            # TODO: 换成Floodgauge显示
            # v_vehicle_no = tk.IntVar()
            # v_vehicle_no.set(int(vehicle_no))
            # v_vehicle_no = str(vehicle_no)
            # l_vehicle_no_value = bs.Floodgauge(
            #     frame_info,
            #     bootstyle='info',
            #     mode='determinate',
            #     maximum=100,
            #     value=vehicle_no,
            #     mask=v_vehicle_no,
            # )
            # update_floodgauge(vehicle_no)
            #
            # def update_floodgauge(vehicle_no):
            #     l_vehicle_no_value.configure(mask=str(vehicle_no))

            v_vehicle_type = bs.StringVar()  # 车辆类型
            # if vehicle_type == 0:
            #     v_vehicle_type.set("Vehicle type: electric bicycle")
            # elif vehicle_type == 1:
            #     v_vehicle_type.set("Vehicle type: electric scooter")
            v_vehicle_type.set(str(vehicle_type))
            # l_vehicle_type = bs.Label(frame_info, textvariable=v_vehicle_type, bootstyle='inverse-info')
            l_vehicle_type = tk.Label(frame_info, text='Vehicle type: ', padx=padx_label, pady=pady_label)
            l_vehicle_type_value = tk.Label(frame_info, textvariable=v_vehicle_type, padx=padx_label, pady=pady_label)

            v_rent = bs.StringVar()  # 租金
            rent = round(rent, 2)
            v_rent.set(str(rent))
            # l_rent = bs.Label(frame_info, textvariable=v_rent, bootstyle='inverse-info')
            l_rent = tk.Label(frame_info, text='Rental cost (£/h): ', padx=padx_label, pady=pady_label)
            l_rent_value = tk.Label(frame_info, textvariable=v_rent, padx=padx_label, pady=pady_label)

            v_battery_life = bs.StringVar()  # 剩余电量
            battery_lift = round(battery_lift, 2)
            v_battery_life.set(str(battery_lift))
            # l_battery_life = bs.Label(frame_info, textvariable=v_battery_life, bootstyle='inverse-info')
            l_battery_life = tk.Label(frame_info, text='Battery life: ', padx=padx_label, pady=pady_label)
            l_battery_life_value = tk.Label(frame_info, textvariable=v_battery_life, padx=padx_label, pady=pady_label)

            v_location = bs.StringVar()  # 位置
            v_location.set(str(location))
            # l_location = bs.Label(frame_info, textvariable=v_location, bootstyle='inverse-info')
            l_location = tk.Label(frame_info, text='Location: ', padx=padx_label, pady=pady_label)
            l_location_value = tk.Label(frame_info, textvariable=v_location, padx=padx_label, pady=pady_label)

            v_state = bs.StringVar()  # 状态
            v_state.set(str(state))
            # l_state = bs.Label(frame_info, textvariable=v_state, bootstyle='inverse-info')
            l_state = tk.Label(frame_info, text='State: ', padx=padx_label, pady=pady_label)
            l_state_value = tk.Label(frame_info, textvariable=v_state, padx=padx_label, pady=pady_label)

            bg1 = '#36a1b7'
            l_vehicle_no.config(bg=bg1, fg='white')
            l_rent.config(bg=bg1, fg='white')
            l_vehicle_type.config(bg=bg1, fg='white')
            l_battery_life.config(bg=bg1, fg='white')
            l_location.config(bg=bg1, fg='white')
            l_state.config(bg=bg1, fg='white')

            l_vehicle_no_value.config(bg=bg1, fg='white')
            l_rent_value.config(bg=bg1, fg='white')
            l_vehicle_type_value.config(bg=bg1, fg='white')
            l_battery_life_value.config(bg=bg1, fg='white')
            l_location_value.config(bg=bg1, fg='white')
            l_state_value.config(bg=bg1, fg='white')

            l_vehicle_no.place(relx=0.07, rely=0.025, relwidth=0.23, relheight=0.2)
            l_vehicle_type.place(relx=0.07, rely=0.325, relwidth=0.23, relheight=0.2)
            l_battery_life.place(relx=0.07, rely=0.625, relwidth=0.23, relheight=0.2)
            l_rent.place(relx=0.53, rely=0.025, relwidth=0.23, relheight=0.2)
            l_location.place(relx=0.53, rely=0.325, relwidth=0.23, relheight=0.2)
            l_state.place(relx=0.53, rely=0.625, relwidth=0.23, relheight=0.2)

            # l_vehicle_no_value_num.place(relx=0.32, rely=0.025, relwidth=0.15, relheight=0.2)
            l_vehicle_no_value.place(relx=0.32, rely=0.025, relwidth=0.15, relheight=0.2)
            l_vehicle_type_value.place(relx=0.32, rely=0.325, relwidth=0.15, relheight=0.2)
            l_battery_life_value.place(relx=0.32, rely=0.625, relwidth=0.15, relheight=0.2)
            l_rent_value.place(relx=0.77, rely=0.025, relwidth=0.15, relheight=0.2)
            l_location_value.place(relx=0.77, rely=0.325, relwidth=0.15, relheight=0.2)
            l_state_value.place(relx=0.77, rely=0.625, relwidth=0.15, relheight=0.2)

            # frame_info.columnconfigure(0, weight=1)
            # frame_info.columnconfigure(1, weight=1)

            frame_book = bs.Frame(single_frame, width=r_width, height=main_height, bootstyle='primary')  # 右侧预定按钮框架
            frame_book.place(x=0 + l_width + m_width, y=0)
            # frame_book = tk.Frame(single_frame)  # 右侧预定按钮框架
            # frame_book.place(relx=300/360, rely=0, relwidth=60/360, relheight=1)

            b_booking = bs.Button(frame_book, text="Charge", bootstyle='info',
                                  command=lambda: self.charge(vehicle_no, info))
            b_booking.place(relx=0.025, rely=0.25, relwidth=0.3, relheight=0.4)
            b_booking = bs.Button(frame_book, text="Repair", bootstyle='info',
                                  command=lambda: self.repair(vehicle_no, info))
            b_booking.place(relx=0.35, rely=0.25, relwidth=0.3, relheight=0.4)
            b_booking = bs.Button(frame_book, text="Move", bootstyle='info',
                                  command=lambda: self.move(vehicle_no, info))
            b_booking.place(relx=0.675, rely=0.25, relwidth=0.3, relheight=0.4)

        return single_frame

    def booking(self, vehicle_no, info):
        """
        若用户存在未支付订单，则不能预定，会跳转到页面complete_order_page
        若用户可以预定，则跳转到order_in_progress页面
        :param vehicle_no:
        :param info:
        :return:
        """
        result = BEF.rent_start(vehicle_no, self.user_info[0])
        print(result)
        if result == 'OngoingError':
            tk.messagebox.showerror('Ongoing Error', 'There is an ongoing order, please complete the order first.')
            self.order_in_progress(vehicle_no, result[0], result[1])
        elif result == 'DepositError':
            tk.messagebox.showerror('Order not completed',
                                    'There is an uncompleted order, please complete the order first.')
            print(self.user_info[0])
            order_info = SQF.get_user_specific_order(self.user_info[0], 'due')
            print(order_info)
            self.complete_order_page(order_info[1], order_info[0])
        elif result == 'UnavailableError':
            tk.messagebox.showerror('Unavailable Error',
                                    'This vehicle is unavailable, please try again later.')
        elif result == 'RentError':
            tk.messagebox.showerror('Rent Error',
                                    'Database error, please try again later.')
        else:
            tk.messagebox.showinfo('info', 'Your vehicle has been booked successfully!')
            self.order_in_progress(vehicle_no, result[0], result[1])

    def order_in_progress(self, vehicle_no, order_no=None, start_time=None):
        """
        用户book成功后跳转至当前页面，用于显示正在进行中的订单信息
        :param vehicle_no:
        :return:
        """
        tk.messagebox.showinfo('info', 'Your Vehicle is unlocked!')

        w_order_in_progress = self.create_new_window(400, 400)

        f_main = bs.Frame(w_order_in_progress, bootstyle='primary')
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)

        pd_vehicles = take_pd_vehicles()  # vehicle info
        vehicle_info = pd_vehicles[pd_vehicles['CarID'] == vehicle_no]
        # print(vehicle_info)
        # print(vehicle_info['CarType'])

        if str(vehicle_info['CarType']) == 'ebike':
            image_file_name = 'ebike.png'
        else:
            image_file_name = 'escooter.png'

        f_order_in_progress = bs.Frame(f_main, bootstyle='primary')
        f_order_in_progress.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        l_order_in_progress = bs.Label(f_order_in_progress, text='Order in progress', anchor='center',
                                       bootstyle='inverse-primary')
        l_order_in_progress.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.8)

        f_order_info = bs.Frame(f_main, bootstyle='primary')
        f_order_info.place(relx=0, rely=0.1, relwidth=1, relheight=0.8)

        vehicle_image = self.resize_image(image_file_name, 200, 200)
        l_icon = bs.Label(f_order_info, image=vehicle_image, bootstyle='primary')
        l_icon.image = vehicle_image  # 保持对图像的引用，以防止被垃圾回收
        l_icon.place(relx=0.25, rely=0.03, relwidth=0.5, relheight=5 / 8, bordermode='outside')

        f_vehicle_info = bs.Frame(f_order_info, bootstyle='primary')  # vehicle info
        f_vehicle_info.place(relx=0, rely=0.705, relwidth=1, relheight=0.295, bordermode='outside')

        v_vehicle_no_value = bs.StringVar()  # vehicle no
        v_vehicle_no_value.set('Vehicle No.\n' + str(vehicle_no))
        l_vehicle_no = tk.Label(f_vehicle_info, textvariable=v_vehicle_no_value)
        # l_vehicle_no = bs.Label(f_vehicle_info, text='test_vehicle_no', bootstyle='inverse-info')

        v_order_no_value = bs.StringVar()  # order no
        v_order_no_value.set('Order No.\n' + str(order_no))
        l_order_no = tk.Label(f_vehicle_info, textvariable=v_order_no_value)
        # l_order_no = bs.Label(f_vehicle_info, text='test_order_no', bootstyle='inverse-info')

        v_start_time_value = bs.StringVar()  # start time
        v_start_time_value.set('Start Time\n' + str(start_time))
        l_start_time = tk.Label(f_vehicle_info, textvariable=v_start_time_value)
        # l_start_time = bs.Label(f_vehicle_info, text='test_start_time', bootstyle='inverse-info')

        v_price_value = bs.StringVar()  # price
        pd_vehicles = take_pd_vehicles()
        vehicle_price = pd_vehicles[pd_vehicles['CarID'] == vehicle_no]['CarPrice'].iloc[0]
        # print(vehicle_price)
        v_price_value.set('Price\n£' + str(vehicle_price) + '/h')
        l_price = tk.Label(f_vehicle_info, textvariable=v_price_value)
        # l_price = bs.Label(f_vehicle_info, text='test_price', bootstyle='inverse-info')

        l_vehicle_no.place(relx=0.05, rely=0.05, relwidth=0.4, relheight=0.4)
        l_order_no.place(relx=0.05, rely=0.55, relwidth=0.4, relheight=0.4)
        l_start_time.place(relx=0.55, rely=0.05, relwidth=0.4, relheight=0.4)
        l_price.place(relx=0.55, rely=0.55, relwidth=0.4, relheight=0.4)

        f_button = bs.Frame(f_main, bootstyle='primary')  # button frame
        f_button.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

        b_pay = bs.Button(f_button, text="Return", bootstyle='info',
                          command=lambda: self.return_vehicle_page(w_order_in_progress, order_no, vehicle_no))
        b_pay.place(relx=0.2, rely=0.1, relwidth=0.2, relheight=0.8)

        b_back = bs.Button(f_button, text="Back", bootstyle='info',
                           command=lambda: w_order_in_progress.destroy())
        b_back.place(relx=0.6, rely=0.1, relwidth=0.2, relheight=0.8)

    def return_vehicle_page(self, w_order_in_progress, order_no, vehicle_no):
        """
        用户归还车辆，确认后还车，并跳转到pay/report界面
        :param w_order_in_progress:
        :return:
        """
        w_choice_location = self.create_new_window(400, 40)

        # 在新窗口中添加一个 Label
        label = tk.Label(w_choice_location, text="new location: ")
        label.place(relx=0, rely=0.2, relwidth=0.3, relheight=0.6)

        # 在新窗口中添加一个 Entry
        combobox = bs.Combobox(w_choice_location, values=LOCATIONS, bootstyle="info")
        combobox.place(relx=0.3, rely=0.2, relwidth=0.45, relheight=0.6)

        # 在新窗口中添加一个 Button
        button = tk.Button(w_choice_location, text="confirm",
                           command=lambda: self.return_vehicle(w_choice_location, combobox.get(), w_order_in_progress,
                                                               order_no, vehicle_no))
        button.place(relx=0.8, rely=0.2, relwidth=0.15, relheight=0.6)

    def return_vehicle(self, w_choice_location, choice_location, w_order_in_progress, order_no, vehicle_no):
        w_choice_location.destroy()
        result = tk.messagebox.askquestion(title="Confirm", message="Are you sure you want to return the car?")
        if result == 'yes':
            db_result = BEF.return_car(order_no, choice_location)
            if db_result == "Successful":
                tk.messagebox.showinfo('info', 'Your vehicle is returned!')
                w_order_in_progress.destroy()
                self.complete_order_page(vehicle_no, order_no)
            elif db_result == "ReturnError":
                tk.messagebox.showerror('Rent Error', 'Database error, please try again later.')

    def complete_order_page(self, vehicle_no, order_no):
        """
        当预定是用户存在未支付订单，或正常结束订单还车后，会跳转到此界面
        :return:
        """
        w_complete_order = self.create_new_window(400, 400)

        f_main = bs.Frame(w_complete_order, bootstyle='primary')
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)

        f_pay = bs.Frame(f_main, bootstyle='primary')  # pay frame
        f_pay.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        l_pay = bs.Label(f_pay, text='Complete Order', bootstyle='inverse-primary', anchor='center')
        l_pay.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.8)

        pd_vehicles = take_pd_vehicles()
        vehicle_info = pd_vehicles[pd_vehicles['CarID'] == vehicle_no]
        f_vehicle = bs.Frame(f_main, bootstyle='primary')  # vehicle frame
        f_vehicle.place(relx=0, rely=0.1, relwidth=1, relheight=0.3)

        l_vehicle_info = bs.Label(f_vehicle, text='Vehicle Info', bootstyle='danger',
                                  anchor='center')  # vehicle info frame
        l_vehicle_info.place(relx=0.2, rely=0, relwidth=0.6, relheight=0.25)

        v_vehicle_no_value = bs.StringVar()  # vehicle no
        v_vehicle_no_value.set('Vehicle No.：' + str(vehicle_info['CarID'].iloc[0]))
        l_vehicle_no = tk.Label(f_vehicle, textvariable=v_vehicle_no_value)
        # l_vehicle_no = bs.Label(f_vehicle, text='test_vehicle_no', bootstyle='inverse-info')
        l_vehicle_no.place(relx=0.2, rely=0.25, relwidth=0.6, relheight=0.25)

        v_vehicle_type_value = bs.StringVar()  # vehicle type
        v_vehicle_type_value.set('Vehicle Type: ' + str(vehicle_info['CarType'].iloc[0]))
        l_vehicle_type = tk.Label(f_vehicle, textvariable=v_vehicle_type_value)
        # l_vehicle_type = bs.Label(f_vehicle, text='test_vehicle_type', bootstyle='inverse-info')
        l_vehicle_type.place(relx=0.2, rely=0.5, relwidth=0.6, relheight=0.25)

        v_vehicle_power_left_value = bs.StringVar()  # vehicle power
        v_vehicle_power_left_value.set('Vehicle Power left: ' + str(vehicle_info['CarPower'].iloc[0]))
        l_vehicle_power_left = tk.Label(f_vehicle, textvariable=v_vehicle_power_left_value)
        # l_vehicle_power_left = bs.Label(f_vehicle, text='test_vehicle_power', bootstyle='inverse-info')
        l_vehicle_power_left.place(relx=0.2, rely=0.75, relwidth=0.6, relheight=0.25)

        # TODO: 订单信息获取
        df_orders = take_pd_orders()
        order_info = df_orders[df_orders['OrderID'] == order_no]
        f_order = bs.Frame(f_main, bootstyle='primary')  # order frame
        f_order.place(relx=0, rely=0.45, relwidth=1, relheight=0.4)

        l_order_info = bs.Label(f_order, text='Order Info', bootstyle='danger', anchor='center')  # order info frame
        l_order_info.place(relx=0.2, rely=0, relwidth=0.6, relheight=0.2)

        v_order_start_time_value = bs.StringVar()  # order_start_time
        v_order_start_time_value.set('Order Start Time: ' + str(order_info['OrderStartTime'].iloc[0]))
        l_order_start_time = tk.Label(f_order, textvariable=v_order_start_time_value)
        # l_order_start_time = bs.Label(f_order, text='test_vehicle_no', bootstyle='inverse-info')
        l_order_start_time.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.2)

        v_order_end_time_value = bs.StringVar()  # order_end_time
        v_order_end_time_value.set('Order End Time: ' + str(order_info['OrderEndTime'].iloc[0]))
        l_order_end_time = tk.Label(f_order, textvariable=v_order_end_time_value)
        # l_order_end_time = bs.Label(f_order, text='test_vehicle_type', bootstyle='inverse-info')
        l_order_end_time.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.2)

        v_total_amount_value = bs.StringVar()  # total_amount
        v_total_amount_value.set('Total Amount: ' + str(order_info['OrderPrice'].iloc[0]))
        l_total_amount = tk.Label(f_order, textvariable=v_total_amount_value)
        # l_total_amount = bs.Label(f_order, text='test_vehicle_power', bootstyle='inverse-info')
        l_total_amount.place(relx=0.2, rely=0.6, relwidth=0.6, relheight=0.2)

        v_order_state_value = bs.StringVar()  # order_state
        v_order_state_value.set('Order State: ' + str(order_info['OrderState'].iloc[0]))
        l_order_state = tk.Label(f_order, textvariable=v_order_state_value)
        # l_order_state = bs.Label(f_order, text='test_vehicle_power', bootstyle='inverse-info')
        l_order_state.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.2)

        f_button = bs.Frame(f_main, bootstyle='primary')  # button frame
        f_button.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

        b_pay = bs.Button(f_button, text="Pay", bootstyle='light',
                          command=lambda: self.pay_order_page(v_order_state_value, order_no))
        b_pay.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.8)

        b_report = bs.Button(f_button, text="Report", bootstyle='light',
                             command=lambda: self.report_page(order_no, order_info['CarEndLocation'].iloc[0]))
        b_report.place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.8)

        b_back = bs.Button(f_button, text="Back", bootstyle='light',
                           command=lambda: w_complete_order.destroy())
        b_back.place(relx=0.7, rely=0.1, relwidth=0.2, relheight=0.8)

    def pay_order_page(self, v_order_state_value, order_no):
        """
        支付界面
        :return:
        """
        result = tk.messagebox.askquestion(title="Confirm", message="Are you sure you want to pay this bill?")
        if result == 'yes':
            # print(self.user_info[0])
            if BEF.pay_order(order_no):
                tk.messagebox.showinfo('info', 'Your bill has paid!')
                v_order_state_value.set('Order State: end')
            else:
                tk.messagebox.showerror('Error', 'Pay Order Failed')

    def report_page(self, order_no, end_location):
        # w_choice_location = self.create_new_window(400, 40)
        #
        # # 在新窗口中添加一个 Label
        # label = tk.Label(w_choice_location, text="new location: ")
        # label.place(relx=0, rely=0.2, relwidth=0.3, relheight=0.6)
        #
        # # 在新窗口中添加一个 Entry
        # combobox = bs.Combobox(w_choice_location, values=LOCATIONS, bootstyle="info")
        # combobox.place(relx=0.3, rely=0.2, relwidth=0.45, relheight=0.6)
        #
        # # 在新窗口中添加一个 Button
        # button = tk.Button(w_choice_location, text="confirm")
        # button.place(relx=0.8, rely=0.2, relwidth=0.15, relheight=0.6)
        #
        w_report = self.create_new_window(400, 400)

        f_top = bs.Frame(w_report, bootstyle='primary')  # top frame
        f_top.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        l_report = bs.Label(f_top, text='Report', bootstyle='inverse-primary', anchor='center')
        l_report.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.8)

        f_middle = bs.Frame(w_report, bootstyle='primary')  # middle frame
        f_middle.place(relx=0, rely=0.1, relwidth=1, relheight=0.75)
        e_report = bs.Entry(f_middle, bootstyle='primary')
        e_report.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.9)

        f_bottom = bs.Frame(w_report, bootstyle='primary')  # bottom frame
        f_bottom.place(relx=0, rely=0.85, relwidth=1, relheight=0.15)
        b_report = bs.Button(f_bottom, text="Confirm", bootstyle='info',
                             command=lambda: self.report(w_report, e_report.get(), order_no, end_location))
        b_report.place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.8)
        # b_report.place(relx=0.2, rely=0.1, relwidth=0.2, relheight=0.8)
        # b_back = bs.Button(f_bottom, text="Back", bootstyle='info')
        # b_back.place(relx=0.6, rely=0.1, relwidth=0.2, relheight=0.8)

    def report(self, w_report, info, order_no, end_location):
        w_report.destroy()
        result = BEF.repair(order_no, info, end_location)
        if result == "OrderError":
            tk.messagebox.showerror('Error', 'No Such Order')
        elif result == "Successful":
            tk.messagebox.showinfo('info', 'Repair Success')

    def back(self):
        # TODO: 返回上一层
        pass
        # # self.last_middle_page.place(relx=0, rely=0, relwidth=1, relheight=1)
        # # self.curent_middle_page = self.last_middle_page
        # self.middle_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def charge(self, vehicle_no, info):
        charge_info = BEF.opt_update_car('charge', vehicle_no)
        if charge_info == 'ChargeSuccess':
            tk.messagebox.showinfo('info', 'Charge Success')
            self.data(info[0], info[1], info[2], info[3], info[4])
        elif charge_info == 'CarFalse':
            tk.messagebox.showerror('Error', 'No Such Car')
        elif charge_info == 'RepairFalse':
            tk.messagebox.showerror('Error', 'Need to Repair First')
        elif charge_info == "RentFalse":
            tk.messagebox.showerror('Error', 'Car In Rent')
        else:
            tk.messagebox.showerror('Error', 'Charge Failed')

    def repair(self, vehicle_no, info):
        repair_info = BEF.opt_update_car('repair', vehicle_no)
        print(repair_info)
        if repair_info == 'RepairSuccess':
            tk.messagebox.showinfo('info', 'Charge Success')
            self.data(info[0], info[1], info[2], info[3], info[4])
        elif repair_info == 'RepairFailed':
            tk.messagebox.showerror('Error', 'Repair Failed')
        elif repair_info == 'RentFalse':
            tk.messagebox.showerror('Error', 'Car In Rent')
        elif repair_info == 'NoRepairFalse':
            tk.messagebox.showerror('Error', 'No Need To Repair')
        elif repair_info == 'CarFalse':
            tk.messagebox.showerror('Error', 'No Such Car')
        else:
            tk.messagebox.showerror("Error', 'Repair Failed")

    def create_new_window(self, width, height):
        new_window = tk.Toplevel(self.root)
        new_window.transient(self.root)

        window_width = width
        window_height = height

        screen_width = new_window.winfo_screenwidth()
        screen_height = new_window.winfo_screenheight()

        # 计算居中位置
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # 设置窗口位置和大小
        new_window.geometry(f'{window_width}x{window_height}+{x}+{y}')

        return new_window

    def move(self, vehicle_no, info):

        new_window = self.create_new_window(400, 40)

        # 在新窗口中添加一个 Label
        label = tk.Label(new_window, text="new location: ")
        label.place(relx=0, rely=0.2, relwidth=0.3, relheight=0.6)

        # 在新窗口中添加一个 Entry
        combobox = bs.Combobox(new_window, values=LOCATIONS, bootstyle="info")
        combobox.place(relx=0.3, rely=0.2, relwidth=0.45, relheight=0.6)

        # 在新窗口中添加一个 Button
        button = tk.Button(new_window, text="confirm",
                           command=lambda: self.location_confirm(vehicle_no, info, combobox.get()))
        button.place(relx=0.8, rely=0.2, relwidth=0.15, relheight=0.6)

    def location_confirm(self, vehicle_no, info, choice_location):
        move_result = BEF.opt_update_car('move', vehicle_no, choice_location)
        if move_result == 'MoveSuccess':
            tk.messagebox.showinfo('info', 'Move Success')
            self.data(info[0], info[1], info[2], info[3], info[4])
        elif move_result == 'RentFalse':
            tk.messagebox.showerror('Error', 'Car In Rent')
        elif move_result == 'CarFalse':
            tk.messagebox.showerror('Error', 'No Such Car')
        else:
            tk.messagebox.showerror('Error', 'Move Failed')

    def print_PDF(self):
        pass
        # TODO: print to a PDF file

    def operator_main_page(self):
        self.root.geometry('1600x800')
        f_main = bs.Frame(self.root)
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)
        top = self.frame_top(f_main, 'Operator')
        middle = self.frame_middle(f_main, 1)
        self.operator_sort_page(middle)

    def operator_sort_page(self, f_middle):
        self.middle_page_clear()

        choose_vehicle_frame = bs.Frame(f_middle, bootstyle='info')
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
                                command=lambda: self.vehicle_bottom_treeview(f_bottom, c_sort.get(), True))
        b_deascending = bs.Button(f_top, text='Deascending', bootstyle='info',
                                  command=lambda: self.vehicle_bottom_treeview(f_bottom, c_sort.get(), False))

        l_sort.place(relx=0.4, rely=0.3, relwidth=0.1, relheight=0.4)
        c_sort.place(relx=0.55, rely=0.3, relwidth=0.1, relheight=0.4)
        b_ascending.place(relx=0.7, rely=0.3, relwidth=0.1, relheight=0.4)
        b_deascending.place(relx=0.85, rely=0.3, relwidth=0.1, relheight=0.4)

        def on_combobox_select(event):
            selected_value = c_sort.get()

        f_bottom = bs.Frame(f_main)  # 下层显示区
        f_bottom.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

        self.vehicle_bottom_treeview(f_bottom, 'CarID')

    def vehicle_bottom_treeview(self, frame, sort_column, sort_type=True):
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
    # app.root.protocol("WM_DELETE_WINDOW", on_close)
    # def on_close():
    #
    # # exit()
    # app = FE_User.AppManager()
    # app.mainloop()


if __name__ == "__main__":
    main()
