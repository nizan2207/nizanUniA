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

    def find_tables_by_key(self, key):
        return list(map(lambda x: x.get_table_name(), filter(lambda y: key in y.get_key(), self.get_tables())))


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
        if self.is_fitted() == True and len(self.contains_key(row)) == 0 and self.equal_values(row) == True:
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

    def columns_names(self):
        col = self.get_other_columns() + self.get_key()
        return list(map(lambda x: x, col))

    def new_row_keys(self, new_row):
        keys = new_row.keys()
        return list(map(lambda x: x, keys))

    def is_fitted(self, new_row):
        new_row_keys = self.new_row_keys(new_row)
        col_names = self.columns_names()
        pt1 = all(list(map(lambda x: x in col_names, new_row_keys)))
        pt2 = all(list(map(lambda x: x in new_row_keys, col_names)))
        return pt1 and pt2

    def other_record_types(self, new_row):
        new_row_keys = self.new_row_keys(new_row)
        data_tp = self.get_values_types()
        row_data_tp = tuple(map(lambda x: data_tp.get(x), new_row_keys))
        res = {}
        for i in range(0, len(row_data_tp)):
            res[new_row_keys[i]] = row_data_tp[i]
        return res

    def equal_values(self, new_row):
        new_row_dict_tp = self.other_record_types(new_row)
        data_dict_tp = self.get_values_types()
        pt1 = all(list(map(lambda x: x in data_dict_tp, new_row_dict_tp)))
        pt2 = all(list(map(lambda x: x in new_row_dict_tp, data_dict_tp)))
        return pt1 and pt2

    def other_row_keys(self, new_row):
        keys_tb = self.get_key()
        keys_data = tuple(map(lambda x: new_row.get(x), keys_tb))
        res = {}
        for i in range(0, len(keys_tb)):
            res[keys_tb[i]] = keys_data[i]
        return res

    def contains_key(self, new_row):
        keys_and_val = self.other_row_keys(new_row)
        lst = list(map(lambda x: self.other_row_keys(x), self.get_records()))
        return list(filter(lambda x: keys_and_val == x, lst))

    def select(self, func):
        return list(filter(func, self.get_records()))

    def sum_of_column(self, column_name):
        if not self.get_records():
            return 0
        else:
            return reduce(lambda x, y: x + int(y[column_name]), self.get_records(), 0)
