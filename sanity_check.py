def sanity_check(dataframe):
    # Checking for missing values
    missing_data = dataframe.isnull().sum()

    # Checking for duplicate rows
    duplicated = dataframe.duplicated().sum()

    # Identifying potential garbage values in object columns
    garbage_values = {}
    for col in dataframe.select_dtypes(include="object").columns:
        garbage_values[col] = dataframe[col].value_counts(dropna=False)

    return missing_data, duplicated, garbage_values


missing, dupes, garbage = sanity_check(dataframe)

print("Missing values:\n", missing)
print("\nDuplicated rows:", dupes)
print("\nObject column value counts:")
for col, values in garbage.items():
    print(f"\n{col}:\n{values}")
