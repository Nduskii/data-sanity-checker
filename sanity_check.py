# import libraries
import pandas as pd

def sanity_check(dataframe):
    """
    Perform a quick sanity check on a pandas DataFrame.

    Returns:
        missing_data (pd.Series): Count of missing values per column.
        duplicated (int): Number of duplicate rows.
        garbage_values (dict): Value counts for object columns (helps spot inconsistencies).
    """
    # Check for missing values
    missing_data = dataframe.isnull().sum()

    # Check for duplicate rows
    duplicated = dataframe.duplicated().sum()

    # Identify potential garbage values in object columns
    garbage_values = {}
    for col in dataframe.select_dtypes(include="object").columns:
        garbage_values[col] = dataframe[col].value_counts(dropna=False)

    return missing_data, duplicated, garbage_values
