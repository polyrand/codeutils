"""Module with some useful functions to clean data."""

import pandas as pd
import numpy as np


# def convert_cat2num(df):
#     # Convert categorical variable to numerical variable
#     num_encode = {'col_1': {'YES': 1, 'NO': 0},
#                   'col_2': {'WON': 1, 'LOSE': 0, 'DRAW': 0}}
#     df.replace(num_encode, inplace=True)


def check_missing_data(df):
    # check for any missing data in the df (display in descending order)
    return df.isnull().sum().sort_values(ascending=False)


def make_lower(df, cols):
    """Make columns with 'str' data lowercase."""
    df = df.copy()
    for col in cols:
        df[col] = df[col].astype(str).str.lower()

    return df


def correct_types(df, cols, types):
    """Change the type of each column in [cols] to each type in [types]."""
    assert(len(cols) == len(types))
    df = df.copy()
    for i in range(len(cols)):
        df[cols[i]] = df[cols[i]].astype(types[i])

    return df


def correct_col_str(df, columns):
    # remove a portion of string in a dataframe column - col_1
    if type(columns) == str:
        columns = [columns]

    df = df.copy()

    for col in columns:
        df[col] = df[col].astype(str).str.lower()
        df[col].replace('\n', '', regex=True, inplace=True)
        df[col].replace(' ', '_', inplace=True)
        df[col].replace('\n', '', regex=True, inplace=True)
        # remove all the characters after &# (including &#) for column - col_1
        df[col].replace(' &#.*', '', regex=True, inplace=True)

    return df