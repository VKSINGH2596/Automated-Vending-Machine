from database import Datahub


data = Datahub('tblProductCategory', 'vending_machine', 'DESKTOP-UQNO8AE')
data_cursor = data.data_selection('*', vCategoryCode='VMCF')
row = data_cursor.fetchone()
while row:
    print(row[:])
    row = data_cursor.fetchone()



def update(column_value, where_condition, table_name):
    # my_con = pyodbc.connect(fr'Driver=SQL Server;Server={server_name};Database={database_name};Trusted_Connection=yes;')
    # my_cursor = my_con.cursor()
    sql_query = f"Update {table_name} set {column_value} where {where_condition}"
    # my_cursor.execute(sql_query)
    print(sql_query)

update('vDescription = coffee1', "vCategoryCode = 'VMCF'", 'tblProductCategory')