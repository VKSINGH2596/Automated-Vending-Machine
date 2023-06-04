from database import Datahub


data = Datahub('tblProductCategory', 'vending_machine', 'DESKTOP-UQNO8AE')
data_cursor = data.data_selection('*', vCategoryCode='VMCF')
row = data_cursor.fetchone()
while row:
    print(row[:])
    row = data_cursor.fetchone()
