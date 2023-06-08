import pyodbc
from CoffeePackage import database

class MyUserLogin:
    def __init__(self):
        print("Welcome to Automated Vending Machine\nKindly choose from the below options:")
        self.option = input("  EXISTING USER (PRESS - A)       NEW USER (PRESS - B)\n-- ").upper()
        if self.option.isalpha() and len(self.option) == 1:
