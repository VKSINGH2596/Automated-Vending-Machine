# from database import Datahub
#
#
# data = Datahub('tblUsers', 'vending_machine', 'DESKTOP-UQNO8AE')
# data_cursor = data.data_selection('*', "vUserId='VM-1' vPassword = 'Silly'")
# row = data_cursor.fetchone()
# while row:
#     print(row[:])
#     row = data_cursor.fetchone()
#
# #
# #
# #
# # def update(column_value, where_condition, table_name):
# #     # my_con = pyodbc.connect(fr'Driver=SQL Server;Server={server_name};Database={database_name};Trusted_Connection=yes;')
# #     # my_cursor = my_con.cursor()
# #     sql_query = f"Update {table_name} set {column_value} where {where_condition}"
# #     # my_cursor.execute(sql_query)
# #     print(sql_query)
# #
# # update('vDescription = coffee1', "vCategoryCode = 'VMCF'", 'tblProductCategory')
#
#
# college = {
#     "Name": "Harvard University",
#     "Location": "Cambridge, Massachusetts.",
#     "Founded": "1636"
# }
#
# for item in college:
#     print(f'keys = {item} value = {college[item]}')


row = "Decimal('8')"

print(row[len(row)-3])