import pandas as pd
import copy, ast


class TedAnalyzer:
    """
    the building function it gets the file path and reads it and put it on the data attribute
    """
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    """
    return the copy of the data 
    """
    def get_data(self):
        return copy.deepcopy(self.data)
    """
    the function return the shape of the data attribute
    """
    def get_data_shape(self):
        return self.data.shape
    """
    Returns a Dataframe object that contains a copy of the top ​n ​ rows from the ​data ​ attribute, that has the highest values in the 
column_name ​ column. If n is bigger than the number of rows in ​data ​ attribute, return all of the rows. 
    """
    def get_top_n_by_col(self, column_name, n):
        if n > self.get_data_shape()[0]:
            return self.get_data()
        else:
            return copy.deepcopy(self.data.nlargest(n, column_name))
    """
    Returns a list of the unique values in the column ​column_name ​ . 
    """
    def get_unique_values_as_list(self, column_name):
        return list(self.get_data()[column_name].unique())
    """
    Returns a dictionary of the unique value in column ​column_name ​ as keys and the number of rows they appear in as values.  
    """
    def get_unique_values_as_dict(self, column_name):
        return dict(self.get_data()[column_name].value_counts())
    """
    Return a Series object with counts of the null values in each column. 
    """
    def get_na_counts(self):
        return self.data.isnull().sum(axis=0)
    """
    Returns a copy of the ​data ​ attribute with all the rows that contain at least one null value.
    """
    def get_all_na(self):
        return self.get_data()[pd.isnull(self.get_data()).any(axis=1)]
    """
    Removes all rows that contain at least a single column with null value from the ​data ​ attribute and resets the index of the result DataFrame. Note that this method mutates the ​data attribute
    """
    def drop_na(self):
        #new_column_values = pd.Series([])
        #for i in range(self.get_data().shape[0]):
            #new_column_values[i] = i
        #self.data.insert(0, 'index', new_column_values)
        self.data.dropna(inplace=True)
        self.data.reset_index(drop=False,inplace=True)
        return None
    """
    Returns a list of all the unique strings from the “tags” column. Suggested approach: start by transforming all the rows strings containing a Python list into a list type object. 
    """
    def get_unique_tags(self):
        new_list = []
        for i in self.get_data()['tags']:
            new_list.extend(ast.literal_eval(i))
        used = set()
        unique = [x for x in new_list if x not in used and (used.add(x) or True)]
        return unique
    """
    Adds a new column called new_column_name ​ to the ​data ​ attribute that shows the “duration” value in minutes instead of seconds
    """
    def add_duration_in_minutes(self, new_column_name):
        new_column_values = pd.Series([])
        for i in range(self.get_data().shape[0]):
            new_column_values[i] = int(self.get_data()['duration'][i]*0.016666666666667)
        self.data.insert(self.get_data().shape[1],new_column_name,new_column_values)
        return None
    """
    Returns a subset of the ​data ​ attribute with all the rows that their ​column_name ​ values exceed the ​threshold. 
    """
    def filter_by_row(self, column_name, threshold):
        filterd = self.get_data()
        for i in range(self.get_data().shape[0]):
            if self.get_data()[column_name][i] < threshold:
                filterd = filterd.drop([i])
        return filterd
