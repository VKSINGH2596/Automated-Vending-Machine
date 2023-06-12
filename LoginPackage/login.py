from CoffeePackage.database import Datahub
class Login:

    def __init__(self,password,userid,username):
        self.password = password
        self.userid = userid
        self.username = username
    def login_page(self):
        login = Datahub('tblUsers', 'vending_machine', 'DESKTOP-UQNO8AE')
        data_cursor = login.data_selection('*', vUserId=self.userid, vPassword=self.password)
        row = data_cursor.fetchone()
        if row:
            print(f"Hi {row[2]}! Welcome Back 👋. Here is today's menu📜. Happy to serve you 💗.")
            return True
        else:
            print("Hey there! Please check your userid or password and try again 🤗.")
            return False

    def new_login(self):
        new_user = Datahub('tblUsers', 'vending_machine', 'DESKTOP-UQNO8AE')
        data_cursor = new_user.data_insert(vUserName=f'{self.username}', vPassword=f'{self.password}')
        row = data_cursor.fetchone()
        my_id = row[0]
        data_cursor = new_user.data_selection('vUserId', iId=my_id)
        row = data_cursor.fetchone()
        if row:
            print(f"Hi {self.username}👋 here is your User ID {row[0]}. Enjoy your time here.")
            return True
        else:
            return False


# obj = Login('Silly1','VM-21','Ayush')
# if obj.new_login():
#     while not obj.login_page():
#         obj.login_page()




