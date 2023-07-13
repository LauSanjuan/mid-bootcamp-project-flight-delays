import pandas as pd


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function takes a Pandas DataFrame as an input and standardizes the names of its columns,
    transforming all the letters to lower case and replacing the spaces with '_'.

    Inputs:
    df: Pandas DataFrame

    Outputs:
    A pandas DataFrame with its column names standardized.
    '''

    df2=df.copy()
    cols = []
    for colname in df2.columns:
        cols.append(colname.lower().replace(" ","_"))

    df2.columns = cols
    return df2


def time_columns_standardize(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    '''
    This function takes a Pandas DataFrame and a string as inputs and standardizes the values of the column,
    adding a 0 to the left, so all the values have 4 digits. Then it changes the column to time.

    Inputs:
    df: Pandas DataFrame
    column_name: string

    Outputs:
    A pandas DataFrame with the column values as time.
    '''
    df2 = df.copy()
    df2[column_name] = df2[column_name].apply(lambda x: f'{int(x):04}' if pd.notna(x) else x)
    df2[column_name] = pd.to_datetime(df2[column_name], format='%H%M',errors='coerce').dt.time
    
    return df2