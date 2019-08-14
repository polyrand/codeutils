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


def factorize(data, cols_bin=None, cols_muti=None):
    df = data.copy()

    if cols_bin:
        for column in cols_bin:
            df[column] = df[column].factorize()[0]
    else:
        print('No columns to encode binary')

    if cols_muti:
        for column in cols_muti:
            df = pd.concat(df, pd.get_dummies(df[column]), axis=1)
            df.drop(column, axis=1, inplace=True)
    else:
        print('No columns to one-hot enconde')

    return df


def remove_counts(df: pd.DataFrame, column: str):
    """Remove conditioned on value_counts()"""

    assert isinstance(column, str)

    df = df.copy()

    df = df[
        df[column]
        != df[column].value_counts().loc[df[column].value_counts() < 2].index[0]
    ]

    return df

# dict 2 case_when
# def case_when(row):
#     if (row['IMDB_Rating'] >= 0) & (row['IMDB_Rating'] <= 6): return 'OK'  elif (row['IMDB_Rating'] > 6) & (row['IMDB_Rating'] <= 8):
#         return 'Good'

#     else:
#         return 'Excellent'

# # apply case_when function
# mydata['IMDB_cat'] = mydata.apply(case_when, axis=1)

# # https://stackoverflow.com/a/49228646
# pd_df['difficulty'] = 'Unknown'
# pd_df.loc[pd_df['Time'].between(0, 30, inclusive=False), 'difficulty'] = 'Easy'
# pd_df.loc[pd_df['Time'].between(30, 60, inclusive=True), 'difficulty'] = 'Medium'

# pd_df['difficulty'] = np.select(
#     [
#         pd_df['Time'].between(0, 30, inclusive=False),
#         pd_df['Time'].between(30, 60, inclusive=True)
#     ],
#     [
#         'Easy',
#         'Medium'
#     ],
#     default='Unknown'
# )


# pd_df['difficulty'] = np.where(
#      pd_df['Time'].between(0, 30, inclusive=False),
#     'Easy',
#      np.where(
#         pd_df['Time'].between(0, 30, inclusive=False), 'Medium', 'Unknown'
#      )
# )

# def func(row):
#     if row['mobile'] == 'mobile':
#         return 'mobile'
#     elif row['tablet'] =='tablet':
#         return 'tablet'
#     else:
#         return 'other'

# df['combo'] = df.apply(func, axis=1)
