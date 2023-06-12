# Complimentary Database module for accessing SQL Server and performing query actions
import pyodbc


class Datahub:

    def __init__(self, table_name, database_name, server_name):
        self.table_name = table_name
        self.my_con = pyodbc.connect(fr'Driver=SQL Server;Server={server_name};Database={database_name};Trusted_Connection=yes;')
        self.my_cursor = self.my_con.cursor()

    def __str__(self):
        """Method for returning Object info."""
        return f"Datatable hub selected for '{self.table_name}' table."

    def _where_condition(self, clause_dict):
        """Non-public method for creating the where clauses for queries."""
        str_clause = " where"
        my_clause = ""
        for key, value in clause_dict.items():
            my_clause += f" {key} = '{value}' ;"

        my_clause = my_clause.replace(';', 'and')
        str_clause += my_clause[:(len(my_clause) - 3)]
        return str_clause

    def data_selection(self, *columns, **clause):
        my_columns = ', '.join(columns)
        my_indexes = ''
        if clause != {}:
            my_indexes = self._where_condition(clause)

        sql_query = f"Select {my_columns} from {self.table_name}{my_indexes}"
        self.my_cursor.execute(sql_query)
        return self.my_cursor

    # def select(self, columns, clause):
    #     if clause != '':
    #         sql_query = f"Select {columns} from {self.table_name} where {clause}"
    #     else:
    #         sql_query = f"Select {columns} from {self.table_name}"
    #
    #     self.my_cursor.execute(sql_query)
    #     return self.my_cursor

    def connection_close(self):
        self.my_con.close()

    def data_update(self, column_value, where_condition):
        sql_query = f"Update {self.table_name} set {column_value} where {where_condition}"
        self.my_cursor.execute(sql_query)
        return self.my_cursor

    def data_delete(self, where_condition):
        sql_query = f"Delete from {self.table_name} where {where_condition}"
        self.my_cursor.execute(sql_query)
        return self.my_cursor

    def data_insert(self, **values):
        my_columns = ''
        my_values = ''
        for data in values:
            my_columns += data + ', '
            my_values += "'"+values[data] + "', "
        my_columns = my_columns[:len(my_columns)-2]
        my_values = my_values[:len(my_values) - 2]
        sql_query = f"Insert into {self.table_name} ({my_columns}) values ({my_values})"
        self.my_cursor.execute(sql_query)
        self.my_con.commit()
        sql_query1 = f"Select IDENT_CURRENT('{self.table_name}') "
        self.my_cursor.execute(sql_query1)
        return self.my_cursor
