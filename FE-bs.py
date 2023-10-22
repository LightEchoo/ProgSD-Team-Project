import tkinter as tk
from tkinter import ttk
import ttkbootstrap as bs
from tkinter import messagebox
import Styles
from PIL import Image, ImageTk
from pathlib import Path
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

IMG_PATH = Path(__file__).parent / 'images'
# 地点位置list
LOCATIONS = ["Learning Hub", "Adam Smith Building", "Boyd Orr Building", "Main Building"]
# 车辆状态
STATE = {0: 'Stationary', 1: 'In Use', 2: 'To be Repaired', 3: 'To be Charged', 4: 'To be Repaired/Charged'}


class MyApp:
    def __init__(self, root):
        """
        构造函数，初始化应用程序
        :param root: 根窗口
        """
        Styles.apply_styles()  # 风格初始化

        self.root = root  # 传入的根窗口存储在类的属性root
        self.root.title("My App")
        self.root.geometry('1600x800')
        self.current_middle_page = None  # 跟踪当前显示的页面
        self.last_middle_page = None

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
        top = self.frame_top(f_main)
        middle = self.frame_middle(f_main, 1)
        self.login_page(middle)

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

        icon = self.resize_image(icon_file_name, 80, 80)

        # l_icon = tk.Label(f_top, image=icon, borderwidth=2, relief="solid")
        l_icon = bs.Label(f_top, image=icon, bootstyle='inverse-dark')
        l_icon.image = icon  # 保持对图像的引用，以防止被垃圾回收

        # l_name = tk.Label(f_top, text=current_page_name)
        l_name = bs.Label(f_top, text=current_page_name, bootstyle='inverse-dark',
                          font=("Arial", 16), anchor=tk.CENTER, justify=tk.CENTER)

        l_icon.pack(side='left')
        l_name.pack(side='left')

        return f_top

    def frame_middle(self, frame, login_type=0):
        """
        中部主界面
        :param login_type: 登录类型，0用户，1操作员，2管理员，默认0
        :param frame: 父frame
        :return: f_middle
        """
        if login_type == 0:
            f_middle = bs.Frame(frame, bootstyle='success')
            f_middle.place(relx=0, rely=0.1, relwidth=1, relheight=0.8)
            return f_middle

        elif login_type == 1:
            f_middle = bs.Frame(frame, bootstyle='success')
            f_middle.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)
            return f_middle

        elif login_type == 2:
            paned_window = bs.PanedWindow(master=frame, orient=tk.HORIZONTAL)
            paned_window.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

            f_middle_left = bs.Frame(paned_window, bootstyle='success', width=250)
            f_middle_left.place(relx=0, rely=0, relwidth=0.2, relheight=1)
            f_middle_right = bs.Frame(paned_window, bootstyle='danger', width=1350)
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

        f_b_l = bs.Frame(f_bottom, bootstyle='warning')
        f_b_l.place(relx=0, rely=0, relwidth=1 / 3, relheight=1)
        f_b_m = bs.Frame(f_bottom, bootstyle='warning')
        f_b_m.place(relx=1 / 3, rely=0, relwidth=1 / 3, relheight=1)
        f_b_r = bs.Frame(f_bottom, bootstyle='warning')
        f_b_r.place(relx=2 / 3, rely=0, relwidth=1 / 3, relheight=1)

        b_vehicle = bs.Button(f_b_l, text="Vehicle", bootstyle='dark-outline',
                              command=lambda: self.user_main_page())
        b_order = bs.Button(f_b_m, text="Order", bootstyle='dark-outline')
        b_home = bs.Button(f_b_r, text="Home", bootstyle='dark-outline')

        b_vehicle.pack(fill='both', expand=True)
        b_order.pack(fill='both', expand=True)
        b_home.pack(fill='both', expand=True)

        return f_bottom

    def login_register_frame(self, frame):
        l_username = bs.Label(frame, text='Account: ', bootstyle='inverse-success',
                              font=("Arial", 16))
        l_username.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.2)

        e_username = bs.Entry(frame, bootstyle='success')
        e_username.place(relx=0.4, rely=0.1, relwidth=0.4, relheight=0.2)

        l_psw = bs.Label(frame, text='Password: ', bootstyle='inverse-success',
                         font=("Arial", 16))
        l_psw.place(relx=0.1, rely=0.5, relwidth=0.2, relheight=0.2)

        e_psw = bs.Entry(frame, bootstyle='success')
        e_psw.place(relx=0.4, rely=0.5, relwidth=0.4, relheight=0.2)

        return e_username.get(), e_psw.get()

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

        username, psw = self.login_register_frame(login_lab_frame)

        b_login = bs.Button(login_lab_frame, text='Login', bootstyle='success-outline',
                            command=lambda: self.login_test(username, psw))
        b_login.place(relx=0.2, rely=0.8, relwidth=0.2, relheight=0.2)
        b_register = bs.Button(login_lab_frame, text='Register', bootstyle='success-outline',
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

        username, psw = self.login_register_frame(register_lab_frame)

        b_login = bs.Button(register_lab_frame, text='Return', bootstyle='success-outline',
                            command=lambda: self.login_page(f_middle))
        b_login.place(relx=0.2, rely=0.8, relwidth=0.2, relheight=0.2)
        b_register = bs.Button(register_lab_frame, text='Register', bootstyle='success-outline',
                               command=lambda: self.register_test(f_middle))
        b_register.place(relx=0.6, rely=0.8, relwidth=0.2, relheight=0.2)

    def login_test(self, username, psw):
        """
        登录测试
        :param username: 用户名
        :param psw: 密码
        :return: None
        """
        pass
        flag = 2
        if flag == 0:  # 用户界面
            self.user_main_page()
        elif flag == 1:  # 操作员界面
            self.operator_main_page()
        elif flag == 2:  # 管理员界面
            self.manager_main_page()
        else:  # 用户不存在
            tk.messagebox.showerror("Error", "The user does not exist")

    def register_test(self, f_middle):
        """
        注册测试
        :param f_middle: 中部框架
        :return:
        """
        pass
        flag = True  # 注册成功标志
        if not flag:
            tk.messagebox.showerror("Error!", "This user is registered!")  # 注册失败显示信息
        else:
            tk.messagebox.showinfo("Congratulations!", "you have been successfully registered")
            self.login_page(f_middle)  # 注册成功返回登录窗口

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
        f_condition = bs.Frame(frame, bootstyle='info')
        f_condition.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.1)

        # 选车界面 frame
        f_select_vehicle = bs.Frame(frame, bootstyle='info')
        f_select_vehicle.place(relx=0.02, rely=0.12, relwidth=0.96, relheight=0.87)

        # 创建一个Canvas小部件，它用于包含可滚动的内容。
        canvas_vehicle = tk.Canvas(f_select_vehicle)
        # 将Canvas小部件放置在中部窗口中，使其在左侧占据空间，并允许其在水平和垂直方向上扩展以填满可用空间。
        canvas_vehicle.place(relx=0, rely=0, relwidth=0.97, relheight=1)

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
        scrollbar.place(relx=0.97, rely=0, relwidth=0.03, relheight=1)
        # 配置Canvas小部件以与垂直滚动条(scrollbar)相关联，使它能够通过滚动条进行垂直滚动。
        canvas_vehicle.configure(yscrollcommand=scrollbar.set)
        # 创建一个Frame小部件，该Frame用于包含实际的滚动内容。
        f_vehicle = bs.Frame(canvas_vehicle)
        # # 将Frame小部件添加到Canvas中，并配置Frame在Canvas上的位置，以及锚点在左上角（NW表示北西）。
        canvas_vehicle.create_window((0, 0), window=f_vehicle, anchor=tk.NW)

        # single = self.single_vehicle_bar(f_vehicle, 1, 0, 80, 11)
        # single.pack()

        # 设置测试list，实际上此处要替换为后端数据
        pass
        vehicle_no = range(10)
        vehicle_type = [random.randint(0, 1) for _ in range(10)]
        battery_lift = [random.uniform(0, 1) * 100 for _ in range(10)]
        rent = [random.uniform(0, 1) * 10 for _ in range(10)]

        for vehicle_no, vehicle_type, battery_lift, rent in zip(vehicle_no, vehicle_type, battery_lift, rent):
            # print(vehicle_no, vehicle_type, battery_lift, rent)
            single_vehicle_bar = self.single_vehicle_bar(f_vehicle, flag, vehicle_no, vehicle_type, battery_lift, rent)
            single_vehicle_bar.pack()

        def on_canvas_configure(event):  # 内置函数 配置Canvas以根据内容自动调整滚动区域
            canvas_vehicle.configure(scrollregion=canvas_vehicle.bbox("all"))

        # 绑定一个事件处理函数，当Frame的配置发生变化时，将调用on_canvas_configure函数来自动调整Canvas的滚动区域。
        f_vehicle.bind("<Configure>", on_canvas_configure)

        def on_mousewheel(event):
            canvas_vehicle.yview_scroll(-1 * (event.delta // 120), "units")

        # 绑定鼠标滚轮事件
        canvas_vehicle.bind_all("<MouseWheel>", on_mousewheel)

    def single_vehicle_bar(self, frame, flag, vehicle_no, vehicle_type, battery_lift, rent,
                           location=None, state=0, image_file_name='WechatIMG3255.jpg', ):
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
        :param image_file_name: 图片，默认为一个绿色电车图
        :return: single_frame 总框架
        """
        if flag == 0:  # user
            main_width = 360
            main_height = 100
            l_width = 100
            m_width = 200
            r_width = 60
        elif flag == 1:  # operator
            main_width = 1470
            main_height = 100
            l_width = 100
            m_width = 1200
            r_width = 170

        style = ttk.Style()
        style.configure('Custom11.TFrame', bg='dark', borderwidth=5, relief='groove')

        single_frame = bs.Frame(frame, width=main_width, height=main_height, style='Custom11.TFrame')  # 主框架
        # single_frame = tk.Frame(frame, relief='groove', bd=1)
        # single_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        frame_image = bs.Frame(single_frame, width=l_width, height=main_height, bootstyle='dark')  # 最左侧图像框架
        frame_image.place(x=0, y=0)
        # frame_image = tk.Frame(single_frame)
        # frame_image.place(relx=0, rely=0, relwidth=100/360, relheight=1)

        vehicle = self.resize_image(image_file_name, 80, 80)
        l_icon = bs.Label(frame_image, image=vehicle, bootstyle='dark')
        l_icon.image = vehicle  # 保持对图像的引用，以防止被垃圾回收
        # l_icon.pack(side='left')
        l_icon.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8, bordermode='outside')

        frame_info = bs.Frame(single_frame, width=m_width, height=main_height, bootstyle='warning')  # 中部信息框架
        frame_info.place(x=0 + l_width, y=0)

        # frame_info = tk.Frame(single_frame)  # 中部信息框架
        # frame_info.place(relx=100/360, rely=0, relwidth=200/360, relheight=1)

        v_vehicle_no = tk.StringVar()  # 车辆编号
        # print("车辆编号："+str(vehicle_no))
        v_vehicle_no.set('Vehicle No.' + str(vehicle_no))
        # print(v_vehicle_no.get())
        # l_vehicle_no = bs.Label(frame_info, textvariable=v_vehicle_no, bootstyle='inverse-info')
        l_vehicle_no = tk.Label(frame_info, textvariable=v_vehicle_no)

        v_vehicle_type = bs.StringVar()  # 车辆类型
        if vehicle_type == 0:
            v_vehicle_type.set("Vehicle type: electric bicycle")
        elif vehicle_type == 1:
            v_vehicle_type.set("Vehicle type: electric scooter")
        # l_vehicle_type = bs.Label(frame_info, textvariable=v_vehicle_type, bootstyle='inverse-info')
        l_vehicle_type = tk.Label(frame_info, textvariable=v_vehicle_type)

        v_battery_life = bs.StringVar()  # 剩余电量
        battery_lift = round(battery_lift, 2)
        v_battery_life.set("Battery life:" + str(battery_lift) + "%")
        # l_battery_life = bs.Label(frame_info, textvariable=v_battery_life, bootstyle='inverse-info')
        l_battery_life = tk.Label(frame_info, textvariable=v_battery_life)

        v_rent = bs.StringVar()  # 租金
        rent = round(rent, 2)
        v_rent.set("Rental cost £" + str(rent) + "%/h")
        # l_rent = bs.Label(frame_info, textvariable=v_rent, bootstyle='inverse-info')
        l_rent = tk.Label(frame_info, textvariable=v_rent)

        if flag == 0:  # user
            l_vehicle_no.pack()
            l_vehicle_type.pack()
            l_battery_life.pack()
            l_rent.pack()
        elif flag == 1:  # operator

            label_width = 84

            v_location = bs.StringVar()  # 位置
            v_location.set("Location: " + str(location))
            # l_location = bs.Label(frame_info, textvariable=v_location, bootstyle='inverse-info')
            l_location = tk.Label(frame_info, textvariable=v_location)

            v_state = bs.StringVar()  # 状态
            v_state.set("State: " + str(STATE[state]))
            # l_state = bs.Label(frame_info, textvariable=v_state, bootstyle='inverse-info')
            l_state = tk.Label(frame_info, textvariable=v_state)

            bg1 = 'lightblue'
            l_vehicle_no.config(bg=bg1, width=label_width)
            l_vehicle_type.config(bg=bg1, width=label_width)
            l_battery_life.config(bg=bg1, width=label_width)
            l_rent.config(bg=bg1, width=label_width)
            l_location.config(bg=bg1, width=label_width)
            l_state.config(bg=bg1, width=label_width)

            l_vehicle_no.grid(row=0, column=0, sticky=tk.W + tk.E, padx=3, pady=5)
            l_vehicle_type.grid(row=1, column=0, sticky=tk.W + tk.E, padx=3, pady=5)
            l_battery_life.grid(row=2, column=0, sticky=tk.W + tk.E, padx=3, pady=5)
            l_rent.grid(row=0, column=1, sticky=tk.W + tk.E, padx=3, pady=5)
            l_location.grid(row=1, column=1, sticky=tk.W + tk.E, padx=3, pady=5)
            l_state.grid(row=2, column=1, sticky=tk.W + tk.E, padx=3, pady=5)

            # frame_info.columnconfigure(0, weight=1)
            # frame_info.columnconfigure(1, weight=1)

        frame_book = bs.Frame(single_frame, width=r_width, height=main_height, bootstyle='info')  # 右侧预定按钮框架
        frame_book.place(x=0 + l_width + m_width, y=0)
        # frame_book = tk.Frame(single_frame)  # 右侧预定按钮框架
        # frame_book.place(relx=300/360, rely=0, relwidth=60/360, relheight=1)

        if flag == 0:
            b_booking = bs.Button(frame_book, text="Book", bootstyle='dark')
            b_booking.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.3)

        elif flag == 1:
            b_booking = bs.Button(frame_book, text="Charge", bootstyle='dark')
            b_booking.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.3)
            b_booking = bs.Button(frame_book, text="Repair", bootstyle='dark')
            b_booking.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.3)
            b_booking = bs.Button(frame_book, text="Move", bootstyle='dark')
            b_booking.place(relx=0.2, rely=0.75, relwidth=0.6, relheight=0.3)

        return single_frame

    def user_vehicle_page(self):
        pass

    def user_order_page(self):
        pass

    def user_home_page(self):
        pass

    def operator_main_page(self):
        self.root.geometry('1600x800')
        f_main = bs.Frame(self.root, bootstyle='success')
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

        self.style.configure('Treeview', font=('Arial', 10))

        tree = bs.Treeview(f_middle_left, bootstyle='success')
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
                       1: self.user_list,
                       2: self.user_visualization,
                       3: self.operator_management,
                       4: self.operator_list,
                       5: self.vehicle_management,
                       6: self.vehicle_list,
                       7: self.vehicle_visualization,
                       8: self.order_management,
                       9: self.order_list}

        def on_tree_select(event):
            selected = tree.selection()  # 获取选择的项目的 iid
            MANAGE_PAGE.get(int(selected[0]))()

        tree.bind("<<TreeviewSelect>>", on_tree_select)

    def user_management(self):
        pass

    def user_list(self):
        pass

    def user_visualization(self):
        pass

    def operator_management(self):
        pass

    def operator_list(self):
        pass

    def vehicle_management(self):
        pass

    def vehicle_list(self):
        pass

    def vehicle_visualization(self):
        pass

    def order_management(self):
        pass

    def order_list(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()  # 创建Tkinter根窗口
    app = MyApp(root)  # 创建实例
    root.mainloop()  # 保持程序运行
