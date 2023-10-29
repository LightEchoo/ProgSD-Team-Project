import os


import InitializeDatabase
import SqlFunction as sqF
import FE_bs as FE
import pdsql

import tkinter as tk

# db_ini_flag = False
#
# def ini_database():
#     '''
#     Function: if the database was established, then not redo it.
#     Input: None
#     return: None
#     '''
#     global db_ini_flag
#     if not db_ini_flag:
#         InitializeDatabase.initialize_etsp_database()
#         InitializeDatabase.input_default_data()
#         db_ini_flag = True

def ini_database():
    # 文件名
    data_filename = "etsp_database.db"

    # 检测文件是否存在
    if os.path.exists(os.path.join(os.getcwd(), data_filename)):
        print(f"{data_filename} exists in the current directory.")
        InitializeDatabase.initialize_etsp_database()  # 创建数据库
        pdsql.test_data_initialization()  # 初始化数据库
    else:
        print(f"{data_filename} does not exist in the current directory.")
if __name__ == "__main__":

    ini_database()
    FE.main()


    # pd_users = pdsql.get_all_users()
    # pd_cars = pdsql.get_all_cars()
    # pd_orders = pdsql.get_all_orders()

    # print(pd_users)
    # print(pd_cars)
    # print(pd_orders)

    # root = tk.Tk()  # 创建Tkinter根窗口
    # app = FE_bs.MyApp(root)  # 创建实例
    # root.mainloop()  # 保持程序运行
