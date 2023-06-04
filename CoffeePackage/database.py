# Complimentary Database module for accessing SQL Server and performing query actions
import pyodbc


class Datahub:
    my_con = pyodbc.connect(r'Driver=SQL Server;Server=GHOST-ASSASSIN;Database=Sample_database;Trusted_Connection=yes;')
    my_cursor = my_con.cursor()

    def __init__(self, table_name):
        self.table_name = table_name

    def __str__(self):
        """Method for returning Object info."""
        return f"Datatable hub selected for '{self.table_name}' table."

    def _where_condition(self, clause_dict):
        """Non-public method for creating the where clauses for queries."""
        str_clause = " where"
        my_clause = ""
        for key, value in clause_dict.items():
            my_clause += f" {key} = {value} ;"

        my_clause = my_clause.replace(';', 'and')
        str_clause += my_clause[:(len(my_clause) - 3)]
        return str_clause

    def data_selection(self, *columns, **clause):
        my_columns = ', '.join(columns)
        my_indexes = self._where_condition(clause)
        sql_query = f"Select {my_columns} from {self.table_name}{my_indexes}"
        self.my_cursor.execute(sql_query)
        return self.my_cursor
