import InitializeDatabase
import SqlFunction as sqF
import FE_bs
import pdsql

import tkinter as tk

db_ini_flag = False

def ini_database():
    '''
    Function: if the database was established, then not redo it.
    Input: None
    return: None
    '''
    global db_ini_flag
    if not db_ini_flag:
        InitializeDatabase.initialize_etsp_database()
        InitializeDatabase.input_default_data()
        db_ini_flag = True

if __name__ == "__main__":

    ini_database()
    pdsql.test_data_initialization()

    pd_cars = pdsql.get_all_cars()
    pd_orders = pdsql.get_all_orders()

    print(pd_cars)
    print(pd_orders)

    # root = tk.Tk()  # 创建Tkinter根窗口
    # app = FE_bs.MyApp(root)  # 创建实例
    # root.mainloop()  # 保持程序运行

