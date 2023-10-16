import InitializeDatabase
import SqlFunction
import bike_share_app
import customer_BE
import operator_BE
import operator_FE
import operaor_and_manager_FE
import tkinter123

ini_flag = False

def ini_database():
    '''
    Function: if the database was established, then not redo it.
    Input: None
    return: None
    '''
    global ini_flag
    if not ini_flag:
        InitializeDatabase.initialize_etsp_database()
        InitializeDatabase.input_default_data()
        ini_flag = True

if __name__ == "__main__":

    ini_database()

    a = SqlFunction.get_all_cars()
    b = SqlFunction.get_all_users()
    print(a,'\n', b)

