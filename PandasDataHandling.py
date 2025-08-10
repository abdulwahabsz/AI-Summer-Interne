import pandas as pd

# Series
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)

# DataFrame from dict
data = {
    'Name': ['Wahab', 'Sara', 'Mariam'],
    'Age': [22, 28, 23],
    'Salary': [50000, 60000, 55000]
}
df = pd.DataFrame(data)
#Viewing DataFrame
print(df)
print(df.head())     # First 5 rows
print(df.tail(2))    # Last 2 rows
print(df.info())     # Structure
print(df.describe()) # Summary stats

#Selecting data
print(df['Name'])              # Column
print(df[['Name', 'Age']])     # Multiple columns
print(df.iloc[0])               # Row by index
print(df.loc[1, 'Salary'])      # Specific cell
