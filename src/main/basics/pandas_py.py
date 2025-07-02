import pandas as pd
# Create a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
# Calculate the average age
average_age = df['Age'].mean()
print("Average age:", average_age) # Output: Average age: 30.0
