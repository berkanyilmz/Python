import pandas as pd
import numpy as np


class DatasetHelper:
    def csv_reader(self, path):
        return pd.read_csv(path)

    def intersection(self, df, column, values):
        # Removes column information other than the one sought in the data set
        return df[df[column].isin(values)]

    def not_intersection(self, df, column, values):
        # Removes the column information sought in the data set
        return df[~df[column].isin(values)]

    def remove_duplicates(self, df, column):
        # Removes duplicate data from a column
        return df.drop_duplicates(column)

    def merge_dataframes(self, df1, df2, column=None, join='inner', left_join=None, right_join=None):
        """
        Merge two dataframes
        :param df1: Primary dataframe
        :param df2: Secondary dataframe
        :param column: Column name to merge
        :param join: Merge type
        :param left_join: Column name of the left dataframe
        :param right_join: Column name of the right dataframe
        :return:
        """
        return pd.merge(df1, df2, how=join, on=column, left_on=left_join, right_on=right_join)

    def change_datetime(self, df, column):
        # Change the datetime format to date
        df[column] = pd.to_datetime(df[column])
        return df[column].dt.date

    def percentage_of_nan(self, df, ):
        # Calculate the percentage of missing
        return df.isnull().mean() * 100

    def drop_columns(self, df, missing_percentages, threshold):
        # Select and remove columns greater than threshold%
        columns_to_drop = missing_percentages[missing_percentages > threshold].index
        for column in columns_to_drop:
            df.drop(column, axis=1, inplace=True)

    def fix_outliers(self, df):
        # Find and correct outliers in the dataset
        for column in df.select_dtypes(include=['float64', 'int64']).columns:
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            df[column] = np.where(df[column] < lower_bound, lower_bound,
                                  np.where(df[column] > upper_bound, upper_bound, df[column]))
        return df

    def fill_nan(self, df):
        # Fill missing data
        df.fillna(df.mean(numeric_only=True), inplace=True)
        for column in df.select_dtypes(include=['object']).columns:
            if df[column].isnull().any():
                df[column].fillna(method='ffill', inplace=True)