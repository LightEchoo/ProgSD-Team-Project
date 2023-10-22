import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import random


class MyApp:
    def __init__(self, root):
        """
        构造函数，初始化应用程序
        :param root: 根窗口
        """
        self.root = root  # 传入的根窗口存储在类的属性root
        self.root.title("My App")
        self.root.geometry('1600x800')
        self.current_middle_page = None  # 跟踪当前显示的页面
        self.last_middle_page = None

        self.show_first_page()

    def show_first_page(self):
        """
        初次显示页面
        :return: None
        """
        f_main = tk.Frame(self.root, relief='groove', borderwidth=3, bg='yellow')
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)
        top = self.frame_top(f_main)
        middle = self.frame_middle(f_main)
        self.login_page(middle)
        # self.frame_bottom(f_main)

    def frame_top(self, frame, icon_file='images/bike.png', current_page_name='electric transportation sharing'):
        """
        顶部导航栏
        :param frame: 父frame
        :param icon_file: 图标
        :param current_page_name: 当前页面名称
        :return: f_top
        """
        f_top = tk.Frame(frame, relief='groove', borderwidth=5, bg='green')
        f_top.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        icon = Image.open(icon_file)
        icon = icon.resize((80, 80), Image.Resampling.LANCZOS)  # 重置图像大小
        icon = ImageTk.PhotoImage(icon)
        l_icon = tk.Label(f_top, image=icon, borderwidth=2, relief="solid")
        l_icon.image = icon  # 保持对图像的引用，以防止被垃圾回收
        l_icon.place(relx=0, rely=0, relwidth=0.05, relheight=1, bordermode='outside')

        l_name = tk.Label(f_top, text=current_page_name)
        l_name.place(relx=0.05, rely=0, relwidth=0.95, relheight=1)

        return f_top

    def frame_middle(self, frame):
        """
        中部主界面
        :param frame: 父frame
        :return: f_middle
        """
        f_middle = tk.Frame(frame, bg='blue')
        f_middle.place(relx=0, rely=0.1, relwidth=1, relheight=0.8)

        return f_middle

    def frame_bottom(self, frame, f_middle):
        """
        底部导航栏
        :param frame: 父frame
        :return: f_bottom
        """
        f_bottom = tk.Frame(frame, bg='red', borderwidth=2, relief="groove", )
        f_bottom.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

        f_b_l = tk.Frame(f_bottom, bg='pink', padx=3, pady=3)
        f_b_l.place(relx=0, rely=0, relwidth=1 / 3, relheight=1)
        f_b_m = tk.Frame(f_bottom, bg='pink', padx=3, pady=3)
        f_b_m.place(relx=1 / 3, rely=0, relwidth=1 / 3, relheight=1)
        f_b_r = tk.Frame(f_bottom, bg='pink', padx=3, pady=3)
        f_b_r.place(relx=2 / 3, rely=0, relwidth=1 / 3, relheight=1)

        b_vehicle = tk.Button(f_b_l, text="Vehicle", command=lambda: self.user_place_page(f_middle))
        b_order = tk.Button(f_b_m, text="Order")
        b_home = tk.Button(f_b_r, text="Home")

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

        login_lab_frame = tk.LabelFrame(f_middle, text='Login', bg='orange')
        self.current_middle_page = login_lab_frame  # 将传入的page设置为当前页面

        login_lab_frame.place(relx=1 / 3, rely=1 / 3, relwidth=1 / 3, relheight=1 / 3)
        l_username = tk.Label(login_lab_frame, text='Account: ')
        l_username.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.2)
        e_username = tk.Entry(login_lab_frame)
        e_username.place(relx=0.4, rely=0.1, relwidth=0.4, relheight=0.2)
        l_psw = tk.Label(login_lab_frame, text='Password: ')
        l_psw.place(relx=0.1, rely=0.5, relwidth=0.2, relheight=0.2)
        e_psw = tk.Entry(login_lab_frame)
        e_psw.place(relx=0.4, rely=0.5, relwidth=0.4, relheight=0.2)

        username = e_username.get()
        psw = e_psw.get()

        b_login = tk.Button(login_lab_frame, text='Login', command=lambda: self.login_test(username, psw))
        b_login.place(relx=0.2, rely=0.8, relwidth=0.2, relheight=0.2)
        b_register = tk.Button(login_lab_frame, text='Register', command=lambda: self.register_page(f_middle))
        b_register.place(relx=0.6, rely=0.8, relwidth=0.2, relheight=0.2)

        return login_lab_frame

    def register_page(self, f_middle):
        """
        创建注册界面
        :param f_middle: 父frame，中部框架
        :return: Nome
        """
        self.middle_page_clear()

        register_lab_frame = tk.LabelFrame(f_middle, text='Register')
        self.current_middle_page = register_lab_frame  # 将传入的page设置为当前页面

        register_lab_frame.place(relx=1 / 3, rely=1 / 3, relwidth=1 / 3, relheight=1 / 3)
        l_username = tk.Label(register_lab_frame, text='Account: ')
        l_username.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.2)
        e_username = tk.Entry(register_lab_frame)
        e_username.place(relx=0.4, rely=0.1, relwidth=0.4, relheight=0.2)
        l_psw = tk.Label(register_lab_frame, text='Password: ')
        l_psw.place(relx=0.1, rely=0.5, relwidth=0.2, relheight=0.2)
        e_psw = tk.Entry(register_lab_frame)
        e_psw.place(relx=0.4, rely=0.5, relwidth=0.4, relheight=0.2)

        b_login = tk.Button(register_lab_frame, text='Return', command=lambda: self.login_page(f_middle))
        b_login.place(relx=0.2, rely=0.8, relwidth=0.2, relheight=0.2)
        b_register = tk.Button(register_lab_frame, text='Register', command=lambda: self.register_test(f_middle))
        b_register.place(relx=0.6, rely=0.8, relwidth=0.2, relheight=0.2)

    def login_test(self, username, psw):
        """
        登录测试
        :param username: 用户名
        :param psw: 密码
        :return: None
        """
        pass
        flag = 0
        if flag == 0:  # 用户界面
            self.user_main_page()
        elif flag == 1:  # 操作员界面
            self.operator_main_page()
        elif flag == 2:  # 管理员界面
            self.admin_main_page()
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
        f_main = tk.Frame(self.root, relief='groove', borderwidth=3, bg='yellow')
        f_main.place(relx=0, rely=0, relwidth=1, relheight=1)
        top = self.frame_top(f_main)
        middle = self.frame_middle(f_main)
        self.user_place_page(middle)
        self.frame_bottom(f_main, middle)

    def user_place_page(self, f_middle):
        """
        位置选择界面
        :param f_middle: 中部框架
        :return:
        """
        self.middle_page_clear()

        choose_place_lab_frame = tk.Frame(f_middle, bg='blue')
        self.current_middle_page = choose_place_lab_frame  # 将传入的page设置为当前页面

        choose_place_lab_frame.place(relx=0.1, rely=1 / 6, relwidth=0.8, relheight=2 / 3)

        l_pickup = tk.Label(choose_place_lab_frame, text='Pickup Location: ')
        l_pickup.place(relx=0.2, rely=1 / 16, relwidth=0.6, relheight=1 / 8)
        l_return = tk.Label(choose_place_lab_frame, text='Return Location: ')
        l_return.place(relx=0.2, rely=7 / 16, relwidth=0.6, relheight=1 / 8)

        v_pickup = tk.StringVar()  # 用户选择的出发位置
        v_return = tk.StringVar()  # 用户选择的到达位置

        locations = ['l1', 'l2', 'l3', 'l4', 'l5']  # 地点位置list

        c_pickup = ttk.Combobox(choose_place_lab_frame, textvariable=v_pickup, values=locations)
        c_pickup.place(relx=0.2, rely=4 / 16, relwidth=0.6, relheight=1 / 8)
        c_return = ttk.Combobox(choose_place_lab_frame, textvariable=v_return, values=locations)
        c_return.place(relx=0.2, rely=10 / 16, relwidth=0.6, relheight=1 / 8)

        b_map = tk.Button(choose_place_lab_frame, text='Map', command=self.view_map)
        b_map.place(relx=0.2, rely=13 / 16, relwidth=0.2, relheight=1 / 8)
        b_booking = tk.Button(choose_place_lab_frame, text='Booking', command=lambda: self.booking_page(f_middle))
        b_booking.place(relx=0.6, rely=13 / 16, relwidth=0.2, relheight=1 / 8)

    def view_map(self):
        """
        跳出新界面显示一个静态的地图，上面有各个位置选项的信息
        :return: None
        """
        pass

    def booking_page(self, f_middle):
        """

        :param f_middle:
        :return: None
        """
        flag = True
        if flag:  # 用户输入信息正确检测
            pass

        self.middle_page_clear()

        # 上层车辆状态筛选条件 和 根据电量/价格排序 frame
        f_condition = tk.Frame(f_middle, bg='purple', padx=2, pady=2)
        f_condition.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.1)

        # 选车界面 frame
        f_select_vehicle = tk.Frame(f_middle, bg='pink', padx=2, pady=2)
        f_select_vehicle.place(relx=0.02, rely=0.12, relwidth=0.96, relheight=0.87)

        # 创建一个Canvas小部件，它用于包含可滚动的内容。
        canvas_vehicle = tk.Canvas(f_select_vehicle)
        # 将Canvas小部件放置在中部窗口中，使其在左侧占据空间，并允许其在水平和垂直方向上扩展以填满可用空间。
        canvas_vehicle.place(relx=0, rely=0, relwidth=0.9, relheight=1)

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
        scrollbar.place(relx=0.9, rely=0, relwidth=0.1, relheight=1)
        # 配置Canvas小部件以与垂直滚动条(scrollbar)相关联，使它能够通过滚动条进行垂直滚动。
        canvas_vehicle.configure(yscrollcommand=scrollbar.set)
        # 创建一个Frame小部件，该Frame用于包含实际的滚动内容。
        f_vehicle = tk.Frame(canvas_vehicle)
        # # 将Frame小部件添加到Canvas中，并配置Frame在Canvas上的位置，以及锚点在左上角（NW表示北西）。
        canvas_vehicle.create_window((0, 0), window=f_vehicle, anchor=tk.NW)

        # 设置测试list，实际上此处要替换为后端数据
        pass
        vehicle_no = range(10)
        vehicle_type = [random.randint(0, 1) for _ in range(10)]
        battery_lift = [random.uniform(0, 1) * 100 for _ in range(10)]
        rent = [random.uniform(0, 1) * 10 for _ in range(10)]

        for vehicle_no, vehicle_type, battery_lift, rent in zip(vehicle_no, vehicle_type, battery_lift, rent):
            single_vehicle_bar = self.single_vehicle_bar(f_vehicle, vehicle_no, vehicle_type, battery_lift, rent)
            single_vehicle_bar.pack()

        def on_canvas_configure(event): # 内置函数 配置Canvas以根据内容自动调整滚动区域
            canvas_vehicle.configure(scrollregion=canvas_vehicle.bbox("all"))

        # 绑定一个事件处理函数，当Frame的配置发生变化时，将调用on_canvas_configure函数来自动调整Canvas的滚动区域。
        f_vehicle.bind("<Configure>", on_canvas_configure)

        def on_mousewheel(event):
            canvas_vehicle.yview_scroll(-1 * (event.delta // 120), "units")

        # 绑定鼠标滚轮事件
        canvas_vehicle.bind_all("<MouseWheel>", on_mousewheel)

    def single_vehicle_bar(self, frame, vehicle_no, vehicle_type, battery_lift, rent,
                           image_file='images/WechatIMG3255.jpg', ):
        """
        用于展示单个车辆信息条
        :param frame: 父框架
        :param vehicle_no: 车辆编号
        :param vehicle_type: 车辆类型
        :param battery_lift: 剩余电量
        :param rent: 租金
        :param image_file: 图片，默认为一个绿色电车图
        :return: single_frame 总框架
        """
        single_frame = tk.Frame(frame, width=360, height=100, relief='groove', bd=1)

        frame_image = tk.Frame(single_frame, width=100, height=100) # 最左侧图像框架
        frame_image.place(x=0, y=0)
        vehicle = Image.open(image_file)
        vehicle = vehicle.resize((100, 100), Image.Resampling.LANCZOS)  # 重置图像大小
        vehicle = ImageTk.PhotoImage(vehicle)
        l_icon = tk.Label(frame_image, image=vehicle, borderwidth=2, relief="solid")
        l_icon.image = vehicle  # 保持对图像的引用，以防止被垃圾回收
        l_icon.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8, bordermode='outside')

        frame_info = tk.Frame(single_frame, width=160, height=100) # 中部信息框架
        frame_info.place(x=100, y=0)
        v_vehicle_no = tk.StringVar() # 车辆编号
        v_vehicle_no.set('Vehicle No.' + str(vehicle_no))
        l_vehicle_no = tk.Label(frame_info, textvariable=v_vehicle_no)
        l_vehicle_no.pack()

        v_vehicle_type = tk.StringVar() # 车辆类型
        if vehicle_type == 0:
            v_vehicle_type.set("Vehicle type: electric bicycle")
        elif vehicle_type == 1:
            v_vehicle_type.set("Vehicle type: electric scooter")
        l_vehicle_type = tk.Label(frame_info, textvariable=v_vehicle_type)
        l_vehicle_type.pack()

        v_battery_life = tk.StringVar() # 剩余电量
        battery_lift = round(battery_lift, 2)
        v_battery_life.set("Battery life:" + str(battery_lift) + "%")
        l_battery_life = tk.Label(frame_info, textvariable=v_battery_life)
        l_battery_life.pack()

        v_rent = tk.StringVar() # 租金
        rent = round(rent, 2)
        v_rent.set("Rental cost £" + str(rent) + "%/h")
        l_rent = tk.Label(frame_info, textvariable=v_rent)
        l_rent.pack()

        frame_book = tk.Frame(single_frame, width=100, height=100) # 右侧预定按钮框架
        frame_book.place(x=300, y=0)
        b_booking = tk.Button(frame_book, text="Book")
        b_booking.place(x=0, y=40, width=40, height=20)

        return single_frame

    def user_vehicle_page(self):
        pass

    def user_order_page(self):
        pass

    def user_home_page(self):
        pass

    def operator_main_page(self):
        pass

    def admin_main_page(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()  # 创建Tkinter根窗口
    app = MyApp(root)  # 创建实例
    root.mainloop()  # 保持程序运行
