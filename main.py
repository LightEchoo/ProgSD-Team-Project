import  InitializeDatabase
import SqlFunction

InitializeDatabase.initialize_etsp_database()
InitializeDatabase.input_default_data()

a = SqlFunction.get_all_cars()
b = SqlFunction.get_all_users()
print(a,'\n', b)

