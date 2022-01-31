import copy
from functools import reduce


class Schema:

    def __init__(self, name):
        self.__tables = []
        self.__schema_name = name

    def get_tables(self):
        return self.__tables

    def add_table(self, table):
        self.__tables.append(table)

    def get_name(self):
        return self.__schema_name

    find_tables_by_key = lambda self, key: list(map(lambda x: x.get_table_name(), filter(lambda y: key in y.get_key(), self.get_tables())))


class Table:
    def __init__(self, key_set, other_columns, values_types, table_name):
        self.__key = tuple(key_set)
        self.__other_columns = tuple(other_columns)
        self.__records = []
        self.__table_name = table_name
        self.__values_types = copy.deepcopy(values_types)

    def __repr__(self):
        columns = []
        res = 'Table: ' + self.__table_name + '\n'
        res += "Columns: "
        for key in self.__key:
            res += str(key) + '(Key) '
            columns.append(key)
        for column in self.__other_columns:
            res += column + ' '
            columns.append(column)
        res += '\nRows:\n'
        for row in self.__records:
            for k in columns:
                res += str(row[k]) + '\t'
            res += '\n'
        return res

    def add_record(self, row):
        is_fit = self.is_fitted(row)
        ###
        is_equal = self.equal_values(row)
        ###
        if self.contains_key(row):
            is_in = False
        else:
            is_in = True
        ###
        if is_fit and is_equal and is_in:
            self.__records.append(row)

    def get_key(self):
        return self.__key

    def get_values_types(self):
        return self.__values_types

    def get_other_columns(self):
        return self.__other_columns

    def get_table_name(self):
        return self.__table_name

    def get_records(self):
        return self.__records

    columns_names = lambda self: list(map(lambda x: x, (self.get_other_columns()) + self.get_key()))

    new_row_keys = lambda self, new_row: list(map(lambda x: x, new_row.keys()))

    is_fitted = lambda self, new_row: (all(list(map(lambda x: x in self.columns_names(), self.new_row_keys(new_row)))) == True) and (all(list(map(lambda x: x in self.new_row_keys(new_row),self.columns_names()))) == True)

    other_record_types = lambda self, new_row: dict(([(key,type(new_row[key])) for key in new_row]))

    equal_values = lambda self, new_row: (all(list(map(lambda x: x in self.get_values_types(), self.other_record_types(new_row)))) == True) and ((all(list(map(lambda x: x in self.other_record_types(new_row), self.get_values_types()))) == True))

    other_row_keys = lambda self, new_row: dict([(key,new_row[key]) for key in self.get_key()])
    
    contains_key = lambda self, new_row: any(list(map(lambda x: self.other_row_keys(new_row)==self.other_row_keys(x), list(map(lambda x: x, self.get_records())))))

    selct =lambda self, func: list(filter(func, self.get_records()))

    sum_of_column = lambda self, column_name: lambda x: 0 if not self.get_records() else reduce(lambda x, y: x + int(y[column_name]), self.get_records(), 0)
