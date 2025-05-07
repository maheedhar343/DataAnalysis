import pandas as pd

# Step 1: Data Extraction
print("Step 1: Data Extraction")
data = pd.read_csv('sales_data.csv')
print(data.head())

# Step 2: Data Cleaning
print("\nStep 2: Data Cleaning")
print("Missing Values:\n", data.isnull().sum())
data_cleaned = data.drop_duplicates()
print("Shape before removing duplicates:", data.shape)
print("Shape after removing duplicates:", data_cleaned.shape)
data_cleaned.to_csv('sales_data_cleaned.csv', index=False)

# Step 3: Data Wrangling
print("\nStep 3: Data Wrangling")
data_wrangled = pd.read_csv('sales_data_cleaned.csv')
data_wrangled.set_index('OrderID', inplace=True)
data_wrangled['Date'] = pd.to_datetime(data_wrangled['Date'])
data_wrangled['TotalSales'] = data_wrangled['Price'] * data_wrangled['Quantity']
data_wrangled = pd.get_dummies(data_wrangled, columns=['Category', 'Region'], drop_first=True)
print(data_wrangled.head())
data_wrangled.to_csv('sales_data_wrangled.csv')
print("Wrangled data saved as sales_data_wrangled.csv")