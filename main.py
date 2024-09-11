df = pd.read_csv('CSV FILE HERE')

value_counts_dict = {}

for column in df.columns:
    if df[column].dtype == 'object':
        value_counts = df[column].unique()
        value_counts_dict[column] = value_counts

for column, value_counts in value_counts_dict.items():
    print(f"Unique values for column '{column}':")
    print(value_counts)
    print()
